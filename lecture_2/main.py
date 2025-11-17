# 1. Define a Function for the Profile & Calculations
def generate_profile(age:int):
    if 0 <= age <= 12:
        return "Child"
    elif 13<= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Adult"

# 2. Get User Input
user_name = input("Enter your full name: ").strip()
while True:

    birth_year_str = input("Enter your birth year: ").strip()
    try:
        birth_year = int(birth_year_str)      # convert to int
        break
    except ValueError:
        print("Invalid birth year. Please enter a number.")

current_age = 2025 - birth_year                    # age

# Create an empty list for hobbies
hobbies = []

# Execution cycle
while True:
    hobby = input('Enter a favorite hobby or type "stop" to finish:').strip()
    if hobby.lower() == "stop":                    # case-insensitive
        break

    if hobby.strip():                                      # ignore blank lines
        hobbies.append(hobby)

# 3. Process and Generate the Profile
life_stage = generate_profile(current_age)         # Function current_age is called

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# 4. Display the Output
print("\n---")
print("Profile Summary")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if len(user_profile["hobbies"]) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")
print("---")