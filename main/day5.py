def coffee_bot():
  print('Welcome to the cafe!')
 
  size = get_size()  
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input("Can I get your name please \n")
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n")

  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_size()
  
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
 
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return 'latte'
  else:
    return get_drink_type()

coffee_bot()