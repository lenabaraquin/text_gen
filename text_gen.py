import json
from random import *
import re #regex
import sys #arguments management

def load_dictionnary(dict_name):
    with open(dict_name, "r") as json_file:
        ngram_dict = json.load(json_file)
    return ngram_dict

def extract_n_from_dict_name(dict_name):
    n = re.findall("_[1-9]{1,2}\.", dict_name)
    n = n[-1]
    n = re.sub("[^1-9]", "", n)
    return int(n)

def generate_text(seed, dict_name, gen_lenght):
    n = extract_n_from_dict_name(dict_name)
    ngram_dict = load_dictionnary(dict_name)
    text_gen = seed
    for i in range(gen_lenght):
        ngram = ""
        for j in range(n):
            ngram += text_gen[i+j]
        text_gen += choice(ngram_dict[ngram])
    return text_gen

if __name__ == "__main__":
    seed = sys.argv[1]
    dict_name = sys.argv[2]
    gen_lenght = int(sys.argv[3])
    n = extract_n_from_dict_name(dict_name)
    if len(seed) != n:
        print("With this model, the given seed need to take", n, "characters")
        exit()

    generated_text = generate_text(seed, dict_name, gen_lenght)
    print(generated_text)

