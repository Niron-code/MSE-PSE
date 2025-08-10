class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        # Split the sentence by whitespace and count the words
        words = self.sentence.split()
        return len(words)

def main():
    sentence = input("Enter a sentence: ")
    counter = WordCounter(sentence)
    word_count = counter.count_words()
    print(f"Number of words in the sentence: {word_count}")

if __name__ == "__main__":
    main()
