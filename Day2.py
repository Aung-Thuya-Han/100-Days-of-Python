logo = r'''
___________.__         _________        .__               .__          __                
\__    ___/|__|_____   \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________ 
  |    |   |  \____ \  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \
  |    |   |  |  |_> > \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/
  |____|   |__|   __/   \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|   
              |__|             \/     \/          \/                \/                   '''
print(logo)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_in_decimal = tip / 100
total_bill = bill + (tip_in_decimal * bill)
bill_for_one = total_bill / people

print(f"Each person should pay: ${bill_for_one:.2f}.")
