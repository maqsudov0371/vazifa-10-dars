import os
import multiprocessing
import re

def count_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        count = file.read()
        sentences = re.split(r'[.!?]+', count)
        return len([file for file in sentences if file.strip()])

def main():
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
    with multiprocessing.Pool() as make:
        counts = make.map(count_file, txt_files)
    
    max_count = sum(counts)
    print(f"Barcha .txt fayllarning qo'shimcha belgilari: {max_count}")

if __name__ == "__main__":
    main()

