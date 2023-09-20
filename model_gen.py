import pygal
import json #dictionnary save
import sys #arguments management



def model_training(corpus, n):
    ngram_dictionnary = {}
    for i in range(len(corpus)-n):
        ngram = ""
        for j in range(n):
            ngram += corpus[i+j]
        #the i rank n-gram as been created
        
        s=1
        #s is a boolean value witch take 1 if the n-gram is new and 0 if the n-gram is already in the dictionnary
        #on suppose le ngram nouveau
        for k in ngram_dictionnary.items():
            if ngram == k[0]:
                s = 0
        #si le n-gram a déjà été rencontré, on passe s à 0
        if s == 1:
            ngram_dictionnary[ngram]=corpus[i+n]
        else:
            ngram_dictionnary[ngram]+=corpus[i+n]
        if i%1000==0:
            print(100*i/len(corpus))
    return ngram_dictionnary

def model_naming(file_name, n):
    n_corpus = str(n)
    model_name = file_name + "_" + n_corpus + ".json"
    return model_name


def model_saving_into_json_file(model_name, ngram_dictionnary):
    with open(model_name, "w") as json_file:
        json.dump(ngram_dictionnary, json_file)
    print("dictionnary ", model_name, " as been created")
    return 0

n = int(sys.argv[1])
file_name = sys.argv[2]

file = open(file_name, "r")
corpus = file.read()
ngram_dictionnary = model_training(corpus, n)
model_name = model_naming(file_name, n)
model_saving_into_json_file(model_name, ngram_dictionnary)
file.close()
