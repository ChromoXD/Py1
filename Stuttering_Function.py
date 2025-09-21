import os

_Inpt = input("enter the word: ")

def Stuttering_Function(word):
    return (2*(word[0] + word [1] + ".. ") + word + "?")

print(Stuttering_Function(_Inpt))