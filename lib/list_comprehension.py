#!/usr/bin/env python3

def return_evens(num_list):
   
    if num_list == []:
       return []
    else:
        num_list = [num for num in num_list if num % 2 == 0]
    return num_list


def make_exclamation(sentence_list):
    if sentence_list == []:
        return []
    else:
        sentence_list = [sentence + '!' for sentence in sentence_list]
        return sentence_list
 

