
def hexstr2intarray(hexstr):
    return [eval("0x" + hexstr[x:x+2])
                           for x in xrange(0, len(hexstr), 2)]

def asciistr2intarray(asciistr):
    return map(ord, asciistr)

def xor_lists(l1, l2):
    return [x[0] ^ x[1] for x in zip(l1, l2)]
