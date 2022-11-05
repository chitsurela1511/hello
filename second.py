#map
# map(fuction,iter(list,tuple,set,dicionary))

# def multiply(num):
#     return num*num
#  #result=map(multiply,[2,4,6,8]) #lamda var:return
# result=map(lambda i:i+1,[2,4,6,8]) #lamda var:return
# print(list(result))

# def toUpper(str):
#     return str.upper()
# res=map(toUpper,("software","sem","3"))
# print(list(res))

# newlist=list(res)
# newlist.append("hey")
# print(newlist)


dict_item={"a":"car","b":"Bike","c":"Train"}
b=map(lambda i:(i[0],i[1]+"s"),dict_item.items())
print(dict(b))
k=map(lambda i:i+"key",dict_item.keys())
print(list(k))