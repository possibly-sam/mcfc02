import random
import math
import numpy


def collapse(b,e,w,p) :
    if p == None: return 0;
    if e < b or w < e: return 0;
    if p/100 < random.random():  return 0;

    mu = (b + 4*e + w)/6
    sd = (mu-b)*(w-mu)
    sd = abs(sd)/7
    sd = math.sqrt(sd)

    return int(round(random.normalvariate(float(mu),float(sd))))

def collapsevector(b_, e_, w_, p_) :
    # require b_length == e_.length etc.
    return sum(list(map(lambda k: collapse( b_[k], e_[k], w_[k], p_[k]  ),
        range(len(b_)))))


def collapsevectorsample(b_, e_, w_, p_, numberofsamples=0) :
    # require b_length == e_.length etc.
    max_samples = len(b_)
    if numberofsamples==0:  numberofsamples=max_samples;

    if numberofsamples < max_samples:
        ix = numpy.random.choice(max_samples,  numberofsamples, False)
        b_ = [ b_[k] for k in ix ]
        e_ = [ e_[k] for k in ix ]
        w_ = [ w_[k] for k in ix ]
        p_ = [ p_[k] for k in ix ]

    return round(max_samples*collapsevector(b_, e_, w_, p_)/numberofsamples);


def collapse_many(b_, e_, w_, p_, number_of_times=1, numberofsamples=0) :
    return [ collapsevectorsample(b_, e_, w_, p_, numberofsamples)  for k in range(number_of_times)  ]



b0 = [0,0, 1]
e0 = [1,1,2]
w0 = [2,3,5]
p0 = [8,13, 21]

def test_collapse():
    return collapse(b0,e0,w0,p0)


samplereturn = [ (101, 0, 1, 5,    90),
                 (102, 1, 2, 8,    80),
                 (103, 1, 3, 13,   70),
                 (104, 2, 5, 21,   60),
                 (105, 3, 8, 34,   50),
                 (106, 5, 13, 55,  40),
                 (107, 8, 21, 89,  30),
                 (108, 13,34, 144, 20),
                 (109, 21,55, 233, 10)]




# for k in range(len(samplereturn))  : print( samplereturn[k][2])

#map( lambda it: it[2], samplereturn)