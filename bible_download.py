#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 00:14:57 2024

@author: isaacfoster
"""

import os

#bg2md -b -c -e -r -v NIV "Jn 3.16-17" > passage.md

def example_download():
    options     = "-b -c -e -f -v"
    book_abbrev = "GEN"
    chapter     = 1
    reference   = book_abbrev+" "+str(chapter)
    version     = "NASB"
    file        = "Genesis1.md"
    
    def download_bible(options,version,reference,file):
        initial = "ruby bg2md.rb "
        
        execute = initial+options+" "+version+" \""+reference+"\" > "+file
        
        os.system(execute)
        print(execute)
        
    download_bible(options,version,reference,file)

example_download()