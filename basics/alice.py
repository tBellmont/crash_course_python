
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the number of word in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['text_files/alice_in_wonderland.txt', 'text_files/guest_book.txt', 'text_files/learning_python.txt', 'dfefe.txt']
for filename in filenames:
    count_words(filename)