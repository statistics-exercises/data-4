import numpy as np

# This loads the data that we are going to investigate
x = np.loadtxt("data.dat")

def numberLessThan( y, a ) : 
  # Your code goes here
   
def fractionMoreThan( y, a ) : 
  # Your code goes here
  
def percentageBetween( y, a, b ) : 
  # Your code goes here
  
def percentageOutside( y, a, b ) : 
  # Your code goes here
  
  
# This code is here to test your functions
print("The number of data points less than 0 is", numberLessThan( x, 0 ) )
print("The fraction of data points more than -1 is", fractionMoreThan(x, -1) )
print(percentageBetween(x, -1, 1 ), "percent of the data is between -1 and 1" )
print(percentageOutside(x, -0.5, 0.5 ), "percent of the data is not between -0.5 and 0.5")

