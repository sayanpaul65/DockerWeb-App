#!/usr/bin/python3


import cgi
import subprocess as sb

print("content-type: text/html")
print()

print('''<style>
pre{
    color: black;
    font-weight: bold;
    font-size: 20px;
}
</style>''')


fs = cgi.FieldStorage()

cmd = fs.getvalue("commands")
output= sb.getoutput(cmd)
print("<body style='padding: 40px;'>")
print('<h1 style="color:#df405a;" >Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")

