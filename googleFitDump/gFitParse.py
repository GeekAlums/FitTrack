#!/usr/bin/python

import sys

def ReadBackEachLine(oneLine):
    text = oneLine.split()
    fo = open('gParsedFile.csv','a')
    for i in range(len(text)):
        fo.write('%s,' %(text[i]))
    fo.write("\n")
    fo.close()

def main():
    SourceFilename = 'googleFit_Dump.csv'
    fileReadObj = open(SourceFilename, 'r')
    for line in fileReadObj:
        ReadBackEachLine(line)
    fileReadObj.close()

if __name__ == '__main__':
  main()
