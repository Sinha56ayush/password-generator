

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "123456789"

symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + numbers + symbols

length_for_pass = int(input("length for password: "))

password = "".join(random.sample(Use_for, length_for_pass))

print("Your generated password",password)


