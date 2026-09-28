
import os
import csv
from validtion import get_age, get_mobile, get_gender, get_class, get_section, get_address

STUDENTS_FILE = "students.csv"
FIELDS = ["ID", "Name", "Age", "Class", "Section", "Mobile", "Address", "Gender"]


def _generate_id():
    try:
        if not os.path.exists(STUDENTS_FILE):
            return 1
        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                return 1
            return max(int(row["ID"]) for row in rows) + 1
    except Exception:
        return 1


def add_student():
    try:
        name = input("Enter Student Name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        # Duplicate name check
        if os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["Name"].lower() == name.lower():
                        print(f"Student '{name}' already exists! (ID: {row['ID']})")
                        return

        age           = get_age()
        student_class = get_class()
        section       = get_section()
        mobile        = get_mobile()
        addr          = get_address()
        gender        = get_gender()

        if not os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(FIELDS)

        student_id = _generate_id()

        with open(STUDENTS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student_id, name, age, student_class, section, mobile, addr, gender])

        print(f"Student Added Successfully! (ID: {student_id})")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error while adding student: {e}")


def view_students():
    try:
        if not os.path.exists(STUDENTS_FILE):
            print("No student records found!")
            return

        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            print("No student records found!")
            return

        print("\n" + "-" * 95)
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Class':<7} {'Section':<9} {'Mobile':<12} {'Gender':<7} {'Address'}")
        print("-" * 95)
        for row in rows:
            print(f"{row['ID']:<5} {row['Name']:<20} {row['Age']:<5} {row['Class']:<7} {row['Section']:<9} {row['Mobile']:<12} {row['Gender']:<7} {row['Address']}")
        print("-" * 95)
        print(f"Total Students: {len(rows)}\n")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error while viewing students: {e}")


def search_student():
    try:
        if not os.path.exists(STUDENTS_FILE):
            print("No student records found!")
            return

        name  = input("Enter Student Name to search: ").strip()
        found = False

        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"].lower() == name.lower():
                    print("\n--- Student Found ---")
                    for key, value in row.items():
                        print(f"  {key}: {value}")
                    found = True

        if not found:
            print("No student found with that name!")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error while searching: {e}")


def update_student():
    try:
        if not os.path.exists(STUDENTS_FILE):
            print("No student records found!")
            return

        student_id = input("Enter Student ID to update: ").strip()
        students   = []
        updated    = False

        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["ID"] == student_id:
                    print(f"\nUpdating record for: {row['Name']}")
                    row["Name"]    = input("New Name: ").strip() or row["Name"]
                    row["Age"]     = get_age()
                    row["Class"]   = get_class()
                    row["Section"] = get_section()
                    row["Mobile"]  = get_mobile()
                    row["Address"] = get_address()
                    row["Gender"]  = get_gender()
                    updated = True
                students.append(row)

        if not updated:
            print("No student found with that ID!")
            return

        with open(STUDENTS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)

        print("Student Updated Successfully!")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error while updating: {e}")


def delete_student():
    try:
        if not os.path.exists(STUDENTS_FILE):
            print("No student records found!")
            return

        student_name = input("Enter Student Name to delete: ").strip()
        students     = []
        deleted      = False

        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"].lower() == student_name.lower():
                    deleted = True
                else:
                    students.append(row)

        if not deleted:
            print("No student found with that name!")
            return

        with open(STUDENTS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)

        print("Student Deleted Successfully!")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error while deleting: {e}")


def import_students():
    try:
        filepath = input("Enter full path of CSV file to import: ").strip()

        if not os.path.exists(filepath):
            print("File not found! Check the path and try again.")
            return

        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            incoming_fields = reader.fieldnames

            if not incoming_fields:
                print("The file is empty or has no headers!")
                return

            required = ["Name", "Age", "Class", "Section", "Mobile", "Address", "Gender"]
            missing  = [col for col in required if col not in incoming_fields]
            if missing:
                print(f"Missing columns in import file: {', '.join(missing)}")
                return

            # Create students.csv with header if not exists
            if not os.path.exists(STUDENTS_FILE):
                with open(STUDENTS_FILE, "w", newline="") as out:
                    writer = csv.writer(out)
                    writer.writerow(FIELDS)

            # Load existing names to avoid duplicates
            existing_names = set()
            with open(STUDENTS_FILE, "r") as out:
                existing_reader = csv.DictReader(out)
                for row in existing_reader:
                    existing_names.add(row["Name"].lower())

            added   = 0
            skipped = 0

            with open(STUDENTS_FILE, "a", newline="") as out:
                writer = csv.writer(out)
                for row in reader:
                    if row["Name"].lower() in existing_names:
                        print(f"  Skipped (duplicate): {row['Name']}")
                        skipped += 1
                        continue
                    student_id = _generate_id()
                    writer.writerow([
                        student_id,
                        row["Name"],
                        row["Age"],
                        row["Class"],
                        row["Section"],
                        row["Mobile"],
                        row["Address"],
                        row["Gender"]
                    ])
                    existing_names.add(row["Name"].lower())
                    added += 1

        print(f"\nImport Complete! Added: {added} | Skipped (duplicates): {skipped}")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error during import: {e}")


def export_students():
    try:
        if not os.path.exists(STUDENTS_FILE):
            print("No student records to export!")
            return

        filename = input("Enter export filename (e.g. backup.csv): ").strip()
        if not filename:
            print("Filename cannot be empty!")
            return
        if not filename.endswith(".csv"):
            filename += ".csv"

        with open(STUDENTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            rows   = list(reader)

        if not rows:
            print("No student records to export!")
            return

        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Exported {len(rows)} student(s) successfully to '{filename}'!")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error during export: {e}")