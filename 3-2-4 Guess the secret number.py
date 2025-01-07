secret_number = 777

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guessed_num = int(input("Enter value to compare: "))

while secret_number != guessed_num:
    print("\nHa ha! You're stuck in my loop!")
    guessed_num = int(input("\nEnter value to compare: "))
print("\nWell done, muggle! You are free now.")
