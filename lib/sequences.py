#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq=[0,1]
    
    while len(fib_seq) < length:
        next_fib= fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
    print(fib_seq[:length])