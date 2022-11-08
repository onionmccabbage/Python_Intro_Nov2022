# file input and output using bytes

# we need some bytes to work with
b = bytes( range(0,255) ) # start at 0, stop-before 255 gives us 255 values
print(b) # we can see the actual byte codes...

def writeBytes():
    ''' write some byte data to a file'''
    try: # we can invent a file called 'bfile'
        fout = open('bfile', 'wb') # 'w' to (over)write 'b' means bytes
        fout.write(b) # commit our byte data to this byte file
        fout.close()
    except Exception as err:
        print(err)

def readBytes():
    '''read back some bytes from a file'''
    try:
        fin = open('bfile', 'rb') # 'r' to read 'b' for bytes
        r = fin.read()
        fin.close()
        print(r) # here we just print the retrieved bytes
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writeBytes()
    readBytes()