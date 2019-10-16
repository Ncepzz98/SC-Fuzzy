import numpy

#===================== IPK ========================

ipk_low = []
ipk_mid = []
ipk_high = []

for i in numpy.arange(0,2.1,0.1):
    i = round(i, 2)
    ipk_low.append(i)

for i in numpy.arange(1,4.1,0.1):
    i = round(i, 2)
    ipk_mid.append(i)

for i in numpy.arange(3,4.1,0.1):
    i = round(i, 2)
    ipk_high.append(i)

#==================== TOEFL =======================

toefl_low = []
toefl_mid = []
toefl_high = []

for i in numpy.arange(300,461,1):
    i = round(i, 2)
    toefl_low.append(i)

for i in numpy.arange(380,601,1):
    i = round(i, 2)
    toefl_mid.append(i)

for i in numpy.arange(530,631,1):
    i = round(i, 2)
    toefl_high.append(i)

#====================== TPA ======================

tpa_low = []
tpa_mid = []
tpa_high = []

for i in numpy.arange(0,301,1):
    i = round(i, 2)
    tpa_low.append(i)

for i in numpy.arange(150,601,1):
    i = round(i, 2)
    tpa_mid.append(i)

for i in numpy.arange(450,751,1):
    i = round(i, 2)
    tpa_high.append(i)


