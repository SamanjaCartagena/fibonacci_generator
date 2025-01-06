# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:55:12 2025

@author: c.samanja09
"""
from typing import Generator

def fibinacci_generator() ->Generator[int, None, None]:
    a,b =0,1
    while True:
        yield a
        a,b = b,(a +b)
        
def main() ->None:

    fib_gen:Generator[int,None,None] =fibinacci_generator()
    n:int =10
    line_break:str ='-'*20
    
    while True:
        input(f'Tap "enter" for the next {n} numbers of fibonacci generator')
        for i in range(n):
            print(f'{next(fib_gen)}')
            
        print(line_break)

if __name__=='__main__':
    main()