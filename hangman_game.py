'''This for is a project to train my level in python
The program gives you 3 chances to try guess the word, letter per letter.
Do you want to make a partnership or project?
Contact-me:
Email: assalim.py@gmail.com
Instagram: JoaoAssalim_
Github: JoaoAssalim'''


from random import choice
from colorama import Fore
def points_3(): #Initial hangman
    print('''
|-----
|     |
|
|
|
|
|
    ''')
def points_2(): #hangman with 1 error
    print('''
|-----
|     |
|     o
|     |
|     |
|
|
    ''')
def points_1(): #hangman with 2 errors
    print('''
|-----
|     |
|     o
|    /|\\
|     |
|
|
    ''')
def points_0(): #hangman with 3 errors == You lose
    print('''
|-----
|     |
|     o
|    /|\\
|     |
|    / \\
|
    ''')

typed_right = []
words_typed_wrong = set()

#Functions choicing a word in the list
def words_to_guess():
    list_animals = ['monkey','dog','cat','bear','bird','fish','chicken','cow','fox','horse'] #Animal List
    list_countries = ['brazil','belgium','mexico','canada','china','france'] #Countries list
    list_colors = ['green','yellow','red','blue','cyan','black','white','orange','purple','gray'] #Colors list
    
    totaly_lists = [list_animals, list_countries, list_colors] #store the 3 lists
    list_choiced = choice(totaly_lists) #Choice one of the lists
    choiced_word = choice(list_choiced) #Choice a word in the list choiced

    if list_choiced == list_animals: #verify if the choiced list is equal animal list
        print('Tip: this word is a animal' + '\n')
    elif list_choiced == list_countries:
        print('Tip: this word is a Country' + '\n')#verify if the choiced list is equal countries list
    elif list_choiced == list_colors:
        print('Tip: this word is a Color' + '\n')#verify if the choiced list is equal colors list
    
    points_3() #print the initial fork
    
    #make a display with "_" to user see how many letters are correct and how many are left
    display = []
    for i in range(len(choiced_word)):
        display += "_"
    print(display)

    #Separate the word in letters
    lista_set = set()
    for i in choiced_word: 
        lista_set.add(i)
    lista_set = sorted(lista_set) #arrange alphabetically
    chances = 3 #Chances to guess the word

    while True:
        letter = input(Fore.BLUE+'Type a letter: ').lower() #Try to guess any letter per time
        if len(letter) == 1:
            if letter in lista_set: #if letter is in word, the program execute
                for pos in range(len(choiced_word)):
                    let = choiced_word[pos]
                    if let == letter:
                        display[pos] = let
                        
                typed_right.append(letter)
                print(Fore.GREEN+'Letter in secret word')
                #For letter in the List, a set add the letter to verify if is equal the user typed 
                list_typed_right = set()
                for letter_right in typed_right:
                    list_typed_right.add(letter_right)
                list_typed_right = sorted(list_typed_right)
                if lista_set == list_typed_right: #Verify if all the letters is in 2 words
                    print(f"you Win, The word is: {choiced_word}")
                    break

            elif letter not in lista_set:#if letter is not in word, the program execute
                words_typed_wrong.add(letter)
                print(Fore.RED+'Letter not in secret word')
                chances -=  1 #take a point for making a mistake

                if chances == 2:
                    points_2()
                elif chances == 1:
                    points_1()
                elif chances == 0:
                    points_0()
                    print(f'You losed, The word is: {choiced_word}')
                    break
        print(display)
        print(Fore.RED+f'Words Typed wrong: {sorted(words_typed_wrong)}') #Print every letter typed
words_to_guess()
