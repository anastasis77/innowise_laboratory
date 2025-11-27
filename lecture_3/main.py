students = [] # List of dictionaries:  [{"name": :"Alice", "grades": [95, 88, ...]}, ...]

def print_menu():
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    if any(s["name"].lower() == name.lower()
for s in students):
        print(f"Student '{name}' already exists!")
        return
    students.append({"name": name, "grades": []})
    print(f"Student '{name}' added successfully!")


def add_grades():
    if not students:
        print("No students found. Add a student first.")
        return

    name = input("Enter student name: ").strip()
    student = next((s for s in students if s["name"].lower() == name.lower()), None)
    if not student:
        print(f"Student '{name} not found.")
        return

    print(f"Enter grades for {student['name']} (0-100). Type 'done' to finish:")
    while True:
        raw = input("Enter a grade (or 'done' to finish): ").strip()
        if raw.lower() == "done":
            break
        try:
            grade = int(raw)
            if 0 <= grade <= 100:

                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else None


def show_report():
    if not students:
        print("No students in the system.")
        return

    print("/n--- Student Report ---")
    valid_averages = []

    for student in students:
        avg = calculate_average(student["grades"])
        if avg is None:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            valid_averages.append(avg)

    if valid_averages:
        print("--------------------------------------")
        print(f"Max Average: {max(valid_averages):.1f}")
        print(f"Min Average: {min(valid_averages):.1f}")
        print(f"Overall Average: {sum(valid_averages) / len(valid_averages):.1f}")

def find_top_performer():
    with_grades = [s for s in students if s["grades"]]
    if not students:
        print("No students in the system.")
    elif not with_grades:
        print("No students have grades yet.")
    else: #we filter only those who have grades
        top = max(with_grades, key=lambda s: calculate_average(s["grades"]))
        avg = calculate_average(top["grades"])
        print(f"The student with the highest average is {top['name']} "
              f"with a grade of {avg:.1f}.")

def main():
    while True:
        try:
            print_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                add_grades()
            elif choice == "3":
                show_report()
            elif choice == "4":
                find_top_performer()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("\nExiting program.")
            break

if __name__ == "__main__":
    main()
