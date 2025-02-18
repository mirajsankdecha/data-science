list1 = ["Hi","Hello","kem cho"]
list2 = [20,90,40]

dict1 = dict(zip(list1,list2))
print(dict1)

dic = {}
for key in list1:
    for value in list2:
        dic[key] = value
        list2.remove(value)
        break
print(dic)
