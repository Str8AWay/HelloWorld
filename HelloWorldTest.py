import subprocess
import sys

expected = "Hello, World\n"

proc = subprocess.Popen(["java", "HelloWorld"], stdout=subprocess.PIPE)
output = proc.stdout.read()

if output != expected:
    sys.exit("Test failed.\nActual: " + output + "\nExpected: " + expected)

print "Tests passed"
