# PROJECT CARA SA
# binofit equivalence test 
# @author: rcamelo
# @param: {x: n° of success in each individual trial, 
#          n: n° of individual trials
#          alpha: "100(1 - alpha)#" confidence intervals. (optional)                     
#         }
# output file name: binofit_python_out.txt

#-------------0.11, 0.23, 0.55, 0,60, 0,90 Expectect Probabilities (in this order)
#-------------0.95 confidence intervals ----------------
from binofit_python import binofit

[phat,pci] = binofit([10, 5,6,8,9],55) 
phat, pci
[phat,pci] = binofit([11, 15,13,12,14],55)
phat, pci
[phat,pci] = binofit([26,33,36,27,37],55)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55)
phat, pci


[phat,pci] = binofit([10, 12, 7 , 8 , 9],100)
phat, pci
[phat,pci] = binofit([25, 32, 26, 23, 18],100)
phat, pci
[phat,pci] = binofit([49, 52, 56, 57, 53],100)
phat, pci
[phat,pci] = binofit([55, 65, 62, 64, 57],100)
phat, pci
[phat,pci] = binofit([95, 90, 88, 89, 92],100)
phat, pci


[phat,pci] = binofit([23,24,34,35,32],256)
phat, pci
[phat,pci] = binofit([65, 62, 66, 56, 47],256)
phat, pci
[phat,pci] = binofit([134, 135, 148, 149, 132],256)
phat, pci
[phat,pci] = binofit([165, 155, 147, 145, 155],256)
phat, pci
[phat,pci] = binofit([224, 231, 227, 238, 236],256)
phat, pci

phat, pci
[phat,pci] = binofit([57, 62, 65 , 53 , 67],500)
phat, pci
[phat,pci] = binofit([120, 124, 122, 117, 118],500)
phat, pci
[phat,pci] = binofit([276, 294, 267, 279, 281],500)
phat, pci
[phat,pci] = binofit([305, 313, 299, 300, 306],500)
phat, pci
[phat,pci] = binofit([445,  455,  448, 456, 449],500)
phat, pci

[phat,pci] = binofit([118,111,110,108,120],1000)
phat, pci
[phat,pci] = binofit([237,202,213,241,229],1000)
phat, pci
[phat,pci] = binofit([532,571,542,529,566],1000)
phat, pci
[phat,pci] = binofit([691,598,580,620,615],1000)
phat, pci
[phat,pci] = binofit([891,894,908,900,895],1000)
phat, pci
#-------------0.99 confidence intervals ----------------
[phat,pci] = binofit([10, 5,6,8,9],55,0.01)
phat, pci
[phat,pci] = binofit([11, 15,13,12,14],55,0.01)
phat, pci
[phat,pci] = binofit([26,33,36,27,37],55,0.01)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55,0.01)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55,0.01)
phat, pci

[phat,pci] = binofit([10, 12, 7 , 8 , 9],100,0.01)
phat, pci
[phat,pci] = binofit([25, 32, 26, 23, 18],100,0.01)
phat, pci
[phat,pci] = binofit([49, 52, 56, 57, 53],100,0.01)
phat, pci
[phat,pci] = binofit([55, 65, 62, 64, 57],100,0.01)
phat, pci
[phat,pci] = binofit([95, 90, 88, 89, 92],100,0.01)
phat, pci

[phat,pci] = binofit([23,24,34,35,32],256,0.01)
phat, pci
[phat,pci] = binofit([65, 62, 66, 56, 47],256,0.01)
phat, pci
[phat,pci] = binofit([134, 135, 148, 149, 132],256,0.01)
phat, pci
[phat,pci] = binofit([165, 155, 147, 145, 155],256,0.01)
phat, pci
[phat,pci] = binofit([224, 231, 227, 238, 236],256,0.01)
phat, pci

[phat,pci] = binofit([57, 62, 65 , 53 , 67],500,0.01)
phat, pci
[phat,pci] = binofit([120, 124, 122, 117, 118],500,0.01)
phat, pci
[phat,pci] = binofit([276, 294, 267, 279, 281],500,0.01)
phat, pci
[phat,pci] = binofit([305, 313, 299, 300, 306],500,0.01)
phat, pci
[phat,pci] = binofit([445,  455,  448, 456, 449],500,0.01)
phat, pci

[phat,pci] = binofit([118,111,110,108,120],1000,0.01)
phat, pci
[phat,pci] = binofit([237,202,213,241,229],1000,0.01)
phat, pci
[phat,pci] = binofit([532,571,542,529,566],1000,0.01)
phat, pci
[phat,pci] = binofit([691,598,580,620,615],1000,0.01)
phat, pci
[phat,pci] = binofit([891,894,908,900,895],1000,0.01)
phat, pci

#-------------0.60 confidence intervals ----------------
[phat,pci] = binofit([10, 5,6,8,9],55,0.4)
phat, pci
[phat,pci] = binofit([11, 15,13,12,14],55,0.4)
phat, pci
[phat,pci] = binofit([26,33,36,27,37],55,0.4)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55,0.4)
phat, pci
[phat,pci] = binofit([25,35,39,30,37],55,0.4)
phat, pci

[phat,pci] = binofit([10, 12, 7 , 8 , 9],100,0.4)
phat, pci
[phat,pci] = binofit([25, 32, 26, 23, 18],100,0.4)
phat, pci
[phat,pci] = binofit([49, 52, 56, 57, 53],100,0.4)
phat, pci
[phat,pci] = binofit([55, 65, 62, 64, 57],100,0.4)
phat, pci
[phat,pci] = binofit([95, 90, 88, 89, 92],100,0.4)
phat, pci

[phat,pci] = binofit([23,24,34,35,32],256,0.4)
phat, pci
[phat,pci] = binofit([65, 62, 66, 56, 47],256,0.4)
phat, pci
[phat,pci] = binofit([134, 135, 148, 149, 132],256,0.4)
phat, pci
[phat,pci] = binofit([165, 155, 147, 145, 155],256,0.4)
phat, pci
[phat,pci] = binofit([224, 231, 227, 238, 236],256,0.4)
phat, pci

[phat,pci] = binofit([57, 62, 65 , 53 , 67],500,0.4)
phat, pci
[phat,pci] = binofit([120, 124, 122, 117, 118],500,0.4)
phat, pci
[phat,pci] = binofit([276, 294, 267, 279, 281],500,0.4)
phat, pci
[phat,pci] = binofit([305, 313, 299, 300, 306],500,0.4)
phat, pci
[phat,pci] = binofit([445,  455,  448, 456, 449],500,0.4)
phat, pci

[phat,pci] = binofit([118,111,110,108,120],1000,0.4)
phat, pci
[phat,pci] = binofit([237,202,213,241,229],1000,0.4)
phat, pci
[phat,pci] = binofit([532,571,542,529,566],1000,0.4)
phat, pci
[phat,pci] = binofit([691,598,580,620,615],1000,0.4)
phat, pci
[phat,pci] = binofit([891,894,908,900,895],1000,0.4)
phat, pci