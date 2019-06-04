#Write your function here
def max_num(lst):
  maximum = lst[0]
  for item in lst:
    if item > maximum :
      maximum = item
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
