import numpy as np
import math
N = 3
M = 4
T = 6
OI = [2, 1, 4, 3, 2, 3]

def fwd_induction_method(A,B,Pi):
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
def bwd_induction_method(A,B):
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
def tool_D(A,B,Alpha,Beta):
    D = []
    for t in range(T-1):
        sum1 = 0
        for i in range(N):
            sum2 = 0
            for j in range(N):
                val1 = Alpha[t][i]
                val2 = A[i][j]
                val3 = B[j][OI[t+1]-1]
                val4 = Beta[t+1][j]
                val = val1 * val2 * val3 * val4
                sum2 += val
            sum1 += sum2
        D.append(pow(sum1,-1))
    return D
def tool_Xi(D,a,b,Alpha,Beta):
    Xi=[]
    for t in range(T-1):
        page = []
        for i in range(N):
            line = []
            for j in range(N):
                val1 = D[t]
                val2 = Alpha[t][i]
                val3 = a[i][j]
                val4 = b[j][OI[t+1]-1]
                val5 = Beta[t+1][j]
                val = val1 * val2 * val3 * val4 * val5
                line.append(val)
            page.append(line)
        Xi.append(page)
    return Xi

def tool_Mu(Xi):
    Mu = []
    for t in range(T-1):
        line = []
        for i in range(N):
            Sum = 0
            for j in range(N):
                Sum += Xi[t][i][j]
            line.append(Sum)
        Mu.append(line)
    print(Mu)
    return Mu

def baum_welch_method(Pi,min):
    A = [[0.1, 0.2, 0.7], [0.2, 0.3, 0.5], [0.3, 0.4, 0.3]]
    B = [[0.4, 0.1, 0.2, 0.3], [0.3, 0.1, 0.2, 0.4], [0.4, 0.2, 0.1, 0.3]]
    Alpha = fwd_induction_method(A,B,Pi)
    Beta = bwd_induction_method(A,B)
    D = []
    piCheck = True
    aCheck = True
    bCheck = True
    Xi = []
    Mu = []
    iteration = 1
    while(True):
        Alpha = fwd_induction_method(A,B,Pi)
        Beta = bwd_induction_method(A,B)
        D = tool_D(A,B,Alpha,Beta)
        Xi = tool_Xi(D,A,B,Alpha,Beta)
        Mu = tool_Mu(Xi)
        newPi = []
        I = 0
        running = True
        if(piCheck == True):
            while(running == True):
                newPi.append(Mu[0][I])
                if(abs(newPi[I] - Pi[I]) <= min):
                    piCheck = False
                I += 1
                if(I == N):
                    I = 0
                    Pi = newPi.copy()
                    newPi = []
                    running = False

        if(aCheck == True):
            newA = []
            I = 0
            J = 0
            running = True
            line = []
            while(running == True):
                numerator = 0
                denominator = 0
                if(J == 0):
                    line = []
                for t in range(T-1):
                    numerator += Xi[t][I][J]
                for t in range(T-1):
                    denominator += Mu[t][I]
                val = numerator / denominator
                line.append(val)
                if(Pi[0] + Pi[1] + Pi[2] <= 1):
                    if(abs(line[J] - A[I][J]) <= min):
                        aCheck = False
                J += 1
                if(J == N):
                    newA.append(line)
                    J = 0
                    I += 1
                    if(I == N):
                        A = newA.copy()
                        newA = []
                        I = 0
                        running = False

        if(bCheck == True):
            newB = []
            I = 0
            K = 0
            running = True
            line = []
            while(running == True):
                numerator = 0
                denominator = 0
                if(K == 0):
                    line = []
                for t in range(T-1):
                    if(OI[t]-1 == K):
                        numerator += Mu[t][I]
                for t in range(T-1):
                    denominator += Mu[t][I]
                val = numerator / denominator
                line.append(val)
                if(Pi[0] + Pi[1] + Pi[2] <= 1):
                    if(abs(line[K] - B[I][K]) <= min):
                        bCheck = False
                K += 1
                if(K == M):
                    newB.append(line)
                    K = 0
                    I += 1
                    if(I == N):
                        B = newB.copy()
                        newB = []
                        I = 0
                        running = False
        iteration += 1
        if(piCheck == False or aCheck == False or bCheck == False):
            break
    print("Iteration: ", iteration)
    print("Pi:")
    print(Pi)
    print()
    print("A:")
    for n in range(len(A)):
        print(A[n])
    print()
    print("B:")
    for n in range(len(B)):
        print(B[n])

