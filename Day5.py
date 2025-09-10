import random
print(r'''
__________                                               .___  
\______   \_____    ______ ________  _  _____________  __| _/  
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |   
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |   
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   
                \/     \/     \/                          \/   
  ________                                   __                
 /  _____/  ____   ____   ________________ _/  |_  ___________ 
/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/     \/     \/     \/           \/                   ''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_letters = []
pass_symbols = []
pass_numbers = []

for _ in range(nr_letters):
    pass_letters.append(random.choice(letters))

for _ in range(nr_symbols):
    pass_symbols.append(random.choice(symbols))

for _ in range(nr_numbers):
    pass_numbers.append(random.choice(numbers))

normal_password = pass_letters + pass_symbols + pass_numbers
normal_password_combined = ''.join(normal_password)
print(f"Normal password: {normal_password_combined}")

hard_password = pass_letters + pass_symbols + pass_numbers
random.shuffle(hard_password)
hard_password_combined = ''.join(hard_password)
print(f"Hard password: {hard_password_combined}")
