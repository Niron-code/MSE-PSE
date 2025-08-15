import pandas as pd
import numpy as np
import re

class FileWordCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_words(self, chunk_size=1024*1024):
        word_count = 0
        try:
            for chunk in pd.read_csv(self.file_path, sep='\n', header=None, encoding='utf-8', chunksize=chunk_size, engine='python'):
                # Each chunk is a DataFrame with one column
                lines = chunk.iloc[:, 0].values
                # Use numpy and regex for fast splitting
                words = np.concatenate([re.findall(r'\b\w+\b', line) for line in lines])
                word_count += len(words)
        except UnicodeDecodeError:
            print("Error: Could not decode file. Try a different encoding.")
            return None
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def main():
    file_path = r"C:\Users\HP\Downloads\demo.txt"
    counter = FileWordCounter(file_path)
    word_count = counter.count_words()
    if word_count is not None:
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()