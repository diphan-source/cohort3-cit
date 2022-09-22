
import sys

data = []

def is_full():
    return len(data) == 10

def check_queue():
    if len(data) == 0:
        return "Queue is empty"

def add_element():
    if not is_full():
        data.insert(0, input("Enter element: "))
        print(f"Element added to queue: {data}")
        return data

def remove_element():
    if not check_queue():
            data.pop()
            print(f"Element removed from queue: {data}")
            return data

    
def main():
    while True:
        print("1. Add element \n2. Remove element \n3. Check queue \n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_element()
        elif choice == "2":
            remove_element()
        elif choice == "3":
            print(check_queue())
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
    