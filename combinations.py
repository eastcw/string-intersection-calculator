alphabet = "abcdefghijklmnopqrstuvwxyz"

calculateNoDuplicates = False # set this to True if you want to ignore duplicate letters

# Put your input words into these three arrays. Each sub-array should contain possibilities for one clue.
# Don't forget the quotes!
circle1 = [
    ["variants", "for", "the", "first", "word"],
    ["variants", "for", "the", "second", "word"],
    ["etc"]
]
circle2 = [
    ["variants", "for", "the", "first", "word"],
    ["variants", "for", "the", "second", "word"],
    ["etc"]
]
circle3 = [
    ["variants", "for", "the", "first", "word"],
    ["variants", "for", "the", "second", "word"],
    ["etc"]
]

def calculate(strings):
    result = ""
    letterCounts = []
    for i in range(0,len(strings)):
        letterCounts.append(count_letters(strings[i]))
    
# this loop takes the dictionaries and for each place (letter) adds the smallest number in that position of all the
# dictionaries (this will be the intersection) to the result string, then the string is returned
    for i in alphabet:
        smallest = letterCounts[0][i]
        # this loop calculates the smallest number for a given letter in all the inputs
        for j in range(0,len(letterCounts)):
            if letterCounts[j][i] < smallest:
                smallest = letterCounts[j][i]
        # this loop adds that number of the right letter to the output
        for k in range(0,smallest):
            result += i
    return result

def calculate_no_duplicates(strings):
    result = ""
    letterCounts = []
    for i in range(0,len(strings)):
        letterCounts.append(count_letters(strings[i]))
    
# this loop takes the dictionaries and for each place (letter) adds the smallest number in that position of all the
# dictionaries (this will be the intersection) to the result string, then the string is returned
    for i in alphabet:
        isInAll = True
        for j in letterCounts:
            if j[i] == 0:
                isInAll = False
        if isInAll == True:
            result += i
    return result     

def clean_input(string):
    # cleans the strings by removing non-letter characters and converting upper-case letters to lower-case
    string = string.lower()
    cleanString = ""
    for i in string:
        if i in alphabet:
                cleanString += i
    return cleanString

def count_letters(string):
    dict = {}
# creates a dictionary with entries at zero for each letter in the alphabet
    for i in alphabet:
        dict[i] = 0
# counts every letter in the input string and stores the count in the sictionary, then returns the dictionary
    for i in string:
        dict[i] += 1
    return dict

def main():
    for i in itertools.product(*circle1):
        for j in itertools.product(*circle2):
            for k in itertools.product(*circle3):
                if calculate_no_duplicates == False:
                    print(calculate([clean_input(str(i)), clean_input(str(j)), clean_input(str(k))]))
                else:
                    print(calculate_no_duplicates([clean_input(str(i)), clean_input(str(j)), clean_input(str(k))]))

if __name__ == "__main__":
    import itertools
    main()
