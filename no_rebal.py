from math import log

import numpy as np

epsilon = 1e-8

t = np.zeros((1111, 4), np.float32)
p = np.zeros((1111, 4), np.float32)

for i in range(0, 0 + 1):
    t[i, 0] = 1.0
for i in range(1, 1 + 10):
    t[i, 1] = 1.0
for i in range(11, 11 + 100):
    t[i, 2] = 1.0
for i in range(111, 111 + 1000):
    t[i, 3] = 1.0

p = np.clip(p, epsilon, 1.0)
for i in range(1111):
    p[i, 0] = 1.0


loss = 0

for i in range(1111):
    for j in range(4):
        # print('t[{}, {}]: {}'.format(i, j, t[i, j]))
        # print('p[{}, {}]: {}'.format(i, j, p[i, j]))
        delta = -t[i, j] * log(p[i, j])
        # print('delta: ' + str(delta))
        loss += delta

print('loss: ' + str(loss))
print('mean loss: ' + str(loss/1111))
