from lab1.DFA_lab1 import *

# "lab1_json_test.json", "lab1_json_test2.json", "lab1_json_alph3.json"

# TODO №1  Create Class for DFA minimization DONE
# TODO №2  Create method for reading json file DONE
# TODO №3  Create method for parsing json file DONE
# TODO №4  Create 2-dimention matrix for parsing DFA: DONE .... .... ....
    # TODO Обозначить "Х" элементы (F, NOT F) в объединении (NOT F and F):  (f, ^f) and (^f, f) DONE
    # TODO Делать проверку (работа с json файлом) переходов

class DFAmin(DFA):
    def __init__(self, jsonfile):
        super(DFAmin, self).__init__(json_file=jsonfile)
        self._dfa_table = [[' ' for x in range(len(self.attitude))] for y in range(len(self.attitude))]
        self._delimiters = ['*', 'x', 'v', '_']

    def play(self):
        self._fill_table()
        self._show_matrix()

    """Minimizates DFA"""
    def _create_table(self):
        """creates an auxiliary table for further processes"""
        for x, xVal in enumerate(self._dfa_table):
            for y, yVal in enumerate(xVal):
                if x > y:
                    self._dfa_table[x][y] = self._delimiters[0]
                elif x == y:
                    self._dfa_table[x][y] = self._delimiters[2]
                else:
                    self._dfa_table[x][y] = self._delimiters[3]
        return self._dfa_table

    def _fill_table(self):
        """fills created table with default values from algorithm"""
        assert len(self._dfa_table) != 0
        assert isinstance(self._dfa_table, list)
        checked_delims = ['x', 'v', 'Ⓧ', 'Ⓥ']
        self._dfa_table = self._create_table()
        for y, y_value in enumerate(self._dfa_table):
            for x, x_value in enumerate(y_value):
                if (x in self.state_true and y not in self.state_true) or\
                   (y in self.state_true and x not in self.state_true):
                    if x > y:
                        self._dfa_table[y][x] = checked_delims[0]
        self._show_matrix()
        # for check if our table has some changes
        while self._fill_gaps():
            self._show_matrix()
            self._fill_gaps()
        return self._dfa_table

    def _fill_gaps(self):
        """Fills gaps ('_') in _dfa_table with 'X' according to algorithm"""
        check_for_changes = False
        for y, y_value in enumerate(self._dfa_table):
            for x, x_value in enumerate(y_value):
                if x_value == self._delimiters[-1]:
                    # Empty states (self._dfa_table[y][x] == '_')
                    state_y = self.attitude[y] #row
                    state_x = self.attitude[x] #column
                    # Check if next state is 'X' for any length alphabet
                    for num in range(len(self.alphabet)):
                        # state_z[num] where num is index of the next state
                        # it means that we check pair of the next states of current
                        if self._dfa_table[state_y[num]][state_x[num]] == self._delimiters[1]:
                            check_for_changes = True
                            self._dfa_table[y][x] = "x"
                            break
        return check_for_changes

    def _show_matrix(self):
        print("-" * (len(self._dfa_table) * 2))
        for i in self._dfa_table:
            for j in i:
                print(j, end=" ")
            print()

"""
print(path)
filename = readJSON("new_lab1_json_test.json")
min = DFAmin(filename)
dfaTable = min.fill_table()
show_matrix(dfaTable)
"""

"""Shows result of calculations"""
# while True:
#     tape = input("Input tape:")
#     fileJSON = readJSON(filename)
#     testDFA1 = DFA(fileJSON)
#     testDFA1.__repr__()
#     print(testDFA1.predicate())`
#     testDFA1.current_state = 0
#     question = input("Rewrite a tape? (Press key 'Enter' to rewrite and 'NO' if you dont want):")
#     if question == "NO":
#         break

"""how to create new DFA and dump it to JSON file"""

# json_instance = Create_JSON_data("Vanya DFA", 0, ([7,8]), ([0,1]), [[1,2], [3,0], [0,4], [0,5], [6,0], [7,9], [10,8], [7,7], [8,8], [9,5], [6,10]])
# writeJSON(json_instance.string_for_json_encode())
