
id = ["12r34t","12j123","12j123","13uda7","14ghjt5","14ghjt5","14ghjt5"]
list1 = []
list2 = []
for each in id:
    print(id.count(each))
    if id.count(each) == 1:
        list1.append(each)
    if id.count(each) == 2:
        list1.append(each)
        list2.append(each)
print(set(list1),set(list2))