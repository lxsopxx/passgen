import random
import string
import os

def generate_nickname():
    words = ['jim', 'killah', 'kevin', 'robin', 'pythonista', 'jackson','haymaker','creat0r',
             'super','crazy','loco',]  # Add more words here
    nickname = random.choice(words)

    while len(nickname) < 6 or len(nickname) > 16:
        nickname += random.choice(words)

    return nickname

def generate_password():
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*|(()_+'
    password = ''.join(random.choice(characters) for _ in range(random.randint(10, 15)))

    # Ensure at least 2 numbers
    for _ in range(2):
        password += random.choice(string.digits)

    # Insert a symbol between two characters
    index = random.randint(1, len(password) - 1)
    symbol = random.choice('!@#$%^&*|(()_+')
    password = password[:index] + symbol + password[index:]

    return password

def validate_website(website):
    if not website or not website.strip():
        raise ValueError("Website name cannot be empty.")

def validate_email(email):
    if not email or not email.strip():
        raise ValueError("Email cannot be empty.")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")

def validate_nickname(nickname):
    if not nickname or not nickname.strip():
        raise ValueError("Nickname cannot be empty.")
    if len(nickname) < 6 or len(nickname) > 16:
        raise ValueError("Nickname must be between 6 and 16 characters.")

def validate_directory(directory):
    if not os.path.isdir(directory):
        raise ValueError("Invalid directory path. Please enter a valid directory.")

def save_data(nickname, password, website, email):
    folder_directory = "D:\\deasxas"  # Specific directory path

    if not os.path.exists(folder_directory):
        os.makedirs(folder_directory)

    file_name = f"{website.replace('.', '_')}.txt"
    file_path = os.path.join(folder_directory, file_name)

    index = 1
    while os.path.exists(file_path):
        file_name = f"{website.replace('.', '_')}_{index}.txt"
        file_path = os.path.join(folder_directory, file_name)
        index += 1

    with open(file_path, "w") as file:
        file.write(f"Website: {website}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Password: {password}\n")

        if nickname:
            file.write(f"Nickname: {nickname}\n")

    print("Data saved successfully!")

website_name = input("Enter the name of the website: ")
try:
    validate_website(website_name)

    email = input("Enter your email: ")
    try:
        validate_email(email)
    except ValueError as e:
        print("Error:", str(e))
        exit()

    nickname = generate_nickname()
    print(f"Generated Nickname for {website_name}: {nickname}")

    keep_nickname = input("Do you want to keep the generated nickname? (yes/no): ")
    if keep_nickname.lower() == "no":
        nickname = input("Enter your desired nickname: ")
        try:
            validate_nickname(nickname)
        except ValueError as e:
            print("Error:", str(e))
            exit()

    password = generate_password()
    print(f"Generated Password for {website_name}: {password}")

    save_data(nickname, password, website_name, email)
except ValueError as e:
    print("Error:", str(e))