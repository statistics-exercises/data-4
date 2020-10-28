import unittest
from main import *

class UnitTests(unittest.TestCase) :
   def test_less_than(self) : 
       delx = ( max(x) - min(x) ) / 10
       for i in range(11) :
         nv, targ = 0, min(x) + i*delx
         for d in x :
            if d<=targ : nv = nv + 1
         self.assertTrue( np.abs( numberLessThan(x, targ)-nv) < 1e-8, "Your function for generating the number of values less than a particular target is incorrect." )
   
   def test_more_than(self) : 
       delx = ( max(x) - min(x) ) / 10
       for i in range(11) :
          nv, targ = 0, min(x) + i*delx
          for d in x :
             if d>=targ : nv = nv + 1
          self.assertTrue( np.abs( fractionMoreThan(x, targ) - nv/len(x) ) < 1e-8 , "Your function for generating the fraction of values more than a particular target is incorrect.")

   def test_between(self) : 
       delx = ( max(x) - min(x) ) / 10
       for i in range(10) :
          nv, targ1, targ2 = 0, min(x) + i*delx, min(x) + (i+1)*delx
          for d in x :
              if d>targ1 and d<targ2 : nv = nv + 1
          self.assertTrue( np.abs( percentageBetween(x, targ1, targ2) - 100*nv/len(x) ) < 1e-8, "Your function for generating the percentage of values more than are within a particular range is incorrect."  )
   
   def test_outside(self) : 
       delx = ( max(x) - min(x) ) / 10
       for i in range(10) :
          nv, targ1, targ2 = 0, min(x) + i*delx, min(x) + (i+1)*delx
          for d in x :
              if d>targ1 and d<targ2 : nv = nv + 1
          self.assertTrue( np.abs( percentageOutside(x, targ1, targ2) + 100*nv/len(x) - 100 ) < 1e-8, "Your function for generating the percentage of values more than are outside a range is incorrect." )
