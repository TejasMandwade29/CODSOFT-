import random
import string

def Generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level ('low', 'medium', or 'high'): ").lower()
    
    password = Generate_password(length, complexity)
    print("Your Password Is :", password)

if __name__ == "__main__":
    main()