# Dictionary


persons = []


while True:

    add_person = input("Would you like to add new person?")

    if add_person == "E":
        name = input("name: ")
        age = int(input("age: "))
        persons.append({"name": name, "age": age}) 


    elif add_person == "H":
        break

for person in persons:

    print("name: ", person["name"], "age: ", person["age"])
