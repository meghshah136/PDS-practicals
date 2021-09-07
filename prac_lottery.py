import random

lottery_number = random.randint(10,100)
lottery_number_str = str(lottery_number)

user_input = input("Enter 2 digit number : ")

if lottery_number_str == user_input:
    print("You won $10000 !!")
elif lottery_number_str == user_input[::-1]:
    print("You won $3000 !!")
else:
    for i in user_input:
        if i in lottery_number_str:
            print("You won $1000 !!")
            break
    else:
        print(f"Lottery number was : {lottery_number}")
        print("Sorry!! Better luck next time")