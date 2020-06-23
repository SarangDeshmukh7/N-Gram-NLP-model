# Natural Language Processing using Python

# N-Gram Modelling - Word Grams
# Importing libraries
import random
import nltk

# Sample data
text = """India is a great country where people speak different languages but the national language is Hindi.
India is full of different castes, creeds, religion, and cultures but they live together. That’s the reasons 
India is famous for the common saying of “unity in diversity“. India is the seventh-largest country in the whole world."""

# Order of the grams
n = 2

# Our N-Grams
ngrams = {}

# Building the model
words = nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
# Testing the model
currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextItem
    rWords = nltk.word_tokenize(result)
    currentGram = ' '.join(rWords[len(rWords)-n:len(rWords)])

print(result)
