import os
import csv
import hashlib

USERS_FILE = "users.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    try:
        username = input("Enter Username: ").strip().lower()
        if not username:
            print("Username cannot be empty!")
            return
        password = input("Enter Password: ").strip()
        if not password:
            print("Password cannot be empty!")
            return

        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Username", "Password"])

        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Username"] == username:
                    print("Username already exists! Try a different one.")
                    return

        with open(USERS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, hash_password(password)])

        print("Registration Successful!")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error during registration: {e}")


def login():
    try:
        if not os.path.exists(USERS_FILE):
            print("No users registered yet! Please register first.")
            return False

        username = input("Enter Username: ").strip().lower()
        password = input("Enter Password: ").strip()

        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Username"] == username and row["Password"] == hash_password(password):
                    print(f"\nLogin Successful! Welcome, {username}.")
                    return True

        print("Invalid Username or Password!")
        return False

    except FileNotFoundError as e:
        print(f"File error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during login: {e}")
        return False