"""
The function checks if the number of 'o's in the input string is exactly twice the number of 'z's.
If the condition is met, it prints "Yes"; otherwise, it prints "No".

Input: A string containing only the characters 'z' and 'o', with a maximum length of 20 characters.
Output: "Yes" if the number of 'o's is twice the number of 'z's, otherwise "No".

Example:
Input: "zoo"
Output: "Yes"
"""

def check_zoo(zoo):

    for each_character in zoo:
        if each_character in ['z', 'o']:
            total_z = zoo.count('z')
            total_o = zoo.count('o')
            if (total_z*2) == total_o:
                print("Yes")
                break
            else:
                print("No")
                break

zoo = input("\nEnter the string: ")[:20]
check_zoo(zoo)