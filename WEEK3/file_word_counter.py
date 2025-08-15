class FileWordCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_words(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()
                words = content.split()
                return len(words)
        except UnicodeDecodeError:
            print("Error: Could not decode file. Try a different encoding.")
            return None
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None

def main():
    file_path = r"C:\Users\HP\Downloads\demo.txt"
    counter = FileWordCounter(file_path)
    word_count = counter.count_words()
    if word_count is not None:
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()