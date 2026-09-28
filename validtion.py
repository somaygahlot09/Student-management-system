def get_age():
    while True:
        try:
            age = input("Enter Age: ").strip()
            if age.isdigit() and 3 <= int(age) <= 18:
                return age
            print("Enter valid age between 3 and 18!")
        except Exception as e:
            print(f"Error: {e}")

def get_mobile():
    while True:
        try:
            mobile = input("Enter Mobile Number: ").strip()
            if mobile.isdigit() and len(mobile) == 10:
                return mobile
            print("Enter a valid 10-digit mobile number!")
        except Exception as e:
            print(f"Error: {e}")

def get_gender():
    while True:
        try:
            gender = input("Enter Gender (M/F): ").strip().upper()
            if gender in ["M", "F"]:
                return gender
            print("Enter M or F only!")
        except Exception as e:
            print(f"Error: {e}")

def get_class():
    while True:
        try:
            student_class = input("Enter Class (1-12): ").strip()
            if student_class.isdigit() and 1 <= int(student_class) <= 12:
                return student_class
            print("Enter a valid class between 1 and 12!")
        except Exception as e:
            print(f"Error: {e}")

def get_section():
    while True:
        try:
            section = input("Enter Section (A-Z): ").strip().upper()
            if len(section) == 1 and section.isalpha():
                return section
            print("Enter a valid single letter section (A-Z)!")
        except Exception as e:
            print(f"Error: {e}")

def get_address():
    try:
        return input("Enter Address: ").strip()
    except Exception as e:
        print(f"Error: {e}")
        return ""