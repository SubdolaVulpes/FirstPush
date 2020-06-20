# BOOLEN STATMENT 

# will print <class 'str'> not expected
my_baby_bool = "true"
print(type(my_baby_bool))

# Will print <Class 'bool'> expeced
my_baby_bool_two = True
print(type(my_baby_bool_two))

#<========================================================>

# IF ELSE SATRMANT 
y = 5

def greater_than (x):
  if x == y:
    return "These numbers are the same"

print(greater_than(5))

def graduation_reqs(creadits):
  if creadits >= 120:
    return "You have enough credits to graduate!"

print(graduation_reqs(122))


# <==========================================================>
# === BOOLEN OPERATORS(and, or, not)
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

print(graduation_reqs(122, 2.5))

# <================OR===================>

statement_one1 = True

statement_two2 = True

# This way of function is more effecient  
def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
     return True

def graduation_mailer(gpa, credits):
  gpa >= 2.0 or credits >= 120
  return "You pass the credentials"
print(graduation_mailer(2.1, 123))

#<==========IF (and, not)===============>
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
  else: 
    return "I don't know what to say"

print(graduation_reqs(1.0, 119))

# <===========(elif) statement==============>

def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  elif gpa >= 0.0:
    return "F"

print(grade_converter(4.2))

# <============(try: except:)================>

def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")

def check_leap_year(year): 
  is_leap_year = False
  if year % 4 == 0:
    is_leap_year = True

try:
  check_leap_year(2018)
  print(is_leap_year) 
  # The variable is_leap_year is declared inside the function
except:
  print('Your code raised an error!')

  # (-=+++++++++++++=-)

  def applicant_selector(gpa, ps_score, ec_count):
    if gpa >= 3.0 and ps_score >= 90 and ec_count >=3:
      return "This applicant should be accepted."
    elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
      return "This applicant should be given an in-person interview."
    else:
      return "This applicant should be rejected."
  
print(applicant_selector(2.1, 50, 2))

# <=============DUBLE RETURN======================>

def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!" 
# this duble return is VERY unuguale

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# <===========LIST of DATA=================>

data_digits = [1, 4, 5, 56, 2939, 0.5, 9]

# can be store MUTIPLE DATA
multi_data = ['Arthur', 21, 'Max', 24]

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

#Multiple LIST of LIST.
ages = [['Aaron', 15], ['Dhruti', 16]]

# <===============ZIP modifyer==============>

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
# ZIP is modifying the list.
names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# <=================Two Types of print (N)======================>

list1 = range(0, 9)
print(list1)
# will print range(0, 9 )

list2 = range(0, 8)
print(list(list2))
# will print the LIST of from 0-7

list1 = range(5, 15, 3)
print(list(list1))
list2 = range(0, 40, 5)
print(list(list2))

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5 +" <!> " + last_element)

colors = ['red', 'green', 'blue', 'yellow', 'orange']

# List containing only last 2 = ['yellow', 'orange']
print(colors[-2:])

# List excluding last 2 = ['red', 'green', 'blue']
print(colors[:-2])


# <==========================Nested LOOP===============================>

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)

        # Optimized way of NESTED LOOP

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [elmnt for elmnt in heights if elmnt >= 162 ]
print(can_ride_coaster)


