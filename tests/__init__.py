import os
import sys

# check current paths available
# for p in sys.path: print(p)

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"xetra"
)
sys.path.append(SOURCE_PATH)