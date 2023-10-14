import inputs
userIn = 5
def Figure_1():
    inputs.Figure_1A()
    inputs.Figure_1B()
    inputs.Figure_1C()
def Figure_2():
    inputs.Figure_2A()
    inputs.Figure_2B()
    inputs.Figure_2C()
def Figure_3():
    inputs.Figure_3A()
    inputs.Figure_3B()
    inputs.Figure_3C()

while(userIn != 4):
    print("1:Part 1, 2:Part 2, 3:Part 3, 4:Exit ==")
    userIn = int(input())
    if(userIn == 1):
        Figure_1()
    elif(userIn == 2):
        Figure_2()
    elif(userIn == 3):
        Figure_3()
    elif(userIn == 4):
        print("Thank you!")
    else:
        print("Enter correct input")

