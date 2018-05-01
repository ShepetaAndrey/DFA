from lab2.DFA_min_lab2 import *
import time

def main():
    t1 = time.clock()
    json = "lab1_json_alph3.json"
    inst1 = DFAmin(readJSON(json))
    inst1.play()
    t2 = time.clock()
    print("%f sec" % float(t2-t1))

if __name__ == "__main__":
    main()



    # instDFA = Create_JSON_data("blabla", 0, [1,2,3], [0,1], [[1,2], [2,3], [2,9], [3,1]])
    # filename = input("Input file name:")