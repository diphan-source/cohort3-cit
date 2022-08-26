

# ecommerence program 

products = {
    "1": {"name": "laptop", "price": 1000, "quantity": 10},
    "2": {"name": "mobile", "price": 500, "quantity": 20},
}

while True:
    print("Welcome to the ecommerence program")
    print("1.Add Product \n2.Delete Product \n3.Update Product \n4.Display Products \n5.Exit")
    option = input("Enter your choice: ")
    if option == "1":
        id = input("Enter the id: ")
        name = input("Enter the name: ")
        price = input("Enter the price: ")
        quantity = input("Enter the quantity: ")
        if id in products:
            print("Product already exists")
            break
        products[id] = {"name": name, "price": price, "quantity": quantity}
        
    elif option == "2":
        if products[id] in products:
            del products[id]
        else:
            print("Product not found")
            
    elif option == "3":
        id = input("Enter the id: ")
        if id in products:
            name = input("Enter the name: ")
            price = input("Enter the price: ")
            quantity = input("Enter the quantity: ")
            products[id] = {"name": name, "price": price, "quantity": quantity}
        else:
            print("Product not found")
            
    elif option == "4":
        for key, value in products.items():
            print(f"{key} is {value}")
            
    elif option == "5":
        print("Thank you for using the ecommerence program")
        break
    else:
        print("Invalid choice")