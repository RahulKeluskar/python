#!/usr/bin/env python3
'''
Module to analyze the flow of the debugger in pyton
'''

import pdb
filename = __file__
# Note : __file__ returns the file name of the file calling the function

pdb.set_trace()
print(f'The file name is {filename}')
