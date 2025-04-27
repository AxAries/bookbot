
def count_words(words):
    
    """
    for punctuation in string.punctuation:
        words = words.replace(punctuation, "")
    return len(words.split())
    """

    return len(words.split())

def numbers_of_characters(words):
    num_char = {}
    for x in words.lower():
        num_char[x] = (num_char.get(x, 0)+1)
    
    return num_char

def sorted_lst(dict):
    return dict["num"]

def number_of_alfachars(char):
    chars=[]
    for x in char:
        alfa={"char":x, "num":char[x]}
        chars.append(alfa)

    chars.sort(reverse=True, key=sorted_lst)
    return chars