# counting_words.py by mohammed

text = "This comprehension check is to check for comprehension."

# Counts the number of times each word occurs in a str, skips punctuation.
def count_words(text):
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch,"")
    
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else: 
            word_counts[word] = 1
    return word_counts

print(count_words(text))
