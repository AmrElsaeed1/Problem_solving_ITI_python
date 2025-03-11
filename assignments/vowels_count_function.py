def count_vowels(string):
    try:
        if not isinstance(string, str):
            raise ValueError("Input must be a string.")

        vowels = {"a", "e", "i", "o", "u"}

        return sum(1 for char in string.lower() if char in vowels)

    except ValueError:
        return "Invalid input"
