# PROJECT CARA SA
# binofit python equivalent
# @author: rcamelo


from scipy.stats import binomtest

def binofit(k,n,alpha = 0.05):
    """
    @param: {k: n° of success in each individual trial, 
             n: n° of individual trials
             alpha: "100(1 - alpha)%" confidence intervals.                     
    }
    @outputs: {phat: list with the expected probabilities
               pci: list of tupples (lower and upper confidence bounds)
    }
    """
    rlist = []
    if type(n) != list:
        n = [n]
    if type(k) != list:
        k = [k]
    if len(k) == len(n):
         for i in range(len(n)):
                r = binomtest(k[i],n[i])
                rlist.append(r)
    elif len(n) == 1:
        for s in k:
            r = binomtest(s,n[0])
            rlist.append(r)
    else:
       print("The first two inputs must match in size.")
    if len(rlist) > 0:
        phat = [r.proportion_estimate for r in rlist]
        pci = [r.proportion_ci(confidence_level=(1 - alpha)) for r in rlist]
        pci = [(low,up) for low, up in pci]
        
        return phat, pci

#r = binomtest(5,55,(1 - 0.05))
#print(r)
binofit([10, 5,6,8,9],55,alpha = 0.05)     