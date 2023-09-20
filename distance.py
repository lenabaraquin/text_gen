import math
import json
import sys #arguments

def load_dictionary(file_input):
    with open(file_input, "r") as json_file:
        dictionary = json.load(json_file)
    return dictionary

def matching_key(key, dictionary):
    b=0
    for i in dictionary.keys():
        if i==key:
            b=1
    if b==1:
        return key
    else:
        return 0

def keys_euclidian_distance(key_1, key_2):
    if len(key_1) != len(key_2):
        exit
    d=0
    for i in range(len(key_1)):
        d=d+(key_2[i]-key_1[i])*(key_2[i]-key_1[i])
    d=math.sqrt(d)
    return d

def dictionary_distance(dictionary_1, dictionary_2):
    match=0
    medium_distance=0
    for key in dictionary_1.keys():
        if matching_key(key, dictionary_2)!=0:
            match+=1
            medium_distance+=keys_euclidian_distance(dictionary_1[key], dictionary_2[key])
    medium_distance = medium_distance/match
    match = match / max(len(dictionary_1), len(dictionary_2))
    return [match, medium_distance]

def mixed_distance(k, match, medium_distance):
    medium_distance=1-1/(1+medium_distance)
    medium_distance=k*medium_distance
    match=(1-k)*match
    return medium_distance+match


if __name__ == "__main__":
    file_dictionary_1 = sys.argv[1]
    file_dictionary_2 = sys.argv[2]
    dictionary_1=load_dictionary(file_dictionary_1)
    dictionary_2=load_dictionary(file_dictionary_2)
    d = dictionary_distance(dictionary_1, dictionary_2)
    print(f"match, distance moyenne {d}")


