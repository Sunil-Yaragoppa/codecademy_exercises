letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters (word) :
  counter = 0
  for i in letters :
    if i in word :
      counter += 1
  return counter
       
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippiiiii"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
