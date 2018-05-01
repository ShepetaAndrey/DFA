import json
import pprint
import os

path = os.getcwd()


# "lab1_json_test.json", "lab1_json_test2.json", "lab1_json_alph3.json"

class DFA():
    """Initializes class variables with json data from file and tests it"""

    def __init__(self, json_file):
        self.description = json_file["description"]
        self.current_state = json_file["current_state"]
        self.state_true = json_file["state_true"]
        self.alphabet = json_file["alphabet"]
        self.attitude = json_file["attitude"]
        self.json_file = json_file

    def __repr__(self):
        for key, value in self.json_file.items():
            print(str(key) + ": " + str(value))

    def __str__(self):
        return "description: {}, current_state: {} state_true: {}, alphabet: {}, attitude: {}" \
            .format(self.description, self.current_state, self.state_true, self.alphabet, self.attitude)

    def predicate(self, tape):
        """Make decision about accuracy of DFA.
		    If DFA is accurate return True
		    else: return False"""
        for symb in str(tape):
            self.current_state = self.attitude[self.current_state][int(symb)]

        if self.current_state in self.state_true or self.current_state == self.state_true:
            return True
        else:
            return False


class Create_JSON_data():
    """Create string performance of DFA (just for examples)"""

    def __init__(self, description, current_state, state_true, alphabet, attitude):
        self.description = description
        self.current_state = current_state
        self.state_true = state_true
        self.alphabet = alphabet
        self.attitude = attitude

    def string_for_json_encode(self):
        return {'description': self.description, 'current_state': self.current_state, 'state_true': self.state_true,
                'alphabet': self.alphabet, 'attitude': self.attitude}


def writeJSON(fileToWrite, string_to_dump):
    with open(path + "\\" + fileToWrite, 'w') as file:
        json.dump(string_to_dump, file, indent=4)


def readJSON(filename):
    with open(path + "\\" + filename, 'r') as f:
        filejson = json.load(f)
        return filejson


"""Shows result of calculations"""

# while True:
# 	tape = input("Input tape:")
# 	fileJSON = readJSON(filename)
# 	testDFA1 = DFA(fileJSON)
# 	testDFA1.__repr__()
# 	print(testDFA1.predicate())
# 	testDFA1.current_state = 0
# 	question = input("Rewrite a tape? (Press key 'Enter' to rewrite and 'NO' if you don`t want):")
# 	if question == "NO":
# 		break
