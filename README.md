<h1 align="center">
 <img src="https://cdn-icons.flaticon.com/png/128/3098/premium/3098090.png?token=exp=1648104783~hmac=6bb69e4a3952cea9d0f522565832b2e6" alt="PYTHON"><br>
  # Simple-PYTHON-program
</h1><br>
A simple python program for finding the entered value is string,integer or invalid ==>
<a href="https://stackoverflow.com/questions/71574665/in-python-if-the-user-enters-a-string-instead-of-number-integer-value-then-ho" target="_blank"> Question on Stack-Overflow</a>
<pre>
#actual file code ==> evenodd1.py

<i>
# Calling function from another file
from function import*

print("================== < Get Even or Odd Number > ==================")
operationd()
print("================== < Get Even or Odd Number > ==================")
</i>

#actual file code
</pre>
<pre>
#Code of file where function is there ==> function.py
<i>
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
</i>

#Code of file where function is there 
</pre>
<h1><i>#OUTPUT</i></h1>
<img src="https://github.com/shubham-misal/Simple-PYTHON-program/blob/main/outputcc.png" alt="output">
