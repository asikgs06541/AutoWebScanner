import requests

def dir_scan(target):

    found=[]

    # 去掉参数部分
    base = target.split("?")[0]

    with open("payloads/dirs.txt") as f:
        dirs=f.read().splitlines()

    for d in dirs:

        url = base.rstrip("/") + "/" + d

        try:
            r=requests.get(url,timeout=5)

            if r.status_code==200:

                print("[DIR]",url)
                found.append(url)

        except:
            pass

    return found
