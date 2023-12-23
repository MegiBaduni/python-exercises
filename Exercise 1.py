# Function to conduct a reverse lookup on a dictionary
# Parameters:
# - data: the dictionary to perform the reverse lookup on
# - value: the value to search for in the dictionary
# Returns:
# - a list (possibly empty) of keys from data that map to value
def reverseLookup(data, value):
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys

# Demonstrate the reverseLookup function
def main():
    # A dictionary mapping 4 French words to their English equivalents
    french_to_english = {
        'le': 'the',
        'pomme': 'apple',
        'chat': 'cat',
        'chien': 'dog'
    }

    # Demonstrate the reverseLookup function with 3 cases
    print("The French words for 'the' are:", reverseLookup(french_to_english, 'the'))
    print("Expected: []")

    print("\nThe French word for 'apple' is:", reverseLookup(french_to_english, 'apple'))
    print("Expected: ['pomme']")

    print("\nThe French word for 'asdf' is:", reverseLookup(french_to_english, 'asdf'))
    print("Expected: []")

# Only call the main function if this file has not been imported
if __name__ == "__main__":
    main()
