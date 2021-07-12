list1=['1','2','3']
for i in list1:
  {
    print(i)
  }
list2=['4','5','6']
list1.extend(list2)
print("after extending")
for i in list1:
  print(i)
