"""
CP1402

Get Password with minimum length
"""

"""
# Pseudo code of the 1st password creation program
get user password
for password in range(length(password))
display *
"""

# # version 1
# def version_1():
#     # 1st version of the password
#     password = input('Password: ')
#     for password in range(len(password)):
#         print('*', end='')


"""
Pseudocode:

def main:
    get password
    display *
"""
MINIMUM_LENGTH = 4


def main():
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(minimum_length):
    """Function get user input password"""
    password = input(f"Enter password with {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password to short")
        password = input("Enter password with minimum length: ")
    return password


def print_stars(sequence):
    """Function will display a number of * depending on user password"""
    print('*' * len(sequence))


main()
# get_password()
# print_asterisk()
