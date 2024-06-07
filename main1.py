import os
import multiprocessing


def count_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return len(file.read().split())
    

def main():
    files = [file for file in os.listdir() if file.endswith('.txt')]
    
    with multiprocessing.word() as word:
        counts = word.map(count_file, files)
    
    max_word_count = sum(counts)
    print(f" Barcha .txt fayllarning ichidagi to'liq sonlar : {max_word_count}")

if __name__ == "__main__":
    main()
