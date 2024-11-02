alphabet = "abcdefghijklmnopqrstuvwxyz"

def calculate(string1, string2, string3):
    result = ""
    dict1 = count_letters(string1)
    dict2 = count_letters(string2)
    dict3 = count_letters(string3)
    
# this loop takes the dictionaries and for each place (letter) adds the smallest number of the three ditionaries
# (this will be the crossover) to the result string, then the string is returned
    for i in alphabet:
        if dict1[i] != 0 and dict2[i] != 0 and dict3[i] != 0:
            numRequired = min(dict1[i], dict2[i], dict3[i])
            for j in range(0,numRequired):
                result += i

    return result    

def clean_input(string):
    # cleans the strings by removing non-letter characters and converting upper-case letters to lower-case
    lowerString = string.lower()
    cleanString = ""
    for i in lowerString:
        if i in alphabet:
                cleanString += i
    return cleanString

def count_letters(string):
    dict = {}
# creates a doctionary with entries at zero for each letter in the alphabet
    for i in alphabet:
        dict[i] = 0
# counts every letter in the input string and stores the count in the sictionary, then returns the dictionary
    for i in string:
        dict[i] += 1
    return dict

def main():
    print(
          "Welcome to the calculator!\n",
          "This will take three inputs and tell you what letters are common to all three.\n",
          "First, you will need to enter three lists of words.\n",
          "These can be bunched up words or comma seperated lists,",
          " but each list should be inputted as a single input when asked."
    )
    input("Press enter to continue...")
    
    while True :
    
        string1 = input("Please input your first list here, and then press enter: ")
        string2 = input("Okay, now please input your next list, followed by enter: ")
        string3 = input("And finally, the last list followed by enter: ")
        
        cleanString1 = clean_input(string1)
        cleanString2 = clean_input(string2)
        cleanString3 = clean_input(string3)
        
        result = calculate(cleanString1, cleanString2, cleanString3)
        if result == "":
            result = "There are no common letters in these strings!"
        
        print("\nThe result is:")
        print(result, "\n")

if __name__ == "__main__":
    main()
