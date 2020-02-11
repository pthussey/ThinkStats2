import thinkstats2

hist = thinkstats2.Hist([1,2,2,3,5])

def mode_func(d):
    '''
    d =  a hist defined in thinkstats module
        Finds the mode using Freq method of Hist
    '''
    mode = 0
    for x in d:
        if  d.Freq(x) > mode:
            mode = x
        else:
            continue
    print(mode)

mode_func(hist)