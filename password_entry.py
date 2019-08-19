"""
Jesseta Thach
"""

min_password_length = 6


def main():
    password = input("Enter your password: ")
    while len(password) < min_password_length:
        print("Invalid password...")
        password = input("Enter your password: ")
    print('*' * len(password))


def valid_password(password):
    if len(password) < min_password_length:
        return False


main()
