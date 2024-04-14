import random
import string

def generate_password(quantity_letters, quantity_digits, quantity_punctuation):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = '!@?#%'
    
    quantity_letters = ''.join(random.choice(letters) for _ in range(quantity_letters))
    quantity_digits = ''.join(random.choice(digits) for _ in range(quantity_digits))
    quantity_punctuation = ''.join(random.choice(punctuation) for _ in range(quantity_punctuation))
    
    password = quantity_letters + quantity_digits + quantity_punctuation
    
    return password

def shuffle_password(password):
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print(f"Password shuffled: {password}")
    return password

def write_password_to_file(password): # Write the password to a file
    file_path = "password.txt"
    with open(file_path, 'w') as file:
        file.write(password)
    return file_path

def main():    
    quantity_letters = int(input("Enter the quantity of letters: "))
    quantity_digits = int(input("Enter the quantity of digits: "))
    quantity_punctuation = int(input("Enter the quantity of punctuation: "))
    
    password_generated = generate_password(quantity_letters, quantity_digits, quantity_punctuation)
    password_shuffled = shuffle_password(password_generated)
    
    password_file = write_password_to_file(password_shuffled)
    
    print(f"Password sent to file: {password_file}")
    
if __name__ == "__main__":
    main()
