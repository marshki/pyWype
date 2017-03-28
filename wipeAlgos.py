#!/usr/bin/env python 


def singlePassZero(): 
    """ Single-pass zero-fill erase """

    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1

    for int in range(num):
        print 'Processing pass count %s of %d ... '%(passes, num)
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb
        passes += 1

def singlePassRandom(): 
    """ Single-pass random-fill erase """ 

    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1

    for int in range(num):
        print 'Processing pass count %s of %d ...'%(passes, num)
        os.system(('dd if=/dev/random |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb
        passes += 1




 
def usDoD7Pass():
    """ US DoD 7-pass secure erase """ 

def gutmann35Pass(): 
    """ Gutman algorithm 35-pass secure erase """ 

def usDoE3Pass(): 
    """ US DoE algorithm 3-pass secure erase """ 

