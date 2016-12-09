import transactions

class Tape(object):
    blank_symbol = " "

    def __init__(self,
                 tape_string=""):
        self.__tape = dict((enumerate(tape_string)))
        # last line is equivalent to the following three lines:
        # self.__tape = {}
        # for i in range(len(tape_string)):
        #    self.__tape[i] = input[i]

    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine(object):
    def __init__(self,
                 tape="",
                 blank_symbol=" ",
                 initial_state="",
                 final_states=None,
                 transition_function=None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        print ("char under head:",char_under_head)
        x = (self.__current_state, char_under_head)
        print ("state to be compared:", x)
        if x in self.__transition_function:
            print (x," are in transition function")
            y = self.__transition_function[x]
            print ("tape changes value ",self.__tape[self.__head_position]," to :", y[1])
            self.__tape[self.__head_position] = y[1]

            if y[2] == "R":
                self.__head_position += 1
                print ("head position moves to R")
            elif y[2] == "L":
                self.__head_position -= 1
                print ("head position moves to L")
            self.__current_state = y[0]
            return self.__current_state

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False



def montar_TM():
    simbolos = raw_input("simbolos:")
    answers = simbolos.split(' ')

    print answers





montar_TM()

initial_state = "init",
accepting_states = ["final"],
transition_function = transactions.changeLetters
final_states = {"final"}
alpha = raw_input('alfabeto:')
#"010011 "
t = TuringMachine(alpha,
                  initial_state = "init",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())


print (t.get_tape())
while not t.final():
    s=t.step()
    print 'current sate:',s

print("Result of the Turing machine calculation:")
print(t.get_tape())


# consult:
# http://www.python-course.eu/turing_machine.php