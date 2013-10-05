f = open('x-acc.csv')
accs = []
for line in f:
	cols = line.split(',')
	acc = float(cols[1])
	accs.append(acc)
f.close()
n = len(accs)
t = [t*2.0/n for t in range(n)]

import matplotlib.pyplot as plt

#plt.plot(t, accs)
#plt.show()

import scipy.signal
b, a = scipy.signal.butter(4, 0.05, 'low')
output_signal = scipy.signal.filtfilt(b, a, accs)
output_signal[len(output_signal)-10:len(output_signal)] = 0

plt.plot(t, output_signal)
plt.show()