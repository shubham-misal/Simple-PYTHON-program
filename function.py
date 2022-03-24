def operationd():
  try:
    num_ber=input("Enter a number ==>")
    if(num_ber !=None):
      st_nm = int(num_ber)
      if(st_nm % 2 == 0):
        print(st_nm, " is a Even number")
      elif(num_ber == None):
        print("No input from user")
      else:
        print(st_nm, " is a Odd Number")
    else:
      print("Invalid Input")
  except ValueError:
    txt = (num_ber.isalpha())
    if(txt == True):
      print(num_ber, " is a String")
    else:
      print(num_ber, " is not a number")