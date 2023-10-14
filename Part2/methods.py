import numpy as np
N = 3
M = 4
T = 6
A = [[0.1, 0.2, 0.7], [0.2, 0.3, 0.5], [0.3, 0.4, 0.3]]
B = [[0.4, 0.1, 0.2, 0.3], [0.3, 0.1, 0.2, 0.4], [0.4, 0.2, 0.1, 0.3]]
OI = [2, 1, 3, 3, 2, 3]

def fwd_induction_method(Pi):
    result = [[]]
    for i in range(N):
        product = Pi[i] * B[0][OI[0]-1]
        result[0].append(product)
    for t in range(1,T):
        val = []
        for j in range(N):
            totalSum = 0
            for i in range(N):
                val1 = result[t-1][i]
                val2 = A[i][j]
                val3 = B[j][OI[t]-1]
                valRes = val1 * val2 * val3
                totalSum += valRes
            val.append(totalSum)
        result.append(val)
    return result

def bwd_induction_method():
    result = []
    for t in range(T):
        result.append([])
    for n in range(N):
        result[T-1].append(1)

    for t in range(T - 2,-1,-1):
        for i in range(N):
            totalProd = 0
            for j in range(N):
                val1 = A[i][j]
                val2 = B[j][OI[t+1]-1]
                val3 = result[t+1][j]
                valRes = val1 * val2 * val3
                totalProd += valRes
            result[t].append(totalProd)
    return result

def inital_method(Pi):
    alpha = fwd_induction_method(Pi)
    beta = bwd_induction_method()
    theta = np.array(alpha)*np.array(beta)
    pos = np.argmax(theta, axis = 1)
    print("Q array = ",pos)
def vierbi_method(Pi):
    result1 = [[]]
    result2 = [[]]
    finResult = []
    for i in range(N):
        val1 = Pi[i]
        val2 = B[0][OI[0]-1]
        result1[0].append(val1*val2)
    for i in range(N):
        result2[0].append(0)
    for t in range(1,T):
        val = []
        for j in range(N):
            maxArr = []
            for i in range(N):
                val1 = result1[t-1][i]
                val2 = A[i][j]
                maxArr.append(val1*val2)
            val3 = max(maxArr)
            val4 = B[j][OI[t]-1]
            val.append(val3*val4)
        result1.append(val)
    for t in range(1,T):
        val = []
        for j in range(N):
            maxArr = []
            for i in range(N):
                val1 = result1[t-1][i]
                val2 = A[i][j]
                maxArr.append(val1*val2)
            val3 = np.argmax(maxArr)
            val.append(val3)
        result2.append(val)
    maxArr = []
    for i in range(N):
        maxArr.append(result1[T-1][i])
    P = max(maxArr)
    print("P = ", P)
    for t in range(T):
        finResult.append(0)
    finResult[T-1] = np.argmax(result1[T-1])
    for t in range(T - 2,-1,-1):
        val1 = finResult[t+1]
        finResult[t] = (result2[t+1][val1])
    print('Q',T,'=',finResult[T-1])
    print("Q array = ",finResult)