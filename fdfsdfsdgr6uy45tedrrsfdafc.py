def compute_output(A, B, C):
    Q = (A & B) | (B & ~C)
    return Q
print(compute_output(1, 1, 0)) 
