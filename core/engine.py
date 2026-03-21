from concurrent.futures import ThreadPoolExecutor

from plugins.sqli import scan as sqli_scan
from plugins.xss import scan as xss_scan
from plugins.formscan import scan as form_scan


def run_scan(urls):

    # ===== 只保留有参数的URL =====
    urls = list(set(urls))  # 去重
    param_urls = [u for u in urls if "?" in u]

    print(f"[*] 有效参数URL数量: {len(param_urls)}")

    results={"sqli":[],"xss":[],"forms":[]}

    # ===== SQLi =====
    with ThreadPoolExecutor(max_workers=10) as pool:
        for r in pool.map(sqli_scan,param_urls):
            if r:
                results["sqli"]+=r

    # ===== XSS =====
    with ThreadPoolExecutor(max_workers=10) as pool:
        for r in pool.map(xss_scan,param_urls):
            if r:
                results["xss"]+=r

    # ===== 表单 =====
    with ThreadPoolExecutor(max_workers=10) as pool:
        for r in pool.map(form_scan,urls):
            if r:
                results["forms"]+=r

    return results
