""" Using modules sys or argparse, create a command line application that accepts commandline arguments.
    Your program should have the following features:
        - usage of the program
        - should be function based: ie a function that will handle a particular argument passed in
"""

import sys

def usage():
    print("py assigment.py <command>")
    sys.exit(1)
    
def cmd_args(*args):
    if len(args) == 0:
        usage()
    else:
        for arg in args:
            if arg == "version":
                print(sys.version)
            elif arg == "platform":
                print(sys.platform)
            elif arg == "name":
                print(f"Your system name is {sys.thread_info.name}")
            elif arg == "path":
                print(sys.path)
            else:
                print("Invalid command")
                usage()
                
def main():
    cmd_args(*sys.argv[1:])
    
if __name__ == "__main__":
    main()    