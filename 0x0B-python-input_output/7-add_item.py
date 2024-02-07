#!/usr/bin/python3
"""add item module"""
from sys import argv
saveJSON = __import__("5-save_to_json_file").save_to_json_file
loadJSON = __import__('6-load_from_json_file').load_from_json_file


fname = 'add_item.json'
mlist = []
try:
    mlist = loadJSON(fname)
except Exception:
    saveJSON(mlist, fname)

if len(argv) > 1:
    for i in range(1, len(argv)):
        mlist.append(argv[i])
        
    saveJSON(mlist, fname)

