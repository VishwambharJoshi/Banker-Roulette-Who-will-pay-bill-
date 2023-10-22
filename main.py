import random
names_string = input("Provide me Everybuday's name separated by comma.\n ")
names_split = names_string.split(",")
person_who_pay_bill = random.choice(names_split)
#print(person_who_pay_bill + " is going to buy the meal today")
print(f"{person_who_pay_bill} is going to buy the meal today")
