

def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif  weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return (weight * price_per_pound) + 20 

print(ground_shipping(8.5))

drone_prem_ship = 125
# Price for premium pack

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return price_per_pound *weight
print(drone_shipping(1.4))

def print_the_cheapest_method(weight):
	
	ground = ground_shipping(weight)
	drone = drone_shipping(weight)
	premium = drone_prem_ship
	
	if ground < premium and ground < drone:
		method = "standart shipping"
		cost = ground
	elif premium < ground and premium < drone:
		method = "premium shipping"
		cost = premium
	elif drone < ground and drone < premium:
		method = "Drone shipping"
		cost = drone

	print("The cheapest option available is $%.2f with %s shipping." % (cost, method))

print_the_cheapest_method(4.1)
print_the_cheapest_method(56.3)

# <===============Determind VOTES===============>

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
num_i = letters.count('i')
print(num_i)

# <===============.SORT list===================>

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

# Sort the citys with a VALUE 
sorted_cities = sorted(cities)
print(sorted_cities)

# <=====================DOUBLE IndeX======================>

#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# <==================MIDDLE NUMBER======================>

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# <============+++++++++FOR LOOP======================>

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for adopting in dog_breeds_available_for_adoption:
  print(adopting)
  if adopting == dog_breed_I_want:
    print("They have the dog I want!")
    break
print("End of the session")

# <====================**2, **3 in the power==================>

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(single_digits)

for digits in single_digits:
  squares = []
  for digits in single_digits:
    squares.append(digits**2)
print(squares)

cubes = [ digits**3 for digits in single_digits]
print(cubes)