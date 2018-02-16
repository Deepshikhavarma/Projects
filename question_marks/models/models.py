# -*- coding: utf-8 -*-

def QuestionsMarks(str): 
	numbers = "1234567890"
	lastdigit = None
	answer = "false"
	for i in range(len(str)):
		if str[i] in numbers:
			if lastdigit:
				if int(str[lastdigit]) + int(str[i]) == 10:
					if str[lastdigit:i].count("?") == 3:
						answer = "true"
					else:
						return "false"
			lastdigit = i
	return answer 
print QuestionsMarks(input())