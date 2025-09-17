print(r'''_________        .__               .__          __                
\_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________ 
/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \
\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/
 \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|   
        \/     \/          \/                \/                   ''')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Division by zero")
        exit()
    return n1 / n2

calculation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    first_number = int(input("Enter your first number: "))
    user_calculation = input("Choose one\n+, - , * or /: ")
    second_number = int(input("Enter your second number: "))
    answer = calculation[user_calculation](first_number, second_number)
    print(answer)

    while True:
        user_choice = input(f"Would you like to continue with {answer}? (y/n): ").lower()
        if user_choice == "y":
            first_number = answer
            user_calculation = input("Choose one\n+, - , * or /: ")
            second_number = int(input("Enter your second number: "))
            answer = calculation[user_calculation](first_number, second_number)
            print(answer)
        else:
            break
