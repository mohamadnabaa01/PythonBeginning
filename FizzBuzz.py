print("Welcome to FizzBuzz!")

def fizzbuzz(int):
    s1 = str(int)

    if "3" in s1:
        if (int % 3 != 0) and (int % 7 != 0):
            return "Almost Fizz"

    if (int % 3 == 0):
        if (int % 7 == 0):
            return "FizzBuzz"

        return "Fizz"

    if (int % 7 == 0):
        return "Buzz"

    return str(int)

num = int(input());

for i in range(1, num + 1):
    print(fizzbuzz(i))