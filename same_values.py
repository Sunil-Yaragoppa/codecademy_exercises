#Write your function here
def same_values(lst1,lst2):
  indices = list()
  for x in range(0,len(lst1)):
    if lst1[x] == lst2[x] :
      indices.append(x)
  return indices

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
