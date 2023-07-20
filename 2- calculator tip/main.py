"""this code calcule the tip that you want to give the waiter"""

bill = float(input("whats is your bill $$ ?? \n"))
percetip = int(input('whats percentage do you wanna give 10%, 12%, 15%\n'))

peoples = int(input('how many people will split de bill\n'))

c = (bill*(percetip/100))

print('each person should pay {}'.format(round((c+bill)/peoples, 2)))



