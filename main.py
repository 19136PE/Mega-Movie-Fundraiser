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


def int_check(question, low_num, high_num):
  error = "Please enter a whole number between {} and {}".format(low_num, high_num)
  empty_int = "Sorry, this cannot be blank"

  valid = False
  while not valid:
    try:
      response = int(input(question))
      if low_num <= response <= high_num:
        return response
      else:
        print(error)
        print()

    except ValueError:
      print(empty_int)
      print()


# ************ Main Routine ************

# set-up dictionarys / lists needed to hold data

# ask user if they have used program before & show instructions if nessesary

# loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5
  
  #get details...
while MAX_TICKETS != count:
  name = not_blank("Name: ")

  # get age (between 12-130)
  age = int_check("Age: ", 12, 130)

  if name == "xxx":
    print("You have sold {} tickets.  \n"
      "There are {} places still avaliable"
      .format(count, MAX_TICKETS - count))
  elif count == MAX_TICKETS - 1:
    count += 1
    print("You have sold all the avalible tickets!")
  else:
    count += 1
    print("You have {} seats "
          "left".format(MAX_TICKETS - count))
    print()
  # get name (can't be blank)

  # calculate ticket prices
  
  # loop to ask for snacks
  
  # calculate snack price
  
  # ask for payment method (and apply surcharge if nessesary)


# calculate total sales and profit

#output data to text file
