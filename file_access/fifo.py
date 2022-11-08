# file input and file output

def simpleOutput():
    '''
    Python uses File Access Objects to enable file read/write
    The default is 'text' and 'append' but we can overwrite etc.
    If the file does not exist, python will create it (for 'append')
    '''
    # 'a' will append (or create the file)
    # 't' specifies 'text' (default)
    try: # it is a really good idea to use try-except when accessing files
        #  'a' to append, 'w' to (over)write the file, 'x' exclusive access
        # exclusive access throws an exception if the file already exists
        fout = open('output.txt', 'xt') # this will create a File Access Object
        print('here is some content', file=fout)
        fout.close() # tidy up
    except FileExistsError as fe:
        print('Cannot exclusively write: {}'.format(fe))
    except Exception as err:
        print(err)

def simpleInput():
    '''read text back from a file'''
    try: # 'rt' means read text
        fin = open('output.txt', 'rt') # this fails if the file does not exist
        received = fin.read() # read the whole thing
        print(received)
        # tidy up - we no longer need the fin file access object
        fin.close()
    except Exception as err:
        print(err)

def fileWrite(t='default'):
    '''this will write data to a text file in chunks'''
    try:
        fout   = open('mylog.txt', 'at')
        size   = len(t) # size will be the length of the incoming text string
        offset = 0
        chunk  = 24 # here we choose to write 24 characters at a time
        while True:
            if offset > size:
                fout.write('\n') # put a new line character at the end
                break
            else:
                fout.write(t[offset:offset+chunk]) # [start:stop-before]
                offset += chunk # increment by an amount
        fout.close() # close the file access object once the While loop is done
    except Exception as err:
        print(err)

# reading from a file using 'with'
def fileRead(): # we can use 'with' to make a file access object
    with open('mylog.txt', 'rt') as fin: # 'rt' means read text
        retrieved = fin.readlines() # read all the lines into a list
        print(retrieved)
        # no need for fin.close() - when the 'with' ends it will tidy up

if __name__ == '__main__':
    simpleOutput()
    simpleInput()
    fileWrite('here is a lot of text which needs to be writen to an output file called mylog')
    fileRead() # read back all our log file 