#  import statements


# functions go here

  #checks that ticket name is not blank
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    #if name is not blank, program continues
    if response != "":
      return response

    #if name is blank, show error (& repeat loop)
    else:
      print("Sorry, this can't be blank")
      print()

def int_check(question):
  error = "Please enter your current age"

  valid = False
  while not valid:
    try:
      age = int(input(question))
      if age < 12:
        print("Sorry, You are too young for this movie.")
      elif age >= 130:
        print("This is very old, seems like an error.")
      else:
        return age
    except ValueError:
      print(error)
      print()
    
# ****** Main Routine ******

# set-up dictionarys / lists needed to hold data
name = ""
ticket_count = 0
MAX_TICKETS = 5
profit = 0
age = 0
# ask user if they have used program before & show instructions if nessesary

# loop to get ticket details
#get details...
    # get name (can't be blank)
while MAX_TICKETS != ticket_count:
  name = not_blank("Name: ")

  # get age (between 12-130)

  if name == "xxx":
    print("You have sold {} tickets.  \n"
          "There are {} places still avaliable. \n"
          "Profit from Tickets: ${:.2f}"
      .format(ticket_count, MAX_TICKETS - ticket_count, profit))
    break
  elif ticket_count == MAX_TICKETS - 1:
    ticket_count += 1
    age = int_check("Age: ")
    print("You have sold all the avalible tickets!")
    print()
  else:
    age = int_check("Age: ")
    ticket_count += 1
    print("You have {} seats "
          "left".format(MAX_TICKETS - ticket_count))

  if age < 16:
    ticket_price = 7.5
  elif age >= 65:
    ticket_price = 6.5
  else:
    ticket_price = 10.5
    
  profit_made = ticket_price - 5
  profit += profit_made
  if name == "xxx":
    continue
  else:
    print("{} : ${:.2f}".format(name, ticket_price))
  print()


  # calculate ticket prices

  # loop to ask for snacks
  
  # calculate snack price
  
  # ask for payment method (and apply surcharge if nessesary)


# calculate total sales and profit

#output data to text file
