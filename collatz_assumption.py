# Collatz Conjecture, often misspelled as "Collatze," is a famous unsolved problem in mathematics. 
# It is also known as the 3n + 1 conjecture, Ulam conjecture, Kakutani's problem, Thwaites conjecture, Hasse's algorithm, or the Syracuse problem.

# The conjecture can be summarized as follows:
# 1. Take any positive integer n.
# 2. If n is even, divide it by 2 to get n / 2.
# 3. If n is odd, multiply it by 3 and add 1 to get 3n + 1.
# 4. Repeat the process indefinitely.

# The conjecture asserts that no matter which positive integer you start with, you will eventually reach the number 1.

# After reaching 1, the process will continue to cycle through the sequence 4, 2, 1 indefinitely. 
# Despite extensive numerical testing, no counterexample has been found, which supports the conjecture's truth. 
# However, it remains unproven, and proving or disproving it is a significant open question in mathematics.

def collatz_steps(number):
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        steps += 1
    return steps

while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
steps = collatz_steps(number)
print(f"The number {number} reaches 1 according to the Collatz conjecture in {steps} steps.")
