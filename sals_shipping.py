premium_ground_shipping = 125.0
def ground_shipping(weight):
  if weight <= 2 :
    cost = weight * 1.5 + 20.0
  elif weight > 2 and weight <= 6 :
    cost = weight * 3.0 + 20.0
  elif weight >6 and weight <= 10 :
    cost = weight * 4.0 + 20.0
  else :
    cost = weight * 4.75 + 20.0
  return cost

def drone_shipping (weight):
  if weight <= 2 :
    cost = weight * 4.50
  elif weight > 2 and weight <= 6 :
    cost = weight * 9.00
  elif weight >6 and weight <= 10 :
    cost = weight * 12.00
  else :
    cost = weight * 14.25
  return cost

def cheapest_shipping_method (weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping :
    message = "Ground shipping is the cheapest\n" + "The cost is " + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping :
    message = "Drone shipping is the cheapest\n" + "The cost is " + str(drone_shipping(weight))
  else :
    message = "Premium ground shipping is the cheapest\n " + "The cost is " + str(premium_ground_shipping)
  return message
  
print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))
