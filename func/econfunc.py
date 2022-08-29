# create an ecommerence using dictionaries , loop , list , functions 

my_shop ={}

def create_products_container():
    if 'products' in my_shop:
        print("products already exists")
        return my_shop['products']
    else:
        my_shop['products'] = {}
        print("products container created")
        return my_shop['products']
    
def create_product(products , product_id , product_name , product_price):
    if product_id in products:
        print("product already exists")
        return products
    else:
        products[product_id] = {"name": product_name, "price": product_price}
        print("product created")
        return products
    
def update_product(products , product_id , product_name , product_price):
    if not product_id in products:
        print("product not found")
        return products
    products[product_id] = {"name": product_name, "price": product_price}
    return products

def delete_product(products , product_id):
    if not product_id in products:
        print("product not found")
        return products
    del products[product_id]
    return products

def show_products(products):
    for product_id , product_details in products.items():
        print(f"product_id:{product_id},name:{product_details['name']},price:{product_details['price']}")
        
def show_product(products , product_id):
    if not product_id in products:
        print("product not found")
        return products
    product_details = products[product_id]
    print(f"product_id:{product_id},name:{product_details['name']},price:{product_details['price']}")
    
def main():
    products = create_products_container()
    while True:
        print("Welcome to the ecommerence program")
        print("1. create a product \n2. update a product \n3. delete a product \n4. show all products \n5. show a product \n6. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            product_id = input("Enter the product id: ")
            product_name = input("Enter the product name: ")
            product_price = input("Enter the product price: ")
            create_product(products , product_id , product_name , product_price)
            print(f"{product_name} is added to the container")
        elif choice == "2":
            product_id = input("Enter the product id: ")
            product_name = input("Enter the product name: ")
            product_price = input("Enter the product price: ")
            update_product(products , product_id , product_name , product_price)
            print(f"product with prouduct_id:{product_id} is updated")
        elif choice == "3":
            product_id = input("Enter the product id: ")
            delete_product(products , product_id)
        elif choice == "4":
            show_products(products)
        elif choice == "5":
            product_id = input("Enter the product id: ")
            show_product(products , product_id)
        elif choice == "6":
            print("Thank you for using the ecommerence program")
            break
        else :
            print("Invalid choice")
            
main()