alphabet = "qwertyuiopasdfghjklzxcvbnm"

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

# these three arrays count the number of each letter in each string, they start at 26 x zero
    array1 = [0 for i in range(len(alphabet))]
    array2 = [0 for i in range(len(alphabet))]
    array3 = [0 for i in range(len(alphabet))]
    
    length1 = len(string1)
    length2 = len(string2)
    length3 = len(string3)

# these for loops count the numbers of each letter and store the values in the arrays
    for i in range(0,length1):
        array1[ord(string1[i]) - ord("a")] += 1

    for i in range(0,length2):
        array2[ord(string2[i]) - ord("a")] += 1

    for i in range(0,length3):
        array3[ord(string3[i]) - ord("a")] += 1
    
# this loop takes the arrays and for each place (letter) adds the smallest number of the three arrays
# (this will be the crossover) to the result string, then the string is returned
    for i in range(0,len(alphabet)):
        if array1[i] != 0 and array2[i] != 0 and array3[i] != 0:
            numRequired = min(array1[i], array1[i], array3[i])
            for j in range(0,numRequired):
                result += chr(ord("a")+i)

    return result    

print(
      "Welcome to the calculator!\n",
      "This will take three inputs and tell you what letters are common to all three.\n",
      "First, you will need to enter three lists of words.\n",
      "These can be bunched up words or comma seperated lists,",
      " but each list should be inputted as a single input when asked."
)
input("Press enter to continue...")

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
print(result)
