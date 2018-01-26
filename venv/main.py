#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:55:42 2018

@author: kyle
"""


from binarytree import BinaryTree

if __name__ == "__main__":
    test_strings = ["Q*-+abcd","Q*b**+baQba",
                    "*b+a-aQab+//+b+babbabbbababbaaa"]
    for i in test_strings:
        test_tree = BinaryTree(i)
        for ch in test_tree.root.depth_first():
            print(ch)
        print()
    
        
        