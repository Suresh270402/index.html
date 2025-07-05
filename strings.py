# check whether the charecter is upper,lower or number
# char=input("enter a charecter:")
# user=ord(char)
# if user>=97 and user<=122:
#     print("it is a lowercase charecter")
# elif user>=65 and user<=90:
#     print("it is a uppercase charecter")
# elif user>=48 and user<=57:
#     print("is it number")
# else:
#     print("its not a valid")

# write a function to convert vowel charecters into the next charecter
# def vovels_next(a):
#     next_char=""
#     for i in range(len(a)):
#         user=ord(a[i])
#         if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#             next_char+=chr(user+1)
#         else:
#             next_char+=a[i]
#     return next_char
# print(vovels_next("hello"))


def palindromes(string):
    sring=string.split()
    palindrome_no=False
    count=0
    for i in range(len(string)):
        if string[i][::-1]==string[i]:
            palindrome_no=True
            count+=1
    if palindrome_no:
        print("in string",count,"palindromes")
    else:
        print("no palindromes in this string")
string=input("enter your string:")
palindromes(string)

