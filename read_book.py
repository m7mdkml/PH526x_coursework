# read_book.py by mohammed

# intended to read a book as a str
def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text
 
# return number of unique words and word frequencies
def word_stats(word_counts):
  num_unique = len(word_counts)
  counts = word_counts.values()
  return (num_unique, counts)
