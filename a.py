from time import sleep
i= 0
A= 0.05-(i*0.01)
for i in range(20):
    print("加速")
    sleep(A)
    if A ==0:
        A= 0.0001