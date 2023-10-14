D = []
Xi = []

Mu = []



newPi = Pi.copy()
nextPi = []
I = 0
iteration = 1
running = True
while(running == True):
    nextPi.append(Mu[0][i])
    if(abs(nextPi[I] - newPi[I]) <= min):

        newPi = nextPi.copy()
        running = False
    else:
        I += 1
        if(I == N):
            I = 0
            newPi = nextPi.copy()
            nextPi = []
            iteration += 1
print("iteration ",iteration)
print(newPi)
newA = A.copy()

print("iteration ",iteration)
print(newA)
newB = B.copy()

print("iteration ",iteration)
print(newB)