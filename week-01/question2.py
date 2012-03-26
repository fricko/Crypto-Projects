"""
The PRG described below uses a 56-bit secret seed. Running the program generates the following first nine outputs of the PRG:
output #1: 210205973
output #2: 22795300
output #3: 58776750
output #4: 121262470
output #5: 264731963
output #6: 140842553
output #7: 242590528
output #8: 195244728
output #9: 86752752

Show that this PRG is insecure by computing the next output. What is the next output (output #10) of the PRG? Note that you are not given the seed.

Hint: there is an algorithm that takes time approximately 2^28 to predict the next output.
"""
import random
import os
import sys

KEY = 295075153

class WeakPrng(object):
    def __init__(self, p):   # generate seed with 56 bits of entropy
        self.p = p
        self.x = random.randint(0, p)
        self.y = random.randint(0, p)

    def set_state(self, x, y):
        self.x = x
        self.y = y
   
    def next(self):
        # x_{i+1} = 2*x_{i}+5  (mod p)
        self.x = (2*self.x + 5) % self.p

        # y_{i+1} = 3*y_{i}+7 (mod p)
        self.y = (3*self.y + 7) % self.p

        # z_{i+1} = x_{i+1} xor y_{i+1}
        return (self.x ^ self.y)

if __name__ == "__main__":

    ref_output = [210205973,
                   22795300,
                   58776750,
                  121262470,
                  264731963,
                  140842553,
                  242590528,
                  195244728,
                  86752752 ]

    prg = WeakPrng(KEY)

    for x in xrange(KEY + 1):
        y = x ^ ref_output[0]

        prg.set_state(x, y)
        test_out = [prg.next()]
        if test_out[0] == ref_output[1]:
            test_out.extend([prg.next() for z in range(8)])
            print ("POTENTIAL\n=========")
            print ("x = %d, y= %d" % (x,y))
            print test_out
            
            if test_out[1:-1] == ref_output[2:]:
                print "DONE!"
                break

    print "complete"
    
    
    
