import time
import methods
import numpy as np
import matplotlib.pyplot as plt

#For finding termination values
def Figure_1A():
    start = time.time()
    Pi = [0.1, 0.2, 0.4, 0.3]
    #Pi = [0.1, 0.5, 0.4]
    print("Direct method: ", methods.direct_method(Pi))
    end = time.time()
    print("Direct method time:",end - start, "seconds")
    print()
def Figure_1B():
    start = time.time()
    #Pi = [0.1, 0.5, 0.4]
    Pi = [0.1, 0.2, 0.4, 0.3]
    print("Forward Induction Method: ", methods.fwd_induction_method(Pi))
    end = time.time()
    print("Forward Induction time:",end - start, "seconds")
    print()
def Figure_1C():
    start = time.time()
    #Pi = [0.1, 0.5, 0.4]
    Pi = [0.1, 0.2, 0.4, 0.3]
    print("Backward Induction Method: ", methods.bwd_induction_method(Pi))
    end = time.time()
    print("Backward Induction time:",end - start, "seconds")
    print()

#For ploting figure such that 0 <= x <= .6
def Figure_2A():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    #plt.ylim(0, .0001)
    x = 0
    x_array = []
    y_array = []
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        Pi = [0.4, x, 0.1, 0.5 - x]
        #Pi = [0.4, x, 0.6 - x]
        y_array.append(methods.direct_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.1.1 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.1.1')
    plt.show()
    #plt.ylim(0, .0001)
    x = 0
    x_array.clear()
    y_array.clear()
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [0.4, x, 0.6 - x]
        Pi = [0.4, x, 0.1, 0.5 - x]
        y_array.append(methods.fwd_induction_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.1.2 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.1.2')
    plt.show()
    x = 0
    #plt.ylim(0, .0001)
    x_array.clear()
    y_array.clear()
    start = time.time()
    while(x <= .6):
        #print(x)
        x_array.append(x)
        #Pi = [0.4, x, 0.6 - x]
        Pi = [0.4, x, 0.1, 0.5 - x]
        y_array.append(methods.bwd_induction_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.1.3 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.1.3')
    plt.show()
    x_array.clear()
    y_array.clear()

def Figure_2B():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    x = 0
    #plt.ylim(0, .0001)
    x_array = []
    y_array = []
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.4, 0.6 - x]
        Pi = [x, 0.4, 0.2, 0.4 - x]
        y_array.append(methods.direct_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.2.1 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.2.1')
    plt.show()
    x = 0
    #plt.ylim(0, .0001)
    x_array.clear()
    y_array.clear()

    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.4, 0.6 - x]
        Pi = [x, 0.4, 0.2, 0.4 - x]
        y_array.append(methods.fwd_induction_method(Pi))
        x += .01

    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.2.2 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.2.2')
    plt.show()
    x_array.clear()
    y_array.clear()
    x = 0
    #plt.ylim(0, .0001)
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.4, 0.6 - x]
        Pi = [x, 0.4, 0.2, 0.4 - x]
        y_array.append(methods.bwd_induction_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.2.3 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.2.3')
    plt.show()
    x_array.clear()
    y_array.clear()

def Figure_2C():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    x = 0
    #plt.ylim(0, .0000001)
    x_array = []
    y_array = []
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.6 - x, 0.4]
        Pi = [x, 0.4-x, 0.3, 0.3]
        y_array.append(methods.direct_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.3.1 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.3.1')
    plt.show()
    x_array.clear()
    y_array.clear()
    x = 0
    #plt.ylim(0, .1)
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.6 - x, 0.4]
        Pi = [x, 0.4 - x, 0.3, 0.3]
        y_array.append(methods.fwd_induction_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.3.2 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.3.2')
    plt.show()

    x_array.clear()
    y_array.clear()
    x = 0
    #plt.ylim(0, .1)
    start = time.time()
    while(x <= .6):
        x_array.append(x)
        #Pi = [x, 0.6 - x, 0.4]
        Pi = [x, 0.4 - x, 0.3, 0.3]
        y_array.append(methods.bwd_induction_method(Pi))
        x += .01
    xpoints = np.array(x_array)
    ypoints = np.array(y_array)
    plt.scatter(xpoints,ypoints)
    end = time.time()
    print("Figure-2.3.3 time:",end - start, "seconds")
    print()
    plt.title('Figure-2.3.3')
    plt.show()
    x_array.clear()
    y_array.clear()

#For ploting figure such that x >= 0, y>= 0, and x + y <= 1
def Figure_3A():
    fig = plt.figure(figsize=(4,4))
    ax = plt.axes(projection ='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [1 - x - y, x, y]
            newArray.append(methods.direct_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.1.1 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.1.1")
    plt.show()
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [1 - x - y, x, y]
            newArray.append(methods.fwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.1.2 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.1.2")
    plt.show()
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [1 - x - y, x, y]
            newArray.append(methods.bwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.1.3 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.1.3")
    plt.show()

def Figure_3B():
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, 1 - x - y, y]
            newArray.append(methods.direct_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.2.1 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.2.1")
    plt.show()
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, 1 - x - y, y]
            newArray.append(methods.fwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.2.2 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.2.2")
    plt.show()
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, 1 - x - y, y]
            newArray.append(methods.bwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.2.3 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.2.3")
    plt.show()

def Figure_3C():
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, y, 1 - x - y]
            newArray.append(methods.direct_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.3.1 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.3.1")
    plt.show()
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, y, 1 - x - y]
            newArray.append(methods.fwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.3.2 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.3.2")
    plt.show()

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    x = 0
    x_array =[]
    y_array =[]
    z_array =[]
    ax.set_zlim3d(0,.0001)
    start = time.time()
    while(x <= .5):
        x_array.append(x)
        y = 0
        newArray = []
        while(y <= .5):
            Pi = [x, y, 1 - x - y]
            newArray.append(methods.bwd_induction_method(Pi))
            y +=.01
        y_array.append(y)
        z_array.append(newArray)
        x +=.01
    x_np = np.array(x_array)
    y_np = np.array(y_array)
    z_np = np.array(z_array, dtype=float)
    ax.plot_surface(x_np, y_np, z_np)
    end = time.time()
    print("Figure-3.3.3 time:",end - start, "seconds")
    print()
    ax.set_title("Figure-3.3.3")
    plt.show()