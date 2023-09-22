#  Password stars

"""
get user password
display *
"""
password = input('Password: ')
for password in range(len(password)):
    print('*', end='')
