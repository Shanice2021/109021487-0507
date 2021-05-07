import sys
import random as rrr

if __name__=="__main__":
    if len(sys.argv)>2:
        seedval = int(sys.argv[1])        
        data = list(sys.argv[2])
        rrr.seed(seedval)
        rrr.shuffle(data)
        print("".join(data))