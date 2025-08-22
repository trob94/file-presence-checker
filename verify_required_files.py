#!/usr/bin/env python3

import os

# Check if README.md exists
if not os.path.exists("README.md"):
    print("ERROR: README.md is missing!")
    exit(1)

# Check if .gitignore exists  
if not os.path.exists(".gitignore"):
    print("ERROR: .gitignore is missing!")
    exit(1)

# If we get here, both files exist
print("Success!")
