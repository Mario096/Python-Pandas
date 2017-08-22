def isAnagram(s1,s2):
    s1list = []
    s2list = []

    #append the chars to a list, sort the list
    for char in s1:
        char = char.lower()
        s1list.append(char)
    s1list.sort()
    for char2 in s2:
        char2 = char2.lower()
        s2list.append(char2)
    s2list.sort()

    #if the lists are the same return True
    if s1list == s2list:
        return True
    else:
        return False




def main():

    #get the two strings
    s1 = input("Enter the first word:")
    s2 = input("Enter the second word:")

    #apply the anagram function
    are = (isAnagram(s1,s2))

    #print out the correct statement
    if are:
        print('The words "' + s1 + '" and "' + s2 + '" are anagrams')

    else:
        print('The words "' + s1 + '" and "' + s2 + '" are not anagrams')



main()