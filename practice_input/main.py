name = input("Enter your name: ")
age = int(input("Enter ur age: "))

print("Hello,", name + "!")
print(f"{name} is {age} years old.")
print("Next year you will be", age + 1)

a = 10
b = 15
print(a + b)  # 25
print(a / b)
print(a // b)

age = input("Enter your age: ")
age_num = int(age)
print(age_num + 5)

i = 0
for i in range(5):      # 0,1,2,3,4
    print("repeat 5 times")

for i in range(1, 6):       # from 1 to 5
    print(i)

count = 0
while count < (5):
    print("not 5 yet!")
    count += 1  # increase by 1, otherwise it will be infinite

def say_hello():        #new local comand
    print("bull")

def add_numbers(x, y):      #parameters x and y 1 usage
    result = x+ y
    return result



