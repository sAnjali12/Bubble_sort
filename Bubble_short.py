list_name = [-2,45,0,11,-9]
index = 0
while index<len(list_name):
    j  = 0
    while j<len(list_name)-1:
        if list_name[j]>list_name[j+1]  :
            list_name[j],list_name[j+1] =list_name[j+1],list_name[j]
        j = j+1
    index = index+1
print list_name


