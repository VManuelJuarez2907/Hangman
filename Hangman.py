#Hangman
import random
#from words import words
from words import words
import string

def get_valid_word(words):
    word=random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word= random.choice(words) #keeps choosing until there's no '-' or ' ' 
    return word.upper()

def hangman():
    word= get_valid_word(words)
    word_letters = set(word) #divde the word into their letters
    alphabet_english= set(string.ascii_uppercase) #alphabet in uppercase, english
    used_letters = set() #what the user has guessed
    
    lives=10    
    #getting user input
    while len(word_letters) > 0 and lives>0:
        #letters used
        print(f'You have {lives} lives left. You have used these letters: ', ' '.join(used_letters))
        #what .join does is to convert this format ['a','b','c'] into 'a b c' 
        
        #the next thing to do is to tell the user what the current word is
        #but with '-' in the positions where the words undiscovered are.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet_english - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print(f'{user_letter} is not in the word')
                
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again!')
        else:
            print('Invalid character. Please try again.')
    #gets here when len(word_letters) == 0 OR when they died because lives == 0 
    if lives == 0:
        print(f'Sorry, you died! The correct word was {word}')
    else:
        print(f'You have gessed the word correctly. It was {word}')
if __name__ == '__main__':
    hangman()