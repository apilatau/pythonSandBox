import re

text = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]
 
 
def get_words(text):
    words = []
    for sentence in text:
        words_in_sentence = re.findall(r'\w+', sentence.lower())
        for item in words_in_sentence:
            words.append(item)
    
    return words
 
 
def get_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

def get_index_text(word):
    for sentence in text:
        sentence_words = re.split(r'\W+', sentence.lower())        
        try:
            index_sentence = sentence_words.index(word)
        except:
            continue
        return text.index(sentence)
 
 
def main():
    
        words = get_words(text)
        words_dict = get_words_dict(words)
        
        print("word         count      occerence")
        for word in words_dict:
            index_occerence = get_index_text(word)
            print(f"{word.ljust(7)}         {words_dict[word]}       {index_occerence}")

main()