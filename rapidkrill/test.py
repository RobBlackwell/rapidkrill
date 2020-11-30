#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
from echolab2.instruments import EK80
from echolab2.plotting.matplotlib import echogram

ek80 =EK80.EK80()
ek80.read_raw('/home/reb/data/external/aker/2019828-D20190123-T151225.raw')

Sv = ek80.raw_data[ek80.channel_ids[0]][0].get_Sv()

fig = plt.figure()
echogram_2 = echogram.Echogram(fig, Sv)
plt.savefig('echogram.png')

print("hello")
