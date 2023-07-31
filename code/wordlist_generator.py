import random
import string

def generate_words(special_chars, word_length_range, num_words, include_lowercase, include_uppercase):
    generated_words = set()
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    characters += string.digits + special_chars

    min_word_length, max_word_length = word_length_range
    word_length_range = range(min_word_length, max_word_length + 1)

    while len(generated_words) < num_words:
        word_length = random.choice(word_length_range)
        word = ''.join(random.choice(characters) for _ in range(word_length))
        generated_words.add(word)

    return generated_words

def main():
    print("Welcome to the Random Word Generator!")
    special_chars = input("Enter the special characters (e.g., !@#$): ")
    min_word_length = int(input("Enter the minimum word length: "))
    max_word_length = int(input("Enter the maximum word length: "))
    num_words = int(input("Enter the number of words to generate: "))
    include_lowercase = input("Include lowercase characters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase characters? (y/n): ").lower() == 'y'

    if min_word_length <= 0 or max_word_length < min_word_length or num_words <= 0:
        print("Invalid input. Please provide valid inputs.")
        return

    word_length_range = (min_word_length, max_word_length)
    words = generate_words(special_chars, word_length_range, num_words, include_lowercase, include_uppercase)
    
    print(f"\nGenerated {len(words)} unique words:")
    for word in words:
        print(word)


    # Export generated words to "wordlist.txt"
    with open("wordlist.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

    print("Generated words have been exported to 'wordlist.txt'.")

if __name__ == "__main__":
    main()

