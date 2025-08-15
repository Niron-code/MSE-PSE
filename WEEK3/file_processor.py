class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_and_print(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
            return content
        except UnicodeDecodeError:
            print("Error: Could not decode file. Try a different encoding.")
            return None
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None

    def write_content_to_philip(self, content):
        if content is not None:
            output_path = r"C:\Users\HP\Downloads\philip.txt"
            try:
                with open(output_path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Content written to {output_path}")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("No content to write.")

def main():
    file_path = r"C:\Users\HP\Downloads\demo.txt"
    processor = FileProcessor(file_path)
    content = processor.read_and_print()
    processor.write_content_to_philip(content)

if __name__ == "__main__":
    main()