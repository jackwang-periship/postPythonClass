'''
Created on Jun 4, 2018

@author: jwang02
'''
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

def main():

    cpv = os.environ["PATH"]
    pp.pprint(cpv.split(';'))

if __name__ == '__main__':
    main()
    