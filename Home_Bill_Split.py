people_ac_usage = {'zeyad': 0, 'abdelaziz': 0, 'malek': 0, 'yahia': 0, 'omar': 0} #change the names or add/remove to your preference
total_ac_cost = 0

try:
    total_electricity_bill = float(input("Enter total electricity bill: "))
    electricity_rate_per_kwh = float(input("Enter the rate of electricity per KWh: "))
    total_wifi_bill = float(input("Enter total wifi bill: "))
    total_water_bill = float(input("Enter total water bill: "))
except ValueError:
    print("Please enter a valid number!")
    exit(1)
for person, ac_usage in people_ac_usage.items():
    people_ac_usage[person] = float(input(f"How many KWh did {person}'s AC consume? ")) * electricity_rate_per_kwh
    total_ac_cost += people_ac_usage[person]

total_bill_excluding_ac = total_electricity_bill - total_ac_cost
individual_share = (total_bill_excluding_ac + total_wifi_bill + total_water_bill) / len(people_ac_usage)

final_split = {person: format(ac_cost + individual_share, '.3f') for person, ac_cost in people_ac_usage.items()}

print(final_split)