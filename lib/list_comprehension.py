#!/usr/bin/env python3


def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    print(evens if evens else [])
    return evens
   

def make_exclamation(sentence_list):
    return [(sentence + '!') for sentence in sentence_list]