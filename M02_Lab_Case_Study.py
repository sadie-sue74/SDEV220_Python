# Carly Grubbs
# M02_Lab_Case_Study.py

# This code will ask for a student's last and first name
# If the user wants to stop, ask to enter in ZZZ to stop
# Then it will ask for the student's GPA to determine if they are on the Dean's List or the Honor Roll

# Letting the user know what the code will do
print("This program will ask for the student's last and first name.")
print("Then it will ask for their GPA to determine if they are on the Dean's list or the Honor Roll.")
print("To quit please enter in ZZZ.")
print()

# Setting up the lists to get the student's names and GPAs

while True:
    stud_last_name = input("Please enter the student's last name: ").strip() # The .strip() will remove the leading and ending spaces

    if stud_last_name in ("ZZZ", "zzz"): # Checking to see if the student last name variable equals ZZZ or zzz
        break

    stud_first_name = input("Please enter the student's first name: ").strip() # The .strip() will remove the leading and ending spaces
    gpa = float(input("Enter the student's GPA: ")) # Asks for the GPA and sets it as a float
    
    # This will check the GPA that was entered to determine the student's recognition
    if gpa >= 3.5:
        print(f"{stud_first_name} {stud_last_name} made the Dean's List")
    elif gpa >= 3.25:
        print(f"{stud_first_name} {stud_last_name} made the Honor Roll")
    else:
        print(f"{stud_first_name} {stud_last_name} did not make neither the Dean's List or Honor Roll")