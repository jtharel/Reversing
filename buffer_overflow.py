import subprocess

for X in range(100):
  buf = ("A"*X)
  print "Buffer: ", buf, "Buffer length: ", len(buf)
  
  p1 = subprocess.Popen(["test.exe", buf],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = p1.communicate()
  print stdout, stderr
  
