0#  import statements


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
name = ""
count = 0
MAX_TICKETS = 5
  
  #get details...
while MAX_TICKETS >= count:
  name = input("Name: ")
  count += 1
  print()

  if name == "xxx":
    print("You have sold {} tickets.  \n"
      "There are {} places still avaliable"
      .format(count, MAX_TICKETS - count))
  elif count == MAX_TICKETS:
    print("You have sold all the avalible tickets!")
  else:
    print("You have {} seats "
          "left".format(MAX_TICKETS - count))
  # get name (can't be blank)
#name = not_blank("Name: ", "Sorry, This can't be blank, please enter your name")
  
  # get age (between 12-130)
  
  # calculate ticket prices
  
  # loop to ask for snacks
  
  # calculate snack price
  
  # ask for payment method (and apply surcharge if nessesary)


# calculate total sales and profit

#output data to text file
