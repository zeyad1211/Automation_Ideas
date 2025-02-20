people = {'zeyad': 0, 'abdelaziz': 0, 'malek': 0, 'yahia': 0, 'omar': 0} #change the names or add/remove to your preference
AC_only = 0
try:
    electricity_bill = float(input("Enter total electricity bill: "))
    electricity_rate = float(input("Enter the rate of electricty per KWh: "))
    Wifi_bill = float(input("Enter total wifi bill: "))
    Water_bill = float(input("Enter total water bill: "))
except:
    print("enter a number!")

for person, kw_ac in people.items():
    people[person] = float(input(f"How many KW did {person}'s AC consume? "))*electricity_rate
    AC_only += people[person]

total_bill_without_AC = electricity_bill - AC_only
splitted_bill = (total_bill_without_AC + Wifi_bill + Water_bill) / len(people)

final_split = {key: format(value + splitted_bill, '.3f') for key, value in people.items()}

print(final_split)