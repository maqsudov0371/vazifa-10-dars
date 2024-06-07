import os
import multiprocessing
import re


def longest_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        count = file.read()
        malumot = re.split(r'( len=[ ]) +', count)
        longest_word = max(malumot, key=len).strip() if malumot else ''
        return longest_word
    

def main():
    files = [file for file in os.listdir() if file.endswith('.txt')]
    

    with multiprocessing.Pool() as pool:
        longest_word = pool.map(longest_word, files)
    

    object = max(longest_word, key=len).strip() if longest_word else ''
    print(f"Eng uzun soz: {object}")


if __name__ == "__main__":
    main()


