total = 0

# Keep reading until the user enters a blank line
while True:
    try:
        # Try and convert the line to a number
        input_value = input("Enter a number (or press Enter to finish): ")
        
        # If the user enters a blank line, exit the loop
        if input_value == "":
            break
        
        # Convert the input to a float
        number = float(input_value)
        
        # Add it to the total and display the current sum
        total += number
        print("Current sum:", total)

    except ValueError:
        # Display an error message before going on to read the next value
        print("Invalid input. Please enter a valid number.")

# Display the total
print("Final sum:", total)
