K = int(input())

A = [0] * (K + 1)
B = [0] * (K + 1)

A[0] = 1
B[0] = 0

for i in range(1, K + 1):
    A[i] = B[i - 1]
    B[i] = A[i - 1] + B[i - 1]

print(A[K], B[K])
