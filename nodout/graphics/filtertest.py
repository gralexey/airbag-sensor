
from os import sys
filename = ''
if len(sys.argv)==2:
	filename = sys.argv[1]

if filename == '':
	print "no filename given"	
	exit(-1)


f = open(filename)
f.readline()

accs = []
for line in f:
	acc = float(line)
	accs.append(acc)
f.close()
n = len(accs)
t = [t*2.0/n for t in range(n)]
import matplotlib.pyplot as plt

plt.plot(t, accs)
plt.show()
exit(0)

import scipy.signal
b, a = scipy.signal.butter(4, 0.05, 'low')
output_signal = scipy.signal.filtfilt(b, a, accs)
output_signal[len(output_signal)-10:len(output_signal)] = 0

plt.plot(t, output_signal)
plt.show()