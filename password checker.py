import string


def check_password(password):
    if len(password) <8:
         return False
    upcase =any(char.isupper() for char in password)
    lowcase =any(char.islower() for char in password)
    digitcase =any(char.isdigit() for char in password)
    specialkey =any( char not in string.ascii_letters  + string.digits for char in password)
    if not all([upcase,lowcase,digitcase,specialkey]):
         return False
    return True
    

password = input("Enter your password: ")
if check_password(password):
     print('password is strong')
else:
     print('password is weak')


