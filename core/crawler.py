import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse

visited=set()

def crawl(url,depth=2):

    urls=[]

    if depth==0:
        return urls

    if url in visited:
        return urls

    visited.add(url)

    try:

        r=requests.get(url,timeout=5)

        soup=BeautifulSoup(r.text,"html.parser")

        for link in soup.find_all("a"):

            href=link.get("href")

            if not href:
                continue

            full=urljoin(url,href)

            if urlparse(full).netloc==urlparse(url).netloc:

                if full not in visited:

                    print("[URL]",full)

                    urls.append(full)

                    urls+=crawl(full,depth-1)

    except:
        pass

    return urls
