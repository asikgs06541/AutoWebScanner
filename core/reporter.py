import json

def generate_report(target, ports, urls, results, tech):

    f = open("report/report.html", "w")

    f.write("<html><body>")

    f.write("<h1>AutoWebScanner Report</h1>")

    f.write("<h2>Target</h2>" + target)

    f.write("<h2>Technology</h2>" + str(tech))

    f.write("<h2>Open Ports</h2>" + str(ports))

    f.write("<h2>URLs</h2>")
    for u in urls:
        f.write("<p>" + u + "</p>")


    # ===== SQL Injection =====
    f.write("<h2>SQL Injection</h2>")

    if results["sqli"]:
        for v in results["sqli"]:
            f.write("<p>")
            f.write("URL: " + v["url"] + "<br>")
            f.write("Parameter: " + v["param"] + "<br>")
            f.write("Type: " + v["type"])
            f.write("</p>")
    else:
        f.write("<p>No SQL Injection found</p>")


    # ===== XSS =====
    f.write("<h2>XSS</h2>")
    for x in results["xss"]:
        f.write("<p>" + str(x) + "</p>")


    # ===== 表单 =====
    f.write("<h2>Form Vulnerabilities</h2>")
    for f_v in results["forms"]:
        f.write("<p>" + str(f_v) + "</p>")


    f.write("</body></html>")

    f.close()

    json.dump(results, open("report/report.json", "w"), indent=4)
