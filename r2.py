# Pattern Generator & Number Analyzer

def right_angled_triangle():
    """Generate a right-angled triangle using nested loops."""

    while True:
        try:
            rows = int(input("Enter the number of rows: "))

            if rows <= 0:
                print("Invalid row count! Please enter a positive number.")
                break

            print("\nRight-Angled Triangle:")

            # Nested loops
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end=" ")
                print()

            break

        except ValueError:
            print("Please enter a valid integer.")
            break


def number_analyzer():
    """Analyze numbers within a user-defined range."""

    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))

        if start > end:
            print("Invalid range! Start must be less than or equal to end.")
            return

        print("\nNumber Analysis")
        print("-" * 30)

        total = 0
        even_count = 0
        odd_count = 0

        # range() generates numbers from start to end
        for number in range(start, end + 1):

            if number == 0:
                continue

            total += number

            if number % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        count = end - start + 1

        print("Numbers in range:", count)
        print("Sum:", total)
        print("Even numbers:", even_count)
        print("Odd numbers:", odd_count)

        # Average
        if count > 0:
            average = total / count
            print("Average:", average)

        print("\nNumbers:")
        for number in range(start, end + 1):
            print(number, end=" ")

        print()

    except ValueError:
        print("Please enter valid integer values.")




    while True:
        print("    PATTERN & NUMBER ANALYZER")
        print("1. Generate Right-Angled Triangle")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            right_angled_triangle()

        elif choice == "2":
            number_analyzer()

        elif choice == "3":
            print("Thank you for using the program!good bye ")
            break

        else:
            print("Invalid choice! Please select 1-3.")


