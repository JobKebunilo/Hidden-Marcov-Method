from array import *
#N = 3
#M = 4
#T = 6
#A = [[0.1, 0.2, 0.7], [0.2, 0.3, 0.5], [0.3, 0.4, 0.3]]
#B = [[0.4, 0.1, 0.2, 0.3], [0.3, 0.1, 0.2, 0.4], [0.4, 0.2, 0.1, 0.3]]
#OI = [2, 1, 3, 3, 2, 3]
# Input assumpton
N = 4
M = 3
T = 5
A = [[0.1, 0.2, 0.3, 0.4], [0.2, 0.3, 0.2, 0.3], [0.3, 0.4, 0.2, 0.1], [0.2, 0.2, 0.1, 0.5] ]
B = [[0.4, 0.1, 0.5], [0.3, 0.1, 0.6], [0.4, 0.2, 0.4], [0.3, 0.4, 0.3] ]
OI = [2, 3, 3, 3, 2]


def direct_method(Pi):
    finalResult = 0
    val = []
    input = []
    for t in range(T):
        input.append(0)
    stage,valFinal = direct_method_recursive(0,input,val,Pi)
    print(len(valFinal))
    print(valFinal)
    for q in range(pow(N,T)):
        finalResult += valFinal[q]
    return finalResult

def direct_method_recursive(stage,values,result,Pi):
    input = values
    valResult =result
    print(input)
    if(stage < T):
        for n in range(N):
            input[stage] = n
            stage += 1
            stage,valResult = direct_method_recursive(stage, input, valResult, Pi)
            stage -= 1
    elif(stage == T):
        val1 = 1
        val2 = 1
        for t in range(T-1):
            val1 *= A[input[t]][input[t+1]]
        for t in range(T):
            val2 *= B[input[t]][OI[t]-1]
        val3 = Pi[input[0]] * val1
        valResult.append(val3*val2)
        print(values)
        print(val3*val2)
        print(" ")
    return stage,valResult

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
    finalSum = 0.0
    for j in range(N):
        finalSum += result[T-1][j]
    return finalSum

def bwd_induction_method(Pi):
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
    finVal = 0
    for j in range(N):
        valResult = 0
        val1 = round(Pi[j],2)
        val2 = B[j][OI[0]-1]
        val3 = result[0][j]
        valResult = val1 * val2 * val3
        finVal += valResult

    return finVal
def calculation(input):
    result, stage, time = recursive(input, 0, 0)
    print(time)
    return result
def recursive(input, stage,time):
    #print("Stage",stage)
    Origin = input.copy()
    new = Origin.copy()
    total = 0
    run = time

    if(stage < T - 1):

        for n in range(N):
            stage += 1
            #print("Its stage",stage)
            val, stage, run = recursive(Origin, stage, run)
            stage -= 1
            total += val
            if(stage == 0):
                Origin[0] = total
        new[stage] = total
        print(new)
    elif(stage == T-1):
        for n in range(N):
            total += Origin[n]
            run += 1
        new[stage] = total
        print(new)

    #elif(stage == 1):
        #Origin[0]=val
    return total, stage, run

