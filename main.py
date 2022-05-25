#  import statements


# functions go here

  #checks that ticket name is not blank
def not_blank(question, error_message):
  valid = False

  while not valid:
    response = input(question)

    #if name is not blank, program continues
    if response != "":
      return response

    #if name is blank, show error (& repeat loop)
    else:
      print(error_message)

# ************ Main Routine ************

# set-up dictionarys / lists needed to hold data

# ask user if they have used program before & show instructions if nessesary

# loop to get ticket details

  # get name (can't be blank)
name = not_blank("Name: ", "Sorry, This can't be blank, please enter your name")
  
  # get age (between 12-130)
  
  # calculate ticket prices
  
  # loop to ask for snacks
  
  # calculate snack price
  
  # ask for payment method (and apply surcharge if nessesary)


# calculate total sales and profit

#output data to text file
