pokelist=["bublbasur_21","coco_54","squirtle_142","charamandar_23",'ginger_142',"gee_42","ghost_45"]
l2=[]
# for i in pokelist[::-1]:
#     print(i[:-3])
    #output=only name but contain _ with squirtle 
#for i in pokelist:   #if we put[::2] it will chise a alternative character 
    # if i[0]=="g":
    #   k=i.find("_")
    #   print(i[:k])
    # k=i.startswith("g")#alternative way to do above statement
    # if k==True:
    #     l1=i.find('_')
    #     print(i[:l1])
    # print(i[-4::-1])
# for poke in pokelist[::2]:
#     print(poke[:-3])
for i in pokelist[::2]:#add the number to a different list from ione list to other 
    l2.append(i)
print(l2)  


