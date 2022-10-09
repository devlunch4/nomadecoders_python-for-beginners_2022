
# RETRUN FUNCTION
from math import dist


def tax_calc(money):
    return money * 0.35


def pay_tax(tax):
    print("Thank you for paying", tax)


pay_tax(tax_calc(150000))

# MAKE JUICE START
print("## MAKE JUICE")


def make_juice(fruit):
    return f"{fruit}+🥤"


def add_ice(juice):
    return f"{juice}+🧊"


def add_suger(iced_juice):
    return f"{iced_juice}+🍬"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_suger(cold_juice)

print(juice)
print(cold_juice)
print(perfect_juice)


# IF
print("## SIMPLE IF")
a = True
if (a):
    print("a is True")
else:
    print("a is False")

a = False
if (a is not True):
    print("a is False")
else:
    print("a is True")

if (a != True):
    print("a is False")
else:
    print("a is True")

# AND
print("## SIMPLE AND")
a = True
b = False

# True and True == True
if (a and a) == True:
    print(a, "and", a)
# False and True == False
if (b and a) == False:
    print(b, "and", a)
# True and False == False
if (a and b) == False:
    print(a, "and", b)
# False and False == False
if (b and b) == False:
    print(b, "and", b)

# OR
print("## SIMPLE OR")
# True or True == True
if (a or a) == True:
    print(a, "or", a)

# True or False == True
if (a or b) == True:
    print(a, "or", b)

# False or Ture == True
if (b or a) == True:
    print(b, "or", a)

# False or False == False
if (b or b) == False:
    print(b, "or", b)

# While
print("## SIMPLE WHILE")

distance = 0
while distance < 20:
    print("I am running:", distance, "km")
    distance = distance + 1
