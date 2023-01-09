def simm_diff(A, B):
    U = A.union(B)
    I = A.intersection(B)
    R = U.difference(I)
    return R

insieme1 = {4,6,2,9}
insieme2 = {1,2,3,4,7}

print(simm_diff(insieme1, insieme2))