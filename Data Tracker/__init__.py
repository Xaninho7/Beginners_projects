import time
import os


def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)

    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line


if __name__ == '__main__':

    logfile = open("run/foo/access-log", "r")
    loglines = follow(logfile)
    # iterate over the generator
    for line in loglines:
        print(line)

'''
https://medium.com/@aliasav/how-follow-a-file-in-python-tail-f-in-python-bca026a901cf
'''