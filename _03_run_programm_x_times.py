import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9:"))
    if user_number in magic_numbers:
        return "You got the number right"
    if user_number not in magic_numbers:
        return "You got the number wrong"

def run_program_x_times(chances):
    for attempt in range(chances):
        print("this is an attempt {}".format(attempt))
        message = ask_user_and_check_number()
        print(message)

user_attempts = int(input("Enter the number of attempts: "))

run_program_x_times(user_attempts)
