#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPLv3

import sys
import os
import math
import io

def shannon_entropy(data, iterator=None):
    """
    Borrowed from http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
    """
    if not data:
        return 0
    entropy = 0

    if iterator==None:
        SET=""
        for i in range(0,255):
            SET+=chr(i)

    for x in (ord(c) for c in iterator):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

thresshold = 4.5

filename=sys.argv[1]
#fp = open(filename)
fp = io.BufferedReader(io.FileIO(filename,'rb'))

start = int(sys.argv[2])
l = int(sys.argv[3])
flen=os.stat(filename).st_size
if flen == 0:
    flen=int(sys.argv[4])

while True:
	if i <= flen:
		fp.seek(start,0)
		data = fp.read(l)

		e = shannon_entropy(data)

		#print data.encode('hex'),e
 
		if e > thresshold:
		    print data.encode('hex'),e
		i += 1
	else:
		break

	
