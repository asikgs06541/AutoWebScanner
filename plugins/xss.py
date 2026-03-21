import requests
from urllib.parse import urlparse,parse_qs,urlencode,urlunparse

payloads=open("payloads/xss.txt").read().splitlines()

def scan(url):

    vulns=[]

    parsed=urlparse(url)

    params=parse_qs(parsed.query)

    if not params:
        return vulns

    for p in params:

        for payload in payloads:

            params[p]=payload

            q=urlencode(params,doseq=True)

            new=urlunparse(parsed._replace(query=q))

            try:

                r=requests.get(new,timeout=5)

                if payload in r.text:

                    print("[XSS]",new)

                    vulns.append(new)

            except:
                pass

    return vulns
