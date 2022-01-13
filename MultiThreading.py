import threading
import time 

def cal_sqre(num, thread_num): # define a square calculating function  
    print(f" Thread { thread_num } - Calculate the square root of the given number")  
    for n in num: # Use for loop   
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(f'\n Thread { thread_num } - Square {n} is : { n * n }') 

if __name__ == '__main__':
    arr = [4, 5, 6] # given array  
    start_time = time.time() # get total time to execute the functions  
    thread1 = threading.Thread(target=cal_sqre, args=(arr, 1,))
    thread2 = threading.Thread(target=cal_sqre, args=(arr, 2,))
    thread3 = threading.Thread(target=cal_sqre, args=(arr, 3,))
    # start threads
    thread1.start()
    thread2.start()
    thread3.start()
    # join threads by main thread
    thread1.join()
    thread2.join()
    thread3.join()
    end_time = time.time() # get start time
    # print the total time
    print("\n Total time taking by threads is :", end_time - start_time) 