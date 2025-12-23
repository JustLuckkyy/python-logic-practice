"""
Filename: logic_challenges.py
Author: LuckyChoudhary
Date: December 2025
Description: A collection of Python logic challenges and algorithm practices
             completed as part of pre-internship technical training.
"""


# ==========================================
# 1. BASIC CONDITIONALS (Age & Eligibility)
# ==========================================

user_input = int(input("Enter your age: "))

if user_input > 18:
    print("you can watch the movie")
else:
     input_2 = (input("do you have any adult with you: "))
     if input_2 == "yes" :
         print("you can watch the movie")

     else:
         print("sorry!! you can watch the movie.")

######################################################################################

# ==========================================
# 2. MATHEMATICAL LOGIC (Even/Odd & Prime)
# ==========================================
# --- Even or Odd ---

num = int(input("give the number:"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

######################################################################################

# ==========================================
# 3. LOOPING & STRING MANIPULATION
# ==========================================
# --- String Filtering (Words <= 3 chars) ---

string = "are low fine can to learn fight earn no like two moo fly"
slpit_wrd = (string.split())

for i in slpit_wrd:
    if len(i)<=3:
        print(i)


######################################################################################


# ==========================================
# 4. STRING-DRIVEN PATTERN GENERATION
# ==========================================
# Purpose: Uses a string length to control the number of rows in a triangle.

star = "*"
count = 1
# We give it a string with 5 characters so it runs 5 times
for i in "12345":
    if count <= 5:
        print(star * count)
        count = count + 1



###################################################################################33


# ==========================================
# 5. --- FizzBuzz (1 to 50) ---
# ==========================================

num= 1
count = 0
for i in range(0,101):
    count = count +i
    print(count)
count = 0
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        count = count + i
        print(i)
        print(count)

    elif i%3==0:
        print("fizz")
        count = count + i
        print(i)

    elif i%5==0:
        print("buzz")
        count = count + i
        print(i)

    else:
        print(i)

#################################################################################

#==========================================
#6. STRING PARSING & MEMBERSHIP TESTING
#==========================================
#Purpose: Scans a string to count specific characters (vowels).
#Demonstrates: String iteration and the 'in' keyword for membership checking.

sentence = "Python is amazing"
vowels = "aeiouAEIOU"  # We include both cases so we don't miss anything
count = 0

# The loop treats the string like a list of letters
for char in sentence:
    # This is the 'Membership Check'
    if char in vowels:
        count = count + 1
        print(f"Found a vowel: {char}")

print("--------------------------")
print(f"Total vowels found: {count}")


################################################################################

# ==========================================
# 7. FIBONACCI SEQUENCE OR PATTERN
# ==========================================
# --- Fibonacci Sequence (10 terms) --------

a = 0
b = 1
print(a ,b , end=" ")
for i in range(8):
    next_term = a + b
    print(next_term, end=" ")
    # a,b = b, next_term      #optional to use .
    a = b
    b = next_term


###############################################################################


# ==========================================
# 8. --- Factorial Calculator ---
# ==========================================

n = 5
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i
    print(factorial)


############################################################################


#==========================================
#9. OPTIMIZED ALGORITHM: PRIME NUMBER CHECK
#==========================================
#Purpose: Determines if a number is prime using the Square Root method.
#Efficiency: O(sqrt(n)) - This is much faster than checking every number up to n.

n = 25
prime = True

for i in range(2,int(n ** 0.5+1)):
    if n % i ==0:
        prime = False
        break
if prime and n>1:
    print("is prime")
else:
    print("not prime")


#####################################################################################


#==========================================
#10. DATA STRUCTURES (Dictionary Counter)
#==========================================
word = "programming"
dict = {}

for i in word:
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1
    print(f"{i}: {dict[i]}")


#############################################################################






