# -*- coding: utf-8 -*-

def equal_check(str):
	for i in range(len(str)):
		if str[i]=="o" or str[i]=="O":
			a=str[i]
			print("obj1 =",a)
		else:
			b=str[i]
			print("obj2=",b)
	for x in range(len(a)):
		for y in range(len(b)):
			if x==y:
				print("Correct")
			else:
				print("Not Matched")

equal_check("OoXx")
