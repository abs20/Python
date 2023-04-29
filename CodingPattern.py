'''
Two Pointers
Statement
Write a function that takes a string s as input and checks whether it’s a palindrome or not.

Note: A phrase, word or sequence is a palindrome that reads the same backwards as forwards.

Constraints:
- 1≤1≤ s.length ≤2×105≤2×105
- The string won’t have any spaces and will only consist of ASCII characters.

The string won’t have any spaces and will only consist of ASCII characters.
'''


def palindrome(str):
    l = 0
    r = len(str)-1

    while l < r:
        if str[l] == str[r]:
            l =+ 1
            r =- 1
        else:
            return("Not Palindrome")

    return("Palindrome")

def main():
    str = input().strip().split(' ')

    print(palindrome(str))

if __name__ == '__main__':
    main()
