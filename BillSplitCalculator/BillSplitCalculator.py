print("Bill Split Calculator")

bill_amount = float(input('Enter the bill amount in $: '))
tip_percentage = float(input('Enter the tip percentage in $: '))
number_of_people = int(input('Enter the number of people: '))

tip_amount = (tip_percentage / 100) * bill_amount

total_amount = tip_amount + bill_amount
amount_per_person = total_amount / number_of_people

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${amount_per_person}")