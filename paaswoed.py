import random

user_password = input("Enter your password = ")

characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
attempts = 0
guess = ""

if len(user_password) > 6:
   print("Warning: Long passwords may take a huge number of attempts!")

while guess != user_password:
    guess = ''.join(random.choice(characters) for _ in range(len(user_password)))
    attempts += 1
    if attempts % 1000000== 0:
        print(f"Attempt {attempts}: {guess}")

print(f"Password cracked in {attempts} attempts: {guess}")