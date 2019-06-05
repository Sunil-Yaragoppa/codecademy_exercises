def username_generator(first_name,last_name):
  if len(first_name) < 3 or len(last_name) < 4 :
    username = first_name + last_name
  else :
    username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = ''
  for letter in range(0,len(username)):
    password += username[letter-1]
  return password

username = username_generator("Sunil" , "Yaragoppa")

print(password_generator(username))
