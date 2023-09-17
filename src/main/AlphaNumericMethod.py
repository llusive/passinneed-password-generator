# This program will be used as one of the methods for generating an alpha-numeric password.
# The program will create random alphabets and numbers if possible.
import random
import string

class AlphaNumericMethod:
    def generate():
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        print(password);
        return password