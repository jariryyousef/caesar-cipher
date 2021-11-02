import re
import nltk
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()


def encrypt(text, key):
    result = "" 
    for i in text:

        if i.isupper():  
            key_shift = ((ord(i) - ord('A')) + key) % 26 + ord('A')
            new_letter = chr(key_shift)
            result += new_letter

        elif i.islower(): 
            key_shift = ((ord(i) - ord('a')) + key) % 26 + ord('a')
            new_letter = chr(key_shift)
            result += new_letter
        
        elif i.isdigit():
            result += str(((int(i) + key) % 10))
        else:
            result += i
    return result

def decrypt(text, key):

    result = ""
    for i in text:
        if i.isupper():

            index_key = ((ord(i) - ord('a')) - key) % 26 + ord('A')
            old_letter = chr(index_key)
            result += old_letter

        elif i.islower():

            index_shifted_back = ((ord(i) - ord('a')) - key) % 26 + ord('a')
            old_letter = chr(index_shifted_back)
            result += old_letter
        elif i.isdigit():

            old_number = (int(i) - key) % 10
            result += str(old_number)
        else:
            result += i

    return result


def crack(text):
    for i in range(26):
        word_decrypted =  decrypt(text,i)
        word = re.sub(r'[^A-Za-z]+','', word_decrypted)
        if word.lower() in word_list or word in name_list:
            return (word_decrypted)