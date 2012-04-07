# -*- coding: utf-8 -*-
"""
In this assignment your task is to find hash function collisions using the birthday attack discussed in the lecture.

Consider the hash function obtained by truncating the output of SHA256 to 50 bits, say H(x)=LSB50(SHA256(x)), that is we drop all but the right most 50 bits of the output. Your goal is to find a collision on this hash function. Find two strings x≠y such that LSB50(SHA256(x))=LSB50(SHA256(y)) and then enter the hex encoding of these strings in the fields below.

For an implementation of SHA256 use an existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other.
"""

from Crypto.Hash import SHA256
import math


def last_n_bits(n, hex_str):
    num_bytes = (n // 4) + 1
    bin_val = bin(int(hex_str[-num_bytes:], base=16))[2:]
    bin_val = bin_val[-n:].zfill(n)
    return int(bin_val, base=2)

def find_collisions(num_bits, test_hash_func):
    # executes a birthday attack on the chosen hash, assuming you're only using
    # the last num_bits bits of the digest
    results_dict = {}
    rv = ()
    
    for n in xrange(2 ** 30):        
        if not n % 2 ** 20 and n:
            print '2 ^ %d' % (math.log(n, 2))
            
        test_hash = test_hash_func.new(str(n))        
        bits = last_n_bits(num_bits, test_hash.hexdigest())

        if bits in results_dict:
            return (results_dict[bits], n)
        else:
            results_dict[bits] = n

if __name__ == "__main__":
    print find_collisions(50, SHA256)
    
