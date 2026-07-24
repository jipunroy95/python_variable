# Basic Multiple Assignment
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Same Value to Multiple Variables
a = b = c = 100

print(a)
print(b)
print(c)

# Unpacking a Collection
# লিস্ট বা টাপল থেকে একসাথে ভ্যালু বের করা যায়।
# List

numbers = [10, 20, 30]

x, y, z = numbers

print(x)
print(y)
print(z)

# Tuple
person = ("Rahim", 25, "Dhaka")

name, age, city = person

print(name)
print(age)
print(city)

# Using * (Star Expression) যখন ভ্যালুর সংখ্যা বেশি থাকে।
numbers = [10, 20, 30, 40, 50]

a, *b = numbers

print(a)
print(b)

# More Example
numbers = [10, 20, 30, 40, 50]

*a, b = numbers

print(a)
print(b)

# Midile
numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers

print(a)
print(b)
print(c)

# Swapping Variables
x = 10
y = 20

x, y = y, x

print(x)
print(y)


# Ignore Values Using _
person = ("Rahim", 25, "Dhaka")

name, _, city = person

print(name)
print(city)

# Nested Unpacking
data = ("Rahim", (25, "Dhaka"))

name, (age, city) = data

print(name)
print(age)
print(city)

# Multiple Assignment with Function Return


def calculate():
    return 10, 20


a, b = calculate()  # fnction call

print(a, b)

# Advanced Example
student = ("Rahim", 22, "Dhaka", "Python", "AI", "ML")

name, age, city, *skills = student

print(name)
print(age)
print(city)
print(skills)

# Basic Example


def student():
    name = "Rahim"   # Local Variable
    print(name)


student()

# দুটি Function-এর Local Variable


def first():
    x = 10
    print(x)


def second():
    x = 20
    print(x)


first()
second()

# Global Variable in Python
name = "Rahim"   # Global Variable


def student():
    print(name)


student()

# Local এবং Global Variable
name = "Karim"    # Global Variable


def student():
    name = "Rahim"   # Local Variable
    print(name)


student()
print(name)

# Global Variable পরিবর্তন করতে চাইলে
count = 10


def update():
    global count
    count = 20


update()

print(count)

total = 0


def add():
    global total
    total += 2


add()
add()
add()

print(total)

# ছোট Quiz 😊
count = 5


def test():
    global count
    count += 10


test()
test()
print(count)
