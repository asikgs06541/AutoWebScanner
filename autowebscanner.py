import argparse

from modules.portscan import port_scan
from modules.dirscan import dir_scan
from modules.fingerprint import fingerprint

from core.crawler import crawl
from core.engine import run_scan
from core.reporter import generate_report


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-u","--url",help="target url")

    args = parser.parse_args()

    if not args.url:

        print("Usage: python autowebscanner.py -u http://target")
        return


    target = args.url

    host = target.replace("http://","").replace("https://","").split("/")[0]


    print("\n[*] Port scanning")
    ports = port_scan(host)


    print("\n[*] Fingerprint detection")
    tech = fingerprint(target)


    print("\n[*] Crawling website")
    urls = crawl(target)


    print("\n[*] Directory scan")
    dirs = dir_scan(target)

    urls = urls + dirs


    print("\n[*] Vulnerability scan")
    results = run_scan(urls)


    print("\n[*] Generating report")
    generate_report(target,ports,urls,results,tech)


    print("\n[+] Scan finished")
    print("Report: report/report.html")


if __name__ == "__main__":
    main()
