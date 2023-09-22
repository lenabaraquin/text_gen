import math
import numpy as np
import json
import sys #arguments
import matplotlib.pyplot as plt

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

def keys_distance_1(key_1, key_2):
    if len(key_1) != len(key_2):
        exit
    d=0
    for i in range(len(key_1)):
        d=d+abs(key_2[i]-key_1[i])
    return d

def dictionary_distance(dictionary_1, dictionary_2):
    match=0
    medium_distance=0
    list_dist=[]
    for key in dictionary_1.keys():
        if matching_key(key, dictionary_2)!=0:
            match+=1
            medium_distance+=keys_distance_1(dictionary_1[key], dictionary_2[key])
            list_dist.append(keys_distance_1(dictionary_1[key], dictionary_2[key]))

    medium_distance = medium_distance/match
    match = match / max(len(dictionary_1), len(dictionary_2))
    match = 1 - match
    return list_dist
#    return [match, medium_distance]

def mixed_distance(k, match, medium_distance):
    medium_distance=1-1/(1+medium_distance)
    medium_distance=k*medium_distance
    match=(1-k)*match
    return medium_distance+match

def norme(liste):
    n = 0
    p = 1
    n = np.linalg.norm(liste, ord=p)
    return n

def farthest_point_distance(liste):
    d = 0
    r = 1 #les valeurs des probas des caractères suivants sont comprises entre 0 et 1, le rayon de la boule de l'espace des probabilités est donc de 1 (pas très rigoureuse cette explication)
    p = 1 #on utilise la norme 1
    d = norme(liste) + r
    return d

def distance_stella(D1,D2):
    d = 0
#    i = 0
    
    for m in D1.keys():
        if m in D2.keys():
            diff_list = []
            for i in range(len(D1[m])):
                diff_list.append(D1[m][i]-D2[m][i])
            d += norme(diff_list)
        else :
            d += farthest_point_distance(D1[m])
#        i += 1
    
    for m in D2.keys():
        if m not in D1.keys():
            d += farthest_point_distance(D2[m])
#            i += 1
    
#    d = d/i
    return d


if __name__ == "__main__":
    file_dictionary_1 = sys.argv[1]
    file_dictionary_2 = sys.argv[2]
    dictionary_1=load_dictionary(file_dictionary_1)
    dictionary_2=load_dictionary(file_dictionary_2)
    d = distance_stella(dictionary_1, dictionary_2)
    print(d)
#    d = dictionary_distance(dictionary_1, dictionary_2)
#    d.sort()
#    print(d)
#    plt.plot(d)
#    plt.show()
#    k=0.5
#    m_d=mixed_distance(k, d[0], d[1])
#    print(f"match, distance moyenne {d}")
#    print(f"mixed_distance {m_d}")


