
# dict = {'name': 'John', 'age': 30 , 'likes': ['Python', 'C++']}
# get python from the dict using the key

# print(dict['likes'][0])

dict = {}
while True:
    print("Welcome to the dictionary program")
    print("1.Create User \n2.Delete User \n3.Update User \n4.Display Users \n5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        dict[name] = age
    elif choice == "2":
        name = input("Enter the name: ")
        if name in dict:
            del dict[name]
        else:
            print("User not found")
    elif choice == "3":
        name = input("Enter the name: ")
        if name in dict:
            age = input("Enter the age: ")
            dict[name] = age
        else: 
            print("User not found")
    elif choice == "4":
        for key, value in dict.items():
            print(f"{key} is {value} years old")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
    
   