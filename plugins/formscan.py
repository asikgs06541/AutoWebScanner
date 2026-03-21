import requests
from bs4 import BeautifulSoup

payload="<script>alert(1)</script>"

def scan(url):

    vulns=[]

    try:

        r=requests.get(url,timeout=5)

        soup=BeautifulSoup(r.text,"html.parser")

        forms=soup.find_all("form")

        for form in forms:

            inputs=form.find_all("input")

            data={}

            for i in inputs:

                name=i.get("name")

                if name:
                    data[name]=payload

            res=requests.post(url,data=data)

            if payload in res.text:

                print("[FORM-XSS]",url)

                vulns.append(url)

    except:
        pass

    return vulns
