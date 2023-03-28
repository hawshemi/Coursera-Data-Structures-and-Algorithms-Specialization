def guess_number(n):
    # Initialize the range of possible numbers.
    questions = 21

    low = 1
    high = n
    print("")
    print("Answer with 'less' or 'more'.\n")
    # Perform binary search until the number is found.
    for i in range(questions):
        # Compute the midpoint of the range.
        mid = (low + high) // 2

        # Ask the question.
        print(f"Is it: {mid} ?")

        # Get the answer and update the range.
        answer = input()
        if answer == "yes":
            return mid
        elif answer == "less":
            high = mid - 1
        elif answer == "more":
            low = mid + 1

    # If the number isn't found after 7 questions, return -1.
    return -1

# Test the function.
print(guess_number(2097151))
