for number in range(1, 61):
    result = str(number)


    if number % 2 == 0:
        result = result + " - 2 ile bölünüyor"

    if number % 3 == 0:
        if "ile bölünüyor" in result:
            result = result + " ve 3 ile bölünüyor"
        else:
            result = result + " - 3 ile bölünüyor"

    if number % 5 == 0:
        if "ile bölünüyor" in result:
            result = result + " ve 5 ile bölünüyor" 
        else:
            result = result + " - 5 ile bölünüyor"

    print(result)