print("Choose a number between 1 and 100.")

small = 1
large = 100

while True:

    guess = int((small + large) / 2) 
    print("My guess: ", guess)

    answer = int(input("0 = small, 1 = large, 2 = true"))

    if answer == 2:
        print("True")
        break

    elif answer == 0:
        large = guess - 1

    elif answer == 1:
        small = guess + 1


