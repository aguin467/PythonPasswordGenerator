import string;
import secrets;


alphabet = string.ascii_letters + string.hexdigits + string.punctuation;
password = ''.join(secrets.choice(alphabet) for i in range(1000));

print(password);