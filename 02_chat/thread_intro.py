import threading
#Threading allows us to spped up programs by executing multiple tasks at the SAME time.
#Each task will run on its own thread
#Each thread can run simultaneously and share data with each other.

#Every thread when you start it must do SOMETHING, which we can define with a function.
#Our threads will then target these functions.
#When we start the threads, the target functions will be run.

def function1():
    for i in range(10):
        print("ONE ")
def function2():
    for i in range(10):
        print("TWO ")
def function3():
    for i in range(10):
        print("THREE ")

#If we call these functions, we see the first call MUST complete before the next
#They are executed linearly
function1()
function2()
function3()