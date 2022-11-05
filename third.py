# Filter




# example 1

# numbers=[1,2,3,4,5,6,7,8,9,10]
# # return true if numbers is even
# def check_even(number):
#     if number %2==0:
#         return True
#     return False

# even_numbers_iterator = filter(check_even,numbers)
# # converting to list
# even_numbers =list (even_numbers_iterator)
# print(even_numbers)

# example 2

# letters =['a','b','c','d','e','i','j','o']
# def filter_vowels (letter):
#     vowels=['a','e','i','o','u']
#     return True if letter in vowels else False
# filter_vowels =filter (filter_vowels,letters)
# vowels =tuple(filter_vowels)
# print(vowels)

#example 3:

# numbers =[1,2,3,4,5,6,7]
# even_nubers_itertor = filter(lambda x:(x%2==0),numbers)
# even_numbers =list(even_nubers_itertor)
# print(even_numbers)

# tkinter
import tkinter
m=tkinter.Tk()
# widget are added here...
m.mainloop()
