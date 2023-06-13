import random

file = input("What file? ")

class WordFinder:
    def __init__(self, filename):
        self.filename = filename
        self.word_counts = {}
    
    def process_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    self.word_counts[word] = self.word_counts.get(word, 0) + 1
    def get_total_word_counts(self):
        return sum(self.word_counts.values())
    def get_words_list(self):
        return self.word_counts

word_finder = WordFinder(file)

word_finder.process_file()

word_count = word_finder.get_total_word_counts()
word_list = word_finder.get_words_list()
random_word = random.choice(list(word_list.keys()))
print(f"{word_count} words read")
print(random_word)