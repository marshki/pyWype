## pyWipe

A text-based tool to securely wipe hard drives written to work with Python 2 & 3.

*diskWipe.py* works as is in Python 2.7 
The idea here is to enhance the program in Python 2.7 first, then add support for Python 3.4. Eventually, it would be nice if this program could functionally do what OS X's Disk Utility--secure erase option--does: 

![Alt text](https://github.com/marshki/pyWipe/blob/master/secure_erase.png?raw=true "Disk Utility--secureErase")


 
Still early in development. **PROCEED WITH CAUTION**

TODO: 
- [x] Detect attached devices 
- [x] Define block device(s) to be wiped  
- [x] Define number of wipes 
- [x] Confirm wipe 
- [x] Zeros to drive 
- [x] Random to drive 
- [x] Wipe drive 
- [ ] Unit tests 
- [ ] Python 2 & 3 
- [ ] Menu 
- [ ] Argument parsing for CLI action 
- [ ] Investigate various wiping algorithms 
- [ ] More stuff I can't think of ATM 
