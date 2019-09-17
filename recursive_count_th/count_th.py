'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    string = "th"

    #check if string exists in word (find returns the index and -1 is not found)
    if word.find(string) != -1:
        #remove one the first occurence of 'th'
        new_string = word.replace(string, " ", 1)
        #return 1 for this occurence plus the rest of the count
        return 1 + count_th(new_string)
    else:
        #Recursion stops when the string is not found anymore
        return 0


