from DFA.lab2.DFA_min_lab2 import *


def main():
    json = "new_lab1_json_test.json"
    file = readJSON(json)
    inst1 = DFAmin(file)
    inst1.play()

    # filename = input("Input file name:")

if __name__ == "__main__":
    main()