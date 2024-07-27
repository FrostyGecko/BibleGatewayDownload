#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 00:14:57 2024

@author: isaacfoster
"""

import os
import pandas as pd
from tqdm import tqdm

def BibleGatewayReference_example_download():
    # '''
    # Option | Option (longer form) | Meaning
    # --------- | ------------ | ---------------------------------
    # -b | --boldwords  |  Make the words of Jesus be shown in bold
    # -c | --copyright  |  Exclude copyright notice from output
    # -e | --headers |  Exclude editoria l headers from output
    # -f | --footnotes  |  Exclude footnotes from output
    # -h | --help  | Show help
    # -i | --info |  Show information as I work
    # -l | --newline | Start chapters and verses on a new line that starts with an H5 or H6 heading
    # -n | --numbering  | Exclude verse and chapter numbers from output
    # -r | --crossrefs  |  Exclude cross-refs from output
    # -t | --test FILENAME  | Pass HTML from FILENAME instead of live lookup. 'reference' must still be given, but will be ignored.
    # -v | --version VERSION | Select Bible version to lookup using BibleGateway's abbreviations (default:NET)
    # '''
    
    #bg2md -b -c -e -r -v NIV "Jn 3.16-17" > passage.md
    download_directory = 'ExampleDownload/'
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
        
    options     = "-b -c -e -f -v"
    book_abbrev = "Genesis"
    chapter     = 1
    reference   = book_abbrev+" "+str(chapter)
    version     = "NASB"
    file        = "Genesis1.md"
    path        = download_directory+file
    initial     = "BibleGateway-to-Markdown/bg2md.rb "
    execute     = initial+options+" "+version+" \""+reference+"\" > "+path
    
    os.system(execute)
    
def download_bible(options,version,suffix=""):
    bible_index = pd.read_csv("bible_index.csv")
    books       = list(bible_index.columns)
    books.remove('Chapter')
    
    for book in tqdm(books):
        chapter_verse_count = bible_index[book]
        verse_count         = list(filter(lambda num: num != 0, chapter_verse_count))
        chapter_count       = len(verse_count)
        
        for chapter in range(1,chapter_count+1):
            reference   = book+" "+str(chapter)
            directory   = 'Downloads/'+version+suffix+"/"+book+"/"

            if not os.path.exists(directory):
                os.makedirs(directory)
                
            filename    = reference+'.md'
            path        = directory+filename
            initial     = "BibleGateway-to-Markdown\ruby bg2md.rb "
            
            execute = initial+options+" "+version+" \""+reference+"\" > \""+path+"\""

            os.system(execute)

def BibleGatewayReference(version,
                           book,
                           reference,
                           boldwords    = False,
                           copyright    = False,
                           headers      = False,
                           footnotes    = False,
                           newline      = False,
                           crossrefs    = False,
                           numbering    = True,
                           verbose      = False,
                           **args):
    
    # '''
    # Option | Option (longer form) | Meaning
    # --------- | ------------ | ---------------------------------
    # -b | --boldwords  |  Make the words of Jesus be shown in bold
    # -c | --copyright  |  Exclude copyright notice from output
    # -e | --headers |  Exclude editoria l headers from output
    # -f | --footnotes  |  Exclude footnotes from output
    # -h | --help  | Show help
    # -i | --info |  Show information as I work
    # -l | --newline | Start chapters and verses on a new line that starts with an H5 or H6 heading
    # -n | --numbering  | Exclude verse and chapter numbers from output
    # -r | --crossrefs  |  Exclude cross-refs from output
    # -t | --test FILENAME  | Pass HTML from FILENAME instead of live lookup. 'reference' must still be given, but will be ignored.
    # -v | --version VERSION | Select Bible version to lookup using BibleGateway's abbreviations (default:NET)
    # '''
    
    
    #### Construct Options
    if boldwords is True: opt1 = "-b " 
    elif boldwords is False: opt1 = ""
    
    if copyright is True: opt2 = "" 
    elif copyright is False: opt2 = "-c "
    
    if headers is True: opt3 = "" 
    elif headers is False: opt3 = "-e "
    
    if footnotes is True: opt4 = "" 
    elif footnotes is False: opt4 = "-f "
    
    if newline is True: opt5 = "-l "
    elif newline is False: opt5 = "" 
    
    if numbering is True: opt6 = ""
    elif numbering is False: opt6 = "-n " 
    
    if crossrefs is True: opt7 = ""
    elif crossrefs is False: opt7 = "-r " 
    
    options             = opt1+opt2+opt3+opt4+opt5+opt6+opt7+'-v'
        
    #### Build Reference Markdown File
    reference           = book+" "+reference
    filename            = reference+'.md'
    
    #### Download Directory
    download_folder     = 'Downloads/' 
    downloaddir         = download_folder+version+"/"+book+"/"
    savepath            = downloaddir+filename
    
    #### Check Existance of Download Folder
    try:
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
    except:
        print("ERROR: Unable to create download folder") 
        
    #### Check Existance of Download Directory
    try:
        if not os.path.exists(downloaddir):
            os.makedirs(downloaddir)
    except:
        print("ERROR: Unable to create download directory") 
        
    #### Build Execute Statement
    # Build bg2md.rb file from BibleGateway-to-Markdown directory
    initial             = "BibleGateway-to-Markdown/bg2md.rb "    
    
    # Build complete execution statement
    execute             = initial+options+" "+version+" \""+reference+"\" > \""+savepath+"\""
    
    #### Printing
    def debug(verbose):
        if verbose is True:
            print("Options: "+options)
            print("Download Folder: "+download_folder)
            print("Download Directory: "+downloaddir)
            print("Save Path: "+savepath)
            print("Execute Call: "+execute)     
    
    #### Execute
    try:
        os.system(execute)
        debug(verbose)
        return True
    except:
        print("ERROR: Could not execute bg2md.rb")
        debug(True)
        return False
        

#%% Download Reference

book            = "Genesis"
reference       = "1:1-2:5"
version         = "ESV"

BibleGatewayReference(version,book,reference,crossrefs=True)
