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
        if word in sentence_words:
            return text.index(sentence)
 
 
def main():
    
        words = get_words(text)
        words_dict = get_words_dict(words)
        
        print(f"{'word':10}{'count':<10}{'occurrence':>10}")
        for word in words_dict:
            index_occerence = get_index_text(word)
            print(f"{word:<10}{words_dict[word]:<10}{index_occerence:<10}")

main()