print(r'''
___________                                                   .___       .__                     .___
\__    ___/______   ____ _____    ________ _________   ____   |   | _____|  | _____    ____    __| _/
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  |   |/  ___/  | \__  \  /    \  / __ | 
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  |   |\___ \|  |__/ __ \|   |  \/ /_/ | 
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  > |___/____  >____(____  /___|  /\____ | 
                       \/     \/     \/                   \/           \/          \/     \/      \/ 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

user_choice = input("You are at a cross road. Where do you want to go?\nType 'left' or 'right'\n").lower()

if user_choice == "left":
    user_first_option = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swimm across\n").lower()
    if user_first_option == "wait":
        user_second_option = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n").lower()
        if user_second_option == "red":
            print("It's a room full of fire. Game Over.")
        elif user_second_option == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")