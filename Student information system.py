import csv
import matplotlib.pyplot as plt

students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    students[roll] = {"name": name, "marks": {}}
    print("Student added successfully.")

def update_marks():
    roll = input("Enter roll number: ")
    if roll in students:
        subject = input("Enter subject: ")
        marks = float(input("Enter marks: "))
        students[roll]["marks"][subject] = marks
        print("Marks updated.")
    else:
        print("Student not found.")

def calculate_grade(percentage):
    if percentage >= 90: return 'A'
    elif percentage >= 75: return 'B'
    elif percentage >= 60: return 'C'
    elif percentage >= 50: return 'D'
    else: return 'F'

def view_summary():
    for roll, data in students.items():
        print(f"\nRoll No: {roll}, Name: {data['name']}")
        total = sum(data['marks'].values())
        count = len(data['marks'])
        if count == 0:
            print("No marks available.")
            continue
        percentage = total / count
        grade = calculate_grade(percentage)
        print(f"Average: {percentage:.2f}%, Grade: {grade}")

def visualize_data():
    names = []
    averages = []
    for data in students.values():
        if data['marks']:
            avg = sum(data['marks'].values()) / len(data['marks'])
            names.append(data['name'])
            averages.append(avg)
    plt.bar(names, averages)
    plt.ylabel('Average Marks')
    plt.title('Student Performance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def find_topper():
    topper = None
    top_avg = 0
    for roll, data in students.items():
        if data['marks']:
            avg = sum(data['marks'].values()) / len(data['marks'])
            if avg > top_avg:
                top_avg = avg
                topper = data['name']
    if topper:
        print(f"Class Topper: {topper} with average {top_avg:.2f}%")

def calculate_gpa():
    roll = input("Enter roll number: ")
    if roll in students:
        grades = []
        for subject, mark in students[roll]["marks"].items():
            grade = calculate_grade(mark)
            grades.append(grade)
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        gpa = sum([grade_points[g] for g in grades]) / len(grades) if grades else 0
        print(f"GPA for {students[roll]['name']}: {gpa:.2f}")
    else:
        print("Student not found.")

def export_csv(filename='students.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for roll, data in students.items():
            for subject, mark in data['marks'].items():
                writer.writerow([roll, data['name'], subject, mark])
    print("Exported to CSV.")

def import_csv(filename='students.csv'):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                roll, name, subject, mark = row
                if roll not in students:
                    students[roll] = {'name': name, 'marks': {}}
                students[roll]['marks'][subject] = float(mark)
        print("Imported from CSV.")
    except FileNotFoundError:
        print("CSV file not found.")

def menu():
    while True:
        print("\n1. Add Student\n2. Update Marks\n3. View Summary\n4. Show Chart\n5. Calculate GPA\n6. Find Topper\n7. Import CSV\n8. Export CSV\n9. Exit")
        choice = input("Choose option: ")
        if choice == '1': add_student()
        elif choice == '2': update_marks()
        elif choice == '3': view_summary()
        elif choice == '4': visualize_data()
        elif choice == '5': calculate_gpa()
        elif choice == '6': find_topper()
        elif choice == '7': import_csv()
        elif choice == '8': export_csv()
        elif choice == '9': break
        else: print("Invalid choice.")

menu()


