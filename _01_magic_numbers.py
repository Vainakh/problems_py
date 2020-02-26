magic_numbers = [3, 6]
chances = 3
for attempt in range(chances):
    print("This is attempt {}".format(attempt))
    
    user_number = int(input("Please, enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got the number right")
    if user_number not in magic_numbers:
        print("You got the number wrong!")
          
          



