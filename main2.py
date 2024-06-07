import os
import multiprocessing
import re

def count_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        count = file.read()
        return len(re.findall(r'\d', count))

def main():
    files = [file for file in os.listdir()
              if file.endswith('.txt')]
    
    
    with multiprocessing.Pool() as make:
        counts = make.map(count_file, files)
    
    max_count = sum(counts)
    print(f"Barcha .txt fayllarning ichida to'liq sonlar: {max_count}")

if __name__ == "__main__":
    main()


