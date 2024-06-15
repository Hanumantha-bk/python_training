# #  Slicing Operation  #
# s=input()
# fc=s[0]
# for i in range(len(s)) :
#     if s[i]==fc.upper() or s[i]==fc.lower():
#         s=s[:i]+'$'+s[i+1:]
#         r=fc+s[1:]
#         print(r)   
# str="ram ram"
# print("Given String :",str)
# ch = str[0]
# str = str.replace(ch, '$')
# str = ch + str[1:]
# print("After String :",str)     

# # Write a program to add 'ing' at the end of a given string.if the given string already ends with 'ing' then add 'ly'.if the string length is less than 3,leave it unchanged

# string = input()
# if len(string) < 3:
#   print(string)
# elif string[-3:] == 'ing':
#   print(string + 'ly')
# else:
#   print(string + 'ing')  


# str=input("Enter a String :")
# if len(str)>=3:
#     if str.endswith('ing'):
#       ns=str+'ly'
#     else:
#       ns=str+'ing'
# else :
#     ns=str
#     print("Modified String :",ns) 


# s=input()
# r,t="ing","ly"
# if len(s) >3 and s.endswith(r) :
#     print(s[:-3]+t)
# else:
#     print(s if len(s) <=3 else s+r)     

# #write a program tha takes a string as input and returns the length of the longest word in it.

# # str="Anaconda is a Python Prompt"
# str=input("enter a String : \t")
# wrds=str.split()
# l=0
# for wrd in wrds:
#     if len(wrd)>l :
#         l=len(wrd)
# print("Length of Longest Word : ",l)  


# # Write a Program that changes a given string to a new string where the first and last characters have been exchanged

# str="Hann"
# if len(str)>=2 :
#     ns=str[-1]+str[1:-1]+str[0]
#     print("Modified String : ",ns)
# else :
#      print("String is too short")    

 
#  # write a python program to remove the characters with odd index values from the given Sting 


# str=input()
# res = ""
# for i in range(len(str)):
# 	if i % 2 == 0:
# 	  res = res + str[i]
# print(res)


# # write a program that prompts the user to enter a string.
# # the program calculates and display the length of the string until the user enters 'Quit'
# stng=input("Enter a string :  ")
# while stng!='QUIT':
#    print('length of string :',len(stng))
#    stng=input("Enter a string :  ")  


# while True :
#     strng=input("Enter a String (or 'QUIT' to exit)")
#     if strng.upper()=='QUIT' :
#         print("Exiting the Program--")
#         break
#     lngth=len(strng)
# print(f "length of the string:{lngth}")

# stng=input("enter five words:")
# if len(stng)<6:
#     print("re enter the chr :")
# else :
#       if len(stng)>=6:
#            print(stng)

# '''
# # Write a Python Program that prompts the user to enter five words.
# # if the length of any word is less than 6 characters,
# # the program asks user to enter it again.however,if the word is 6 or more characters long,
# # display it on the Screen
# # stng=input("enter five words:")
# # if len(stng)<6:
# #     print("re enter the chr :")
# # else :
# #       if len(stng)>=6:
# #            print(stng)


    

 
