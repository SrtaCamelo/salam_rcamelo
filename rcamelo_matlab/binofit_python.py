# PROJECT CARA SA
# binofit equivalence test (matlab I/O generator)
# @author: rcamelo
# @param: {x: n° of success in each individual trial, 
#          n: n° of individual trials
#          alpha: "100(1 - alpha)%" confidence intervals. (optional)                     
#         }
# output file name: binofit_matlab_out.txt

#  Generate random binomial samples (successes, trials)

from scipy.stats import binomtest

def binofit_cara(k,n,alpha = 0.05):
    if len(k) > 1:
        if len(k) == len(n):
            pass
        elif len(n) == 1:
            pass
        else:
            print("Error")
    else:
        r = binomtest(k,n,(1 - alpha))
#r = binomtest(100,0.6);
[phat,pci] = binomtest(r,100)