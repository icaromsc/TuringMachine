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
        self.count = 0
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
        else:
            self.count += 1

        if self.count>10000:
            return False
        else:
            return True

    def final(self):
        print("atual:",self.__current_state)
        print("finais:", self.__final_states)
        if self.__current_state in self.__final_states:
            return True
        else:
            return False



def montar_TM():
    r = input("simbolos:")
    simbolos = r.split(' ')
    print ("simbolos definidos: ",simbolos)

    r = input("defina os estados possiveis:")
    estados = r.split(' ')
    print("estados definidos: ", estados)

    r = input("defina o estado inicial:")
    inicial = tuple(r.split(' '))

    r = input("defina os estados finais:")
    finais = r.split(' ')
    finais=tuple(finais)
    print("estados finais definidos: ", finais)

    ocorrencias= simbolos + [" "]
    tdict={}
    print("informe as transações de estados para " , ocorrencias )
    for est in estados:
        for o in ocorrencias:
            print("informe as transações de estados para ", o)
            msg = "estado " + est + ": "
            r = input(msg)
            value= r.split(' ')
            if len(r)>0:
                print("instrução:",value)
                tdict[(est,o)]=tuple(value)
    print("função transição montada:",tdict)
    alpha = input('DIGITE A SENTENÇA:')
    #finais = {"final"}
    print("estados finais:",finais)

    turing = TuringMachine(alpha,
                  initial_state = tuple(inicial),
                  final_states = tuple(finais),
                  transition_function=tdict)

    print("Input on Tape:\n" + turing.get_tape())

    aceita = True
    while not turing.final():
        s = turing.step()
        if (s):
            continue
        else:
            aceita = False
            break

    if aceita:
        print("\n*******\n*******\n************* SENTENÇA ACEITADA *************\n*****\n******\n", aceita)
        print("Result of the Turing machine calculation:")
        print(turing.get_tape())
    else:
        print("\n*******\n*******\n************* SENTENÇA REJEITADA *************\n*****\n******\n")








montar_TM()

# initial_state = "init",
# accepting_states = ["final"],
# transition_function = transactions.uppercase
# final_states = {"final"}
# alpha = input('DIGITE A SENTENÇA:')
# #"010011 "
# print("initial:",initial_state)
# print("acepting:",accepting_states)
# print("transaction:",transition_function)
# print("final:",final_states)
# t = TuringMachine(alpha,
#                   initial_state = "init",
#                   final_states = final_states,
#                   transition_function=transition_function)
#
# print("Input on Tape:\n" + t.get_tape())
#
# aceita=True
# while not t.final():
#     s=t.step()
#     if(s):
#         continue
#     else:
#         aceita=False
#         break
#
# if aceita:
#     print("\n*******\n*******\n************* SENTENÇA ACEITADA *************\n*****\n******\n", aceita)
#     print("Result of the Turing machine calculation:")
#     print(t.get_tape())
# else:
#     print("\n*******\n*******\n************* SENTENÇA REJEITADA *************\n*****\n******\n")



# consult:
# http://www.python-course.eu/turing_machine.php