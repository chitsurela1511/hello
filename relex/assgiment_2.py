# 1.

# list1=[-1,2,4,-5,6,-13,12,22,-14,-18,20,3]
# list2=list(filter(lambda x:x>0,list1))
# print(list2)


# 2.using filter function filter the even numbers so that only odd numbers are passed to the new list

# list1=[1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35]
# print(list1)
# list2=list(filter(lambda x:x%2!=0,list1))
# print(list2)


# 3.using filter() and list() functions and .lower() method filter all the vowels in a given string

# str="When you have a dream, you've got to grab it and never let go."
# list1 = list(filter(lambda x: True if x.lower() in "aeiou" else False, str))
# print(list1)


# 4.This time using filter() and list() functions filter all the positive integers in the string.

# str=" Faulkner's Absalom, Absalom! (1936) contains a sentence
#  composed of 1,288 words (in the 1951 Random House version)."
# list1 = list(filter(lambda x: True if x in "0123456789" else False, str))
# print(list1)


# 5.Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.
# list1=[10,-20,-30,-40,50,-60,-80,90,70,100,-120,-130,-140]
# list2 = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, list1)))
# print(list2)