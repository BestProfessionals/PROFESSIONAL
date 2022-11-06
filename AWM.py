import os, sys

try:

    __import__("aw").Main()

except Exception as e:

    exit(str(e))
