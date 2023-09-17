import random
import string

# Function below is referenced from this web: 
# https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
if __name__ == "__main__": 
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    print(password);

# Success!