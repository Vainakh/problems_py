Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 365 * 24 * 60 * 60
31536000
>>> * 100
SyntaxError: can't use starred expression here
>>> 31536000 * 80
2522880000
>>> cleat
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cleat
NameError: name 'cleat' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cls()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cls()
NameError: name 'cls' is not defined
>>> def cls()
SyntaxError: invalid syntax
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
5
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
157680000
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
157680000
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
157680000
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
157680000
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
You have lived for 157680000 seconds.
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
You have lived for 157680000 seconds.This corresponds to5years
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
You have lived for 157680000 seconds. This corresponds to5 years
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
You have lived for 157680000 seconds. This corresponds to 5 years
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
Enter your age: 5
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
Enter your age: 5
You have lived for 157680000 seconds. This corresponds to 5 years
>>> 
=============================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ===============================
Enter your age: 10
You have lived for 315360000 seconds. This corresponds to 10 years
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 5
You have lived for 157680000 seconds.
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 7
You have lived for 220752000 seconds.
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 6
Traceback (most recent call last):
  File "/Users/adlanyandarbiev/Desktop/print.py", line 2, in <module>
    print("You have lived for {} seconds. This corresponds to {} years".format(int(age) * 365 * 24 * 60 * 60), age)
IndexError: Replacement index 1 out of range for positional args tuple
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 5
Traceback (most recent call last):
  File "/Users/adlanyandarbiev/Desktop/print.py", line 2, in <module>
    print("You have lived for {} seconds. This corresponds to {} years.".format(int(age) * 365 * 24 * 60 * 60), age)
IndexError: Replacement index 1 out of range for positional args tuple
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 5
You have lived for 157680000 seconds. This corresponds to 5 years.
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Enter your age: 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================

======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
>>> len(numbers)
10
>>> for number in numbers:
	print(number)

	
0
1
2
3
4
5
6
7
8
9
>>> for number in numbers:
	print(number * 2)

	
0
2
4
6
8
10
12
14
16
18
>>> got number in numbers:
	
SyntaxError: invalid syntax
>>> gor number in numbers:
	
SyntaxError: invalid syntax
>>> for number in numbers:
	print(number ** 2)

	
0
1
4
9
16
25
36
49
64
81
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> greater_than_three = 5 > 3
>>> greater_than_three
True
>>> for number in numbers
SyntaxError: invalid syntax
>>> for number in numbers:
	print(number > 5)

	
False
False
False
False
False
False
True
True
True
True
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Please, enter a number between 0 and 9: 4
You got the number wrong!
>>> 2
2
>>> 3
3
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Please, enter a number between 0 and 9: 3
You got the number wrong!
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Please, enter a number between 0 and 9: 3
You got the number right
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Please, enter a number between 0 and 9: 2
You got the number wrong!
Please, enter a number between 0 and 9: 3
You got the number right
Please, enter a number between 0 and 9: 6
You got the number right
>>> 2
2
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
Traceback (most recent call last):
  File "/Users/adlanyandarbiev/Desktop/print.py", line 4, in <module>
    print("This is attempt {}".format(attempt))
NameError: name 'attempt' is not defined
>>> 
======================== RESTART: /Users/adlanyandarbiev/Desktop/print.py ========================
This is attempt 0
Please, enter a number between 0 and 9: 3
You got the number right
This is attempt 1
Please, enter a number between 0 and 9: 
Traceback (most recent call last):
  File "/Users/adlanyandarbiev/Desktop/print.py", line 6, in <module>
    user_number = int(input("Please, enter a number between 0 and 9: "))
ValueError: invalid literal for int() with base 10: ''
>>> import random
>>> 
=============== RESTART: /Users/adlanyandarbiev/Desktop/python/_02_random_integers.py ==============
This is attempt 0
Please, enter a number between 0 and 9: 
Traceback (most recent call last):
  File "/Users/adlanyandarbiev/Desktop/python/_02_random_integers.py", line 8, in <module>
    user_number = int(input("Please, enter a number between 0 and 9: "))
ValueError: invalid literal for int() with base 10: ''
>>> import random
>>> random.randint(0, 9)
3
>>> 
=============== RESTART: /Users/adlanyandarbiev/Desktop/python/_02_random_integers.py ==============
This is attempt 0
Please, enter a number between 0 and 9: 3
You got the number wrong!
This is attempt 1
Please, enter a number between 0 and 9: 2
You got the number right
This is attempt 2
Please, enter a number between 0 and 9: 3
You got the number wrong!
>>> minimum = 100
>>> for index in range(10):
	random_number = random.randint(0, 100)
	print("The number generated is {}".format(random_number))
	if random_number <= minimum:
		minimum = random_number

		
The number generated is 99
The number generated is 19
The number generated is 52
The number generated is 61
The number generated is 6
The number generated is 23
The number generated is 63
The number generated is 4
The number generated is 20
The number generated is 90
>>> print(minimum)
4
>>> 
========================================= RESTART: Shell ========================================
>>> python3 _02_random_integers.py
SyntaxError: invalid syntax
>>> 
SyntaxError: invalid character in identifier
>>> ask_user_and_check_number()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ask_user_and_check_number()
NameError: name 'ask_user_and_check_number' is not defined
>>> 
========================================= RESTART: Shell ========================================
>>> 
==================== RESTART: /Users/adlanyandarbiev/Desktop/python/first.py ====================
5
>>> 
==================== RESTART: /Users/adlanyandarbiev/Desktop/python/first.py ====================
this is an attempt 0
Enter a number between 0 and 9:4
You got the number wrong
this is an attempt 1
Enter a number between 0 and 9:2
You got the number right
this is an attempt 2
Enter a number between 0 and 9:5
You got the number wrong
>>> 
=========== RESTART: /Users/adlanyandarbiev/Desktop/python/_03_run_programm_x_times.py ==========
this is an attempt 0
Enter a number between 0 and 9:1
You got the number wrong
>>> 
=========== RESTART: /Users/adlanyandarbiev/Desktop/python/_03_run_programm_x_times.py ==========
this is an attempt 0
Enter a number between 0 and 9:2
You got the number right
this is an attempt 1
Enter a number between 0 and 9:3
You got the number wrong
>>> 
=========== RESTART: /Users/adlanyandarbiev/Desktop/python/_03_run_programm_x_times.py ==========
Enter the number of attempts: 2
this is an attempt 0
Enter a number between 0 and 9:1
You got the number wrong
this is an attempt 1
Enter a number between 0 and 9:1
You got the number wrong
>>> 