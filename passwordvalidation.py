import re


def password_check():
    while True:
        password = input('Enter Your Password')
        error = False
        if len(password) <= 8:
            print('Password must be at least 8 character')
            error = True
        elif len(password) >= 12:
            print('Password must be less than 12 character')
            error = True
        if re.search('[A-Z]', password) is None:
            print('Password must be at least One Capital Latter')
            error = True
        if re.search('[a-z]', password) is None:
            print('Password must be at least one small later')
            error = True
        if re.search('[0-9]', password) is None:
            print('Password must be at least  one number')
            error = True
        if re.search('[^A-Za-z0-9, ]', password) is None:
            print('Password must be at least one Spacial Character')
            error = True
        if re.search(' ', password):
            print('Password must be remove Your space')
            error = True
        if not error:
            print('Password is Successfully')
            break
password_check()
