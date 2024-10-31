alphabet = "abcdefghijklmnopqrstuvwxyz"

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

def clean_input(string):
    # cleans the strings by removing non-letter characters and converting upper-case letters to lower-case
    lowerString = string.lower()
    cleanString = ""
    for i in lowerString:
        for j in alphabet:
            if i == j:
                cleanString += i
                break
    return cleanString

def calculate(string1, string2, string3):
    result = ""
    dict1 = {}
    dict2 = {}
    dict3 = {}

# these three dictionaries count the number of each letter in each string, they start at 26 x zero with letter keys
    for i in alphabet:
        dict1[i] = 0
        dict2[i] = 0
        dict3[i] = 0

# these for loops count the numbers of each letter and store the values in the dictionaries
    for i in string1:
        dict1[i] += 1

    for i in string2:
        dict2[i] += 1
        
    for i in string3:
        dict3[i] += 1
    
# this loop takes the dictionaries and for each place (letter) adds the smallest number of the three ditionaries
# (this will be the crossover) to the result string, then the string is returned
    for i in alphabet:
        if dict1[i] != 0 and dict2[i] != 0 and dict3[i] != 0:
            numRequired = min(dict1[i], dict2[i], dict3[i])
            for j in range(0,numRequired):
                result += i

    return result    

if __name__ == "__main__":
    main()
