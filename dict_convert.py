import json
import os #base_name
import sys #arguments

def load_dictionnary(file_input):
    with open(file_input, "r") as json_file:
        dict_enum = json.load(json_file)
    return dict_enum

def convert(dict_enum):
    dict_freq={}
    character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "ø", "œ", "ù", "ú", "û", "ü", "ý", "þ", "ß", "ÿ"]
    for i in dict_enum.keys():
        dict_freq[i] = []
        for j in character_list:
            freq_j = dict_enum[i].count(j)
            freq_j = freq_j/len(dict_enum[i])
            dict_freq[i].append(freq_j)
    return dict_freq

def save_dictionnary(file_output, dict_freq):
    with open(file_output, "w") as json_file:
        json.dump(dict_freq, json_file)
    print("the dictionnary", file_input, "as been converted")
    return 0

if __name__ == "__main__":
    file_input = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(file_input))[0]
    file_output = f"{base_name}_freq.json"
    dict_enum = load_dictionnary(file_input)
    dict_freq = convert(dict_enum)
    save_dictionnary(file_output, dict_freq)
    print(f"The dictionary {file_input} has been converted and saved as {file_output}")

