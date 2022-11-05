# 1. Triple All the number given list:
# import math 
# num=[2,3,4,5,6]
# def listTripler(item):
#     return math.floor(math.pow(item,3))
# resultList=list(map(listTripler,num))
# print(resultList)
#------------------------------------------------
#2 Sparate even odd number from given list.
# nums =[0,1,2,3,4,5,6,7,8,9,10] 
# def evenlist(i):  
#     if(i%2==0):
#         return i
# def oddList(i):
#     if(i%2!=0):
#         return i
# evenNumbers=list(filter(lambda x:x,map(evenlist,nums)))
# oddNUmbers=list(filter(lambda x:x ,map(oddList,nums)))

# print("Odd numbers:{0}",format(oddNUmbers))
# print("even numbers:{0}",format(evenNumbers))
#--------------------------------------------------------
#3.print all string in lower case from given tuple
# from ten import Course


# Course=("SOFTWARE","ITIMS","DD","ANIMATION")
# output=tuple(map(lambda i:i.lower(),Course))
# print(output)
#--------------------------------------------------
#4 print square root of numbers given list:
# import math


# l3=[24,36,64,25]
# output=list(map(lambda i:math.sqrt(i),l3))
# print(output)
#---------------------------------------------------------
#5 Elimate duplicate letter from giving string
# import re
# import string


# string=""
# str="hello world hello"
# def findDuplicate(i):
#     global string
#     if re.search(i,string)==None:
#      string  += i
# ans=map(findDuplicate,str)
# print(list(ans))
# print("String with unique charachters:",string)
#-------------------------------------------------------------------
#6 print table of any number:
# number=int(input("Enter a table for multiplication  table:"))
# l=int(input("Enter limit till you want to print table:"))

# def multiples(i):
#     return number*i
# limitList=[]
# for i in range(1,l+1):
#     limitList.append(i)
# res=list(map(multiples,limitList))
# print("multiplication table is",res)
#---------------------------------------------------------------------
#7 add two list:
# nums1=[1,2,3,]
# nums2=[4,5,6]
# result=map(lambda x,y:x+y,nums1,nums2)
# print("Result : after adding two list:")
# print(list(result))    
#--------------------------------------------------------------------
#8 float digit to integer using funcation..
# l=[2.5,2.4,3.8]
# newlist=list(map(lambda i:int(i),l ))
# print(newlist)
#----------------------------------------------
#10 gmail convert to in lower case:
names={'a':'anna','b':'bharat','c':'carlo','d':'dim'}
gmail= dict(map(lambda x:(x[0],x[1]+'@gmail.com'),names.items()))
print(gmail)


