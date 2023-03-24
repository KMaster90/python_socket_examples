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
# function1()
# function2()
# function3()

#WE can execute these functions concurrently using threads! We mush have a target for a thread.
# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)
# t3 = threading.Thread(target=function3)

#We can start the threads
# t1.start()
# t2.start()
# t3.start()

#Thread can only be run once. If you want to reuse, you must create a new thread
# t1 = threading.Thread(target=function1)
# t1.start()

#If you want to 'pause' the main program until a thread is complete
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.start()
# t1.join() #This will pause the main program until t1 is complete
t2.start()
t2.join()
print("Threading rules!")