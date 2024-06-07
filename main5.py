import os
import string
import multiprocessing


def delete_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        count = file.read()
        

    ozgartiruvchi = str.maketrans('', '', string.punctuation)
    deleter_count = count.translate(ozgartiruvchi)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(deleter_count)


def main():
    files = [file for file in os.listdir() if file.endswith('.txt')]
    

    with multiprocessing.Pool() as pool:
        pool.map(delete_file, files)


if __name__ == "__main__":
    main()


