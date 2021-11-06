#!/usr/bin/env python

##From the exercise prompt

class SentenceIterator:
    def __init__(self, words): 
        self.words = words 
        self.index = 0

    def __next__(self): 
        try:
            word = self.words[self.index] 
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return word 

    def __iter__(self):
        return self

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word #GENERATOR
        #return SentenceIterator(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


my_sentence = Sentence("Yo Vitoria has coffee 4 times a day")

#ITER OF MY SENTENCE IS A GENERATOR
iter(my_sentence) #this is a <generator object>
print(list(iter(my_sentence)))#to actually see my generator , i have to print it through a list

my_sentence # this is simply a <main>

