# The commented code should work but the test doesn't like it

# user_input = int(input())
# if user_input < 0:
#     print(user_input * -1, "\nThe number is positive")
# else:
#     print(user_input * -1, "\nThe number is negative")

user_input = int(input())
print(user_input * -1)
if user_input < 0:
    print("The number is positive")
else:
    print("The number is negative")
