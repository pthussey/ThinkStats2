import thinkstats2

hist = thinkstats2.Hist([1,2,2,3,5,2,1,5,5,5,5])

def all_mode_func(d):
    '''
    d =  a hist defined in thinkstats module
        Finds the mode using Freq method of Hist
    '''
    modes = []
    for x in d:
        modes.append((x, d.Freq(x)))
        modes.sort(key = lambda x : x[1], reverse=True)
    return modes

print(all_mode_func(hist))