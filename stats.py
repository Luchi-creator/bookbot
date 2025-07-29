def count_words(text):

    new_text = text.split()
    return len(new_text)


def count_appereances(text):

    appereances = {}
    new_text = text.lower()

    for i in range(len(new_text)):
        if new_text[i] in appereances:
            appereances[new_text[i]] += 1
        else:
            appereances[new_text[i]] = 1
    
    return appereances

def sort_on(items):
    return items["num"]

def sort_dictionary(words_dictionary):
    
    final_list = []

    for i in words_dictionary:
            dict = {"char":i,"num":words_dictionary[i]}
            if(i.isalpha() == True):
                final_list.append(dict)

    final_list.sort(reverse=True,key=sort_on)
    return final_list