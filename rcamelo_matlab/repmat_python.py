from numpy.matlib import repmat

# PROJECT CARA SA
# repmat equivalence test (numpy matlib repmat)
# input: (filler/ vector/ matrix, n° of column, n° of rows) always three
# @author: rcamelo
# matrix fillers: {string: "e", number: 0}
# output file name: repmat_python_out.txt
# -----------------------------Matrix Creation tests-----------------------------
# -----------------One-Two dimentional tests------------------
# ------------String ---------------
# Commenting inputs where the function will fail
#A = repmat("e",1)
#A = repmat("e",1,1,1)
A = repmat("e",1,2)
A = repmat("e",2,1)
#A = repmat("e",2)
A = repmat("e",2,2)

A = repmat("e",2,5)
A = repmat("e",5,2)
#A = repmat("e",5)
# ------------Number ---------------
#A = repmat(0,1)
#A = repmat(0,1,1,1)
A = repmat(0,1,2)
A = repmat(0,2,1)
#A = repmat(0,2)
A = repmat(0,2,2)

A = repmat(0,2,5)
A = repmat(0,5,2)
#A = repmat(0,5)

"""
# -------------------Three+ dimentional tests------------------
# ------------String ---------------
A = repmat("e",1,3,2)
A = repmat("e",3,1,2)
A = repmat("e",2,2,2)

A = repmat("e",3,3,2,2)
A = repmat("e",1,5,2,2)
A = repmat("e",2,2,2,2)
# ------------Number ---------------

A = repmat(0,1,3,2)
A = repmat(0,3,1,2)
A = repmat(0,2,2,2)

A = repmat(0,3,3,2,2)
A = repmat(0,1,5,2,2)
A = repmat(0,2,2,2,2)
"""
# -----------------------------Matrix replication (n inputs) -----------------------------
# -----------------One-Two dimentional tests------------------
# ------------String ---------------

A = repmat("e",2,2) # Test Matrix
#B = repmat(A,1)
B = repmat(A,1,1)
#B = repmat(A,2)
B = repmat(A,2,2)
B = repmat(A,1,2)
B = repmat(A,2,1)
#B = repmat(A,2,1,2)

# ------------Number ---------------
A = repmat(0,2,2) # Test Matrix
#B = repmat(A,1)
B = repmat(A,1,1)
#B = repmat(A,2)
B = repmat(A,2,2)
B = repmat(A,1,2)
B = repmat(A,2,1)
#B = repmat(A,2,1,2)