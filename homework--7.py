for number in range(1, 61):
    result = str(number)
    is_divisible = False

    if number % 2 == 0:
        if is_divisible == False:
            result = result + " - is divisible by 2"
        else: 
             result = result + ", is divisible by 2"
        is_divisible = True 

    if number % 3 == 0:
        if is_divisible == False:
            result = result + " - is divisible by 3"
        else:
            result = result + ", is divisible by 3"
        is_divisible = True

    if number % 5 == 0:
        if is_divisible == False:
            result = result + " - is divisible by 5"
        else:
            result = result + ", is divisible by 5"
        is_divisible = True
    
    print(result)

    