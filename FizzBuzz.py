words = {3: "Fizz", 5 : "Buzz"}

for i in range (1, 101):
    result = ""
    for element in words:
        if(i % element == 0):
            result += words[element]
    print(i if result == ""  else result)
