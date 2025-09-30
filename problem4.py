"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    with open (filename, "r") as f:
        text = f.read()         # lire tout le contenu du fichier
        words = text.split()    # séparer le texte en mots
        return len(words)       # compter combien il y a de mots




def count_lines(filename):
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    # TODO: Open file and count lines
    with open(filename, 'r') as f:
        return sum(1 for _ in f)
  


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """

    # TODO: Open file and count characters
    # If include_spaces is False, don't count spaces
    with open(filename, 'r') as f:
        text = f.read()
    if include_spaces:
        return len(text)  # compte tout
    else:
        return sum(1 for ch in text if not ch.isspace())



def find_longest_word(filename):
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    # TODO: Find the longest word
    # Hint: You might need to remove punctuation
    import string
    with open(filename, 'r') as f:
        text = f.read()
    table = str.maketrans({ch: " " for ch in string.punctuation})
    cleaned = text.translate(table)

    # séparer en mots
    words = cleaned.split()

    if not words:   # si le fichier est vide
        return ""

    return max(words, key=len)

    


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    import string

    with open(filename, 'r') as f:
        text = f.read()

    # mettre en minuscules
    text = text.lower()

    # enlever la ponctuation
    table = str.maketrans({ch: " " for ch in string.punctuation})
    cleaned = text.translate(table)

    # découper en mots
    words = cleaned.split()

    # dictionnaire vide
    frequency = {}

    # compter chaque mot
    for w in words:
        if w in frequency:
            frequency[w] += 1
        else:
            frequency[w] = 1

    return frequency

    # TODO: Open file
    # TODO: Read all words
    # TODO: Convert to lowercase
    # TODO: Remove punctuation (use string.punctuation)
    # TODO: Count frequency of each word

    


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()