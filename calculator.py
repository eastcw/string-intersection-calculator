alphabet = "abcdefghijklmnopqrstuvwxyz"

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
    print(
          "Welcome to the calculator!\n",
          "First, I will ask you how many lists you want to compare.\n",
          "Then, you can enter your lists of words. \n",
          "These can be bunched up words or comma seperated lists,",
          " but each list should be inputted as a single input when asked."
    )
    input("Press enter to continue...")
    
    while True :
        strings = []
        numOfStrings = 0
        while not (isinstance(numOfStrings,int) and numOfStrings > 1):
            try:
                numOfStrings = int(input("How many lists do you want to compare? Please enter a whole number: "))
            except ValueError:
                input("The input here must be a whole number please. Press enter to continue.")
                continue
            if isinstance(numOfStrings,int) and numOfStrings > 1:
                break
            input("This number needs to be a positive number of two or more please. Press enter to continue.")
        for i in range(0,numOfStrings):
            strings.append(clean_input(input("Please enter list " + str(i+1) + ": ")))
        result = calculate(strings)
        if result == "":
            result = "There are no common letters in these strings!"
        
        print("\nThe result is:")
        print(result, "\n")

if __name__ == "__main__":
    main()
