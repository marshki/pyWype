## pyWipe

A text-based Python tool to securely wipe hard drives and partitions in Linux. 
Tested to work in Python 2.7 & 3.4. 

*diskWipe.py* works as is in Python 2.7 
*pyWypeRemix.py* works as is in Python 2.7 & 3.4 

PROCEED WITH CAUTION. THIS WILL IRRECOVERABLY WIPE DATA FROM YOUR DISK.  
Still early in development.

Open New Issues for: 

- [] dd: error wiritng '/dev/sdb': No space left on device 
- [] dd: writing to 'standard output': Broken pipe 

TODO: 
- [x] Detect attached devices 
- [x] Define block device(s) to be wiped  
- [x] Define partition(s) to be wiped 
- [x] Define number of wipes 
- [x] Confirm wipe 
- [x] Zeros to drive 
- [x] Random to drive 
- [x] Wipe drive
- [ ] Quit at any time option 
- [ ] Support multiple drive wipes 
- [ ] Unit tests and integration with [Travis CI](https://travis-ci.org/)  
- [x] Python 2 
- [X] Python 3
- [x] Menu 
- [ ] Argument parsing for CLI action 
- [ ] OS X compatibility? Can we ammend this to run in both Linux and OS X? 
- [ ] Investigate various wiping algorithms 
- [ ] More stuff I can't think of ATM 
