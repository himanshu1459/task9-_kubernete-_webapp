#!/usr/bin/python3

print("Content-type:text/html")
print()

import cgi,subprocess

a = cgi.FieldStorage()
cmd = a.getvalue("s")
print(cmd)
if "kubectl" in cmd:
    output = subprocess.getoutput("sudo "+cmd+" --kubeconfig admin.conf")
else:
    output = subprocess.getoutput("sudo " +cmd)
print(output)
