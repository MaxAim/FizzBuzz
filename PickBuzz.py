def FizzBuzz():
    amount = int(input("How many numbers will you choose?"))
    words = {}
    while amount > 0:
        x = int(input("Pick a number:"))
        y = input("Choose a word for that number:")
        words[x] = y
        amount = amount - 1
    for i in range(1,101):
        result=""
        for key in words:
            if i % key == 0:
                result += str(words[key])
        if result == "":
            result=str(i)
        print(result)

FizzBuzz()
