import csv
import os
import random

def main():
    print('Norwegian Flash Cards!')
    print('[1] Guess English words from Norwegian in order from 1-1000')
    print('[2] Guess Norwegian words from English in order from 1-1000')
    print('[3] Guess English words from Norwegian at random')
    print('[4] Guess Norwegian words from English at random')
    while True:
        try:
            choice = int(input('What kind of practice would you like to do today: '))
            if choice == 1 or choice == 2:
                display_rows_sequence(choice)
            if choice == 3 or choice == 4:
                display_rows_random(choice)
        except:
            print('invalid input')
            break

    


def english_from_norwegian(row):
    os.system('cls')
    print(row[0] + ': ' + row[1])
    answer = str(input("What is the English word for this: "))

    if answer.lower() == row[2].lower():
        print("correct")
    else:
        print("wrong the answer is " + row[2])
        os.system('pause')

def norwegian_from_english(row):
    os.system('cls')
    print(row[0] + ': ' + row[2])
    answer = str(input("What is the Norsk word for this: "))

    if answer.lower() == row[1].lower():
        print("correct")
    else:
        print("wrong the answer is " + row[1])
        os.system('pause')

def display_rows_sequence(choice):
    rows = read_rows()
    for row in rows:
        if choice == 1:
            english_from_norwegian(row)
        elif choice == 2:
            norwegian_from_english(row)

def display_rows_random(choice):
    rows = read_rows()
    while True:
        random_row = random.choice(rows)
        if choice == 3:
            english_from_norwegian(random_row)
        elif choice == 4:
            norwegian_from_english(random_row)
            
def read_rows():
    with open('norsk.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        rows = list(reader)
        return rows
    
if __name__  == '__main__':
    main()



    
