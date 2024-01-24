import random
alphabeth = ''

small_letters = True
caps_lock = True
numbers = True
accented_letters = True
special_characters = True


if small_letters:
    alphabeth += """abcdefghijklmnopqrstuvwxyz"""
if caps_lock:
    alphabeth += """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
if numbers:
    alphabeth += '01'#"""0123456789"""
if accented_letters:
    alphabeth += """àáãäâÀÁÃÄÂèéêëÈÉÊËìíîïÌÍÎÏòóõôöÒÓÕÔÖùúûüÙÚÛÜ"""
if special_characters:
    alphabeth += """!@#$%&*()-_=+<>"""


rand_len = 8#random.randint(128, 256)
password = []
for idx in range(rand_len):
    password.append(random.choice(alphabeth))
print(''.join(password))

bits = []
for char in password:
    bits.extend([bit for bit in format(ord(char), '08b')])
    bits.append(' ')

print(''.join(bits))