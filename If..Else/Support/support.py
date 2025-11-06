# asking the user to enter his or her age, income and the address.
# default support = 100$
# support will be increased to 200 if age > 70 and address = 'Beirut'
# support will be increased to 150$ if age between 50 and 69 and the income < 1000$

age = int(input('Enter your age'))
income = float(input('Enter your income'))
address = input('Enter your address').capitalize().strip()

support = 100

if age > 70 and address == 'Beirut':
  support = 200
elif age >= 50 and age <= 69 and income < 1000:
  support = 150
elif age > 70 and (address != 'Saida') and (address != 'Beirut'):
  support = 50
else:
  support = 100

print(f"Your support is {support}$")
