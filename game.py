import random

while True:
    n1 = random.randint(1,10)
    print(n1)
    n2 = int(input("Enter a number"))
    print(n2)
    if n2 == 0:
        break

    if n1 == n2:
        print("You Won")
    else:
        print("Better luck next time")
