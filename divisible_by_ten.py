#Write your function here
def divisible_by_ten(nums):
  nums_new=[num for num in nums if num % 10 == 0]
  return len(nums_new)

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
