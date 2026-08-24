# Pattern Generator & Number Analyzer

## 📌 Project Overview

**Pattern Generator & Number Analyzer** is a simple Python console-based project that demonstrates the use of **loops, nested loops, conditional statements, `range()`, functions, and user input**.

The program provides two main features:

1. Generate a **right-angled triangle pattern**
2. Analyze a **range of numbers**

The user can select an option from the menu and interact with the program through the terminal.

---

## 🎯 Objectives

* Practice Python **functions**
* Understand **`for` and `while` loops**
* Demonstrate **nested loops**
* Use conditional statements such as `if`, `elif`, and `else`
* Work with the Python **`range()` function**
* Perform basic numerical calculations
* Handle invalid user input using `try-except`
* Create a simple menu-driven Python application

---

## ✨ Features

### 1. Generate Right-Angled Triangle

The program asks the user to enter the number of rows and generates a right-angled triangle using nested `for` loops.

Example for 5 rows:

```text
*
* *
* * *
* * * *
* * * * *
```

The outer loop controls the rows, while the inner loop controls the number of stars printed in each row.

---

### 2. Analyze a Range of Numbers

The user enters a starting number and an ending number.

The program calculates:

* Number of values in the range
* Sum of the numbers
* Number of even values
* Number of odd values
* Average of the numbers
* Displays all numbers in the range

The program uses `range(start, end + 1)` so that the ending number is included.

### Example

For the range **56 to 66**:

```text
Numbers in range: 11
Sum: 671
Even numbers: 6
Odd numbers: 5
Average: 61.0

Numbers:
56 57 58 59 60 61 62 63 64 65 66
```

---

## 🛠️ Technologies Used

* **Python 3**
* `input()`
* `print()`
* `for` loop
* `while` loop
* Nested loops
* `if / elif / else`
* `range()`
* `try-except`
* Functions

---

## 📂 Project Structure

```text
Pattern Generator & Number Analyzer/
│
├── r2(2).py
└── README.md
```

---

## 🔄 Program Menu

When the program starts, it displays:

```text
========================================
        PATTERN & NUMBER ANALYZER
========================================

1. Generate Right-Angled Triangle
2. Analyze a Range of Numbers
3. Exit
```

The menu is controlled using a `while` loop, allowing the user to perform multiple operations until the **Exit** option is selected.

---

## ⚙️ How the Program Works

### Step 1: Start the Program

Run the Python file:

```bash
python "r2(2).py"
```

### Step 2: Select an Option

Enter:

```text
1
```

to generate a triangle,

```text
2
```

to analyze a number range, or

```text
3
```

to exit.

### Step 3: Generate a Pattern

Enter a positive number of rows.

The program uses nested loops to print the required number of stars.

### Step 4: Analyze Numbers

Enter the start and end numbers.

The program checks each number, calculates the total, and determines whether each number is even or odd.

---

## 🧠 Python Concepts Demonstrated

### Functions

The project separates tasks into functions:

```python
def right_angled_triangle():
```

and

```python
def number_analyzer():
```

This makes the program easier to understand and maintain.

### Nested Loops

The triangle uses one loop inside another loop:

```python
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
```

This controls both the number of rows and stars per row.

### Conditional Statements

The number analyzer checks whether a number is even:

```python
if number % 2 == 0:
```

Otherwise, it counts the number as odd.

### Error Handling

`try-except` is used to handle invalid integer input and prevent the program from crashing.

---

## 🚨 Input Validation

The program checks for invalid input.

For example:

```text
Invalid row count! Please enter a positive number.
```

It also checks whether the starting number is greater than the ending number:

```text
Invalid range! Start must be less than or equal to end.
```

Invalid menu choices are also handled:

```text
Invalid choice! Please select 1-3.
```

---

## 📊 Sample Output

### Triangle

```text
Enter your choice: 1
Enter the number of rows: 5

Right-Angled Triangle:
*
* *
* * *
* * * *
* * * * *
```

### Number Analysis

```text
Enter your choice: 2
Enter the start number: 56
Enter the end number: 66

Number Analysis
------------------------------

Numbers in range: 11
Sum: 671
Even numbers: 6
Odd numbers: 5
Average: 61.0

Numbers:
56 57 58 59 60 61 62 63 64 65 66
```

### Exit

```text
Enter your choice: 3
Thank you for using the program!good bye
```

---

## 📈 Possible Future Improvements

The project could be extended by adding:

* More pattern types such as inverted triangles and pyramids
* Prime-number detection
* Maximum and minimum number calculation
* Separate even and odd number lists
* Better input validation
* A graphical user interface
* Saving analysis results to a file
* More mathematical analysis features

---

## 👨‍💻 Author

**Pattern Generator & Number Analyzer**

A beginner-friendly Python project created to practice fundamental programming concepts, loops, functions, conditions, and numerical analysis.

---

## 📄 License

This project is intended for **educational and learning purposes**.
