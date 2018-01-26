#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:59:46 2018

@author: kyle
"""
offspring_num = {'Q': 1, '*': 2, '+': 2, '-': 2, '/': 2, 'a': 0, 'b': 0, 'c': 0, 'd': 0}


class FilterNode:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class BinaryTree:
    '''
    This class accesses a string and decode it into a tree.
    Notice that the string should be the post_order traverse of a binary tree.
    So the __init__ function directly tranforms the string into an output result.
    And the next step is to get
    '''

    def __init__(self, chromosome):
        self.root = FilterNode(chromosome[0])
        queue = [self.root]

        generator = self.get_char_from_string(chromosome)
        next(generator)

        for i in queue:
            for j in range(offspring_num[i.value]):
                current_node = FilterNode(next(generator))
                queue.append(current_node)
                i.add_child(current_node)

    def get_char_from_string(self, string):
        for i in string:
            yield i
