words = {3:"Fizz",5:"Buzz"}
for i in range(1,101):
	result=""
	for key in words:
		if i % key == 0:
			result += str(words[key])
	if result == "":
		result=str(i)
	print(result)