def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def show_menu():
    print("\n=== SIMPLE CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_menu()
        option = input("Choose an option (1-5): ")

        if option == '5':
            print("Exiting... Have a nice day!")
            break

        if option in ['1', '2', '3', '4']:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers!")
                continue

            if option == '1':
                print("Result:", add(n1, n2))
            elif option == '2':
                print("Result:", subtract(n1, n2))
            elif option == '3':
                print("Result:", multiply(n1, n2))
            elif option == '4':
                print("Result:", divide(n1, n2))
        else:
            print("Invalid option! Please choose from 1 to 5.")

if __name__ == "__main__":
    main()