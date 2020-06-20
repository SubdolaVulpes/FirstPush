# ++++++++++SMALL LIST OF CUSUMERS AGE++++++++++++

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = [32, 41, 29]
age.append(42)
all_ages = age
print(list(all_ages))
name_and_age = zip(first_names + all_ages)
ids = range(0, 4)
print(list(ids))

# Original
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
ids = range(4)

# <=============Grade List====================>

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88, 100]
subjects.append("Computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))

# print(gradebook)

full_gradebook = gradebook + last_semester_gradebook

# full_gradebook = list(zip(gradebook, last_semester_gradebook))

print(full_gradebook)


# <++++++++++++++++++==PIZZA PRICING==++++++++++++++++++>

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# settings
num_pizzas = len(toppings)
pizzas = list(zip(prices, toppings))
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
tree_cheapest = pizzas[:2]
num_two_dollar_slices = prices.count(2) 

all_prints = (num_pizzas, pizzas)
print('Background numerics: ')
print(num_two_dollar_slices)
print()

# Custumer PrintOUT
print('We sell ' +str(num_pizzas)+' different kinds of pizza!')

# <=======================Hairstyles Shop======================>

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for total_price in prices:
    print()
# Calculate the average prices $5
average_price = total_price / len(prices)
print('Average Haircut Price: ' +str(average_price))
# Carly wants to make discounts for all on $5
new_prices = [ cut_prices-5 for cut_prices in prices]
print('Cheaper prices: ' +str(new_prices))

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue: '+str(total_revenue))

average_daily_revenue = (total_revenue/7)
print('Revenue for a week: ' +str(average_daily_revenue))

# list of cuts that under 30
cuts_under_30 = [hairstyles for i in range(len(new_prices)) if new_prices[i] < 30]
print('lsit under $30:')
print(cuts_under_30)
