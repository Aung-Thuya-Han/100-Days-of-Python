import random
print(r'''
__________               __                           
\______   \ ____   ____ |  | __                       
 |       _//  _ \_/ ___\|  |/ /                       
 |    |   (  <_> )  \___|    <                        
 |____|_  /\____/ \___  >__|_ \                       
        \/            \/     \/                       
__________                                            
\______   \_____  ______   ___________                
 |     ___/\__  \ \____ \_/ __ \_  __ \               
 |    |     / __ \|  |_> >  ___/|  | \/               
 |____|    (____  /   __/ \___  >__|                  
                \/|__|        \/                      
  _________      .__                                  
 /   _____/ ____ |__| ______ _________________  ______
 \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
/_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/     \/        \/     \/                 \/ ''')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_keys = [rock, paper, scissors]
print('Welcome to the Rock Paper Scissors Game!')
user_choice = int(input("Type '0' for rock, '1' for paper or '2' for scissors.\n"))
com_choice = random.randint(0, 2)

if user_choice in range(0,3):
    print("You choose")
    print(game_keys[user_choice])
    print("computer choose")
    print(game_keys[com_choice])
    
    if user_choice == 0 and com_choice == 2:
        print("You win!")
    elif user_choice > com_choice:
        print("You win!")
    elif user_choice == com_choice:
        print("It is a draw!")
    else:
        print("You lose!")
else:
    print("Wrong input.")




