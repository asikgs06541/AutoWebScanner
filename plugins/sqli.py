import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

session = requests.Session()

def scan(url):

    vulns=[]

    parsed=urlparse(url)
    params=parse_qs(parsed.query)

    if not params:
        return vulns

    for p in params:

        original=params[p][0]

        try:
            # ===== 原始请求 =====
            normal_res = session.get(url, timeout=5)

            # ===== 多种payload =====
            payloads_true = [
                " AND 1=1",
                "' AND '1'='1",
                " OR 1=1",
                "') AND ('1'='1"
            ]

            payloads_false = [
                " AND 1=2",
                "' AND '1'='2",
                " OR 1=2",
                "') AND ('1'='2"
            ]

            for t, f in zip(payloads_true, payloads_false):

                # TRUE
                params[p] = original + t
                true_q = urlencode(params, doseq=True)
                true_url = urlunparse(parsed._replace(query=true_q))
                true_res = session.get(true_url, timeout=5)

                # FALSE
                params[p] = original + f
                false_q = urlencode(params, doseq=True)
                false_url = urlunparse(parsed._replace(query=false_q))
                false_res = session.get(false_url, timeout=5)

                # ===== 判断逻辑（关键）=====
                if (normal_res.text == true_res.text and
                    normal_res.text != false_res.text and
                    abs(len(true_res.text) - len(false_res.text)) > 20):

                    print("[Boolean SQLi]", url, "param:", p)

                    vulns.append({
                        "url": url,
                        "param": p,
                        "type": "Boolean SQL Injection"
                    })

                    break

        except Exception as e:
            pass

        params[p] = original

    return vulns
