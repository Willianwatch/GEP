#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:00:04 2018

@author: kyle
"""
import math


class Functions:
    '''
    This class stores some symbolic functions inside.
    '''
    def __init__(self):
        self.functions={'1':lambda x:x*x,
                        '2':lambda x:math.log(x),
                        '3':lambda x:math.exp(x),
                        '4':lambda x:math.sin(x),
                        '5':lambda x,y:x+y,
                        '6':lambda x,y:x-y,
                        '7':lambda x,y:x*y,
                        '8':lambda x,y:x/y
                        }

        
if __name__ == "__main__":
    functions_set = Functions()
    function = functions_set.functions['3']
    print(function(4))