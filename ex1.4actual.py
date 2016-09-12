#Get user input
initial_1 = (input("Please enter first string: ")).lower()
initial_2 = (input("Please enter second string: ")).lower()
if len(initial_1) >= len(initial_2):
    str_1 = initial_1
    str_2 = initial_2
else:
    str_1 = initial_2
    str_2 = initial_1

#Slice the strings
def finding_substrings(smaller, longer):
    slice = ''
    longest_substring = ''
    for i in range(0,len(smaller)):
        for j in range(i+1,len(smaller)+1):
            slice = smaller[i:j]
            substring = longer.find(slice)
            if substring == -1:
                break
            else:
                if len(slice) > len(longest_substring):
                    longest_substring = slice
    return longest_substring

longest_substring = finding_substrings(str_2, str_1)
if longest_substring == '':
    print ("You should've entered strings that had things in common")
else:
    print (longest_substring)
