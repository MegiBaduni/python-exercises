# Ecercise 3
def isInteger(s):
    # Remove whitespace from the beginning and end of the string
    s = s.strip()
    
    # Determine if the remaining characters form a valid integer
    if s and (s[0] in ['+', '-'] or s.isdigit()):
        return True
    else:
        return False

# Demonstrate the isInteger function
def main():
    # Read a string from the user
    user_input = input("Enter a string: ")

    # Check if the string represents an integer
    if isInteger(user_input):
        print("The string represents a valid integer.")
    else:
        print("The string does not represent a valid integer.")

# Call the main function if the file has been imported (or not)
if __name__ == "__main__":
    main()