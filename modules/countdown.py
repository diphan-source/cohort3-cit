
import sys # import the system module
import time 
import datetime

# show usage of the time module
def usage():
    print("countdown.py  <number>")
    
# countdown timer function 
def countdown_timer():
    if len(sys.argv) == 2:
        # check the argv being received 
        print(sys.argv)
        # check if argv can be converted to an integer
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            # throw a value error if the argument is not an integer
            print("please enter a valid number")
            sys.exit(-1) 
            
    else:
        # show usage if no argument is passed
        usage()
        sys.exit(-1)
        
    # create an infinite loop
    while countdown > 0:
        # 00:00:00
        # create time and convert it to a string from datetime module
        countdown_timer = datetime.timedelta(seconds=countdown)
        # print time 
        print(countdown_timer)
        # wait for one second 
        time.sleep(1)
        # decrement countdown by 1
        countdown -= 1
    # print finished loop 
    print("countdown finished")
        
            
def main():
    countdown_timer()
    
if __name__ == "__main__":
    main()
    