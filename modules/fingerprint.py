import requests

def fingerprint(url):

    tech=[]

    try:

        r=requests.get(url,timeout=5)

        body=r.text.lower()

        if "wordpress" in body:
            tech.append("WordPress")

        if "dvwa" in body:
            tech.append("DVWA")

        if "php" in r.headers.get("Server","").lower():
            tech.append("PHP")

    except:
        pass

    print("Detected:",tech)

    return tech
