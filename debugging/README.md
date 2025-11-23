# Tasks Overview

## 0. Debugging – Python Factorial
	•	File: factorial.py
	•	Objective: Fix a Python script that calculates the factorial of a number.
	•	Issue Fixed: The original while loop did not decrease n, causing an infinite loop.
	•	Solution: Added n -= 1 inside the loop.

```py
while n > 1:
    result *= n
    n -= 1
```
### Learning Points:
	•	Debugging logic errors in loops
	•	Understanding recursion and iterative approaches


## 1. Debugging – Python Arguments
	•	File: print_arguments.py
	•	Objective: Print command-line arguments without including the script name.
	•	Issue Fixed: Original code printed the script name.
	•	Solution: Start iterating from sys.argv[1:].

  ```py
for arg in sys.argv[1:]:
    print(arg)
```

### Learning Points:
	•	Handling sys.argv correctly
	•	Processing command-line input

## 2. Debugging – HTML / JavaScript
	•	File: change_background.html
	•	Objective: Correct a web page so that a button changes the background color.
	•	Issue Fixed: id of button was misspelled in HTML.
	•	Solution: Corrected id="colorButton" to match JS reference.

  ```py
<button id="colorButton">Change Color</button>
```

### Learning Points:
	•	Debugging DOM element references
	•	Working with JavaScript events


## 3. Debugging – Python Mines (Minesweeper)
	•	File: mines.py
	•	Objective: Fix Python Minesweeper code and implement a win detection mechanism.
	•	Issue Fixed: Game did not detect when all non-mine cells were revealed.
	•	Solution: Added has_won() method to check win condition.

  ```py
def has_won(self):
    for y in range(self.height):
        for x in range(self.width):
            if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                return False
    return True
```

### Learning Points:
	•	Recursive logic and board printing
	•	Detecting game win conditions


## 4. Documentation – Python Factorial
	•	File: factorial_recursive.py
	•	Objective: Add docstrings to a recursive factorial function.
	•	Docstring Example:

  ```py
def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Parameters:
    n (int): Non-negative integer

    Returns:
    int: Factorial of n
    """
```

### Learning Points:
	•	Writing professional docstrings
	•	Understanding parameters, return types, and function descriptions

## 5. Error Handling – Python Checkbook
	•	File: checkbook.py
	•	Objective: Prevent crashes on invalid user input.
	•	Issue Fixed: Program crashed when non-numeric input was entered.
	•	Solution: Added try/except blocks around input conversion.


  ```py
try:
    amount = float(input("Enter the amount: $"))
except ValueError:
    print("Invalid input. Please enter a number.")
  ```

### Learning Points:
	•	Input validation
	•	Exception handling in Python


## 6. Debugging – Tic Tac Toe Python
	•	File: tic.py
	•	Objective: Correct a Python Tic Tac Toe game.
	•	Issues Fixed:
	•	Incorrect winner announcement (printed current player instead of previous)
	•	Missing input validation for row/column numbers
	•	Solution: Adjusted player switching and added input validation.

  ```py

# Switch player after a valid move
player = "O" if player == "X" else "X"

```

### Learning Points:
	•	Turn-taking logic
	•	Input validation and error handling
	•	Checking win conditions in 2D arrays

