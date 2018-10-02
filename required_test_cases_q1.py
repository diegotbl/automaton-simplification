from q1 import nfa2dfa


print("Test 1:\n")
sigma = ['a', 'b']
f = [1, 5, 6]
delta = [[('a', [3]), ('b', [3]), ('b', [4])],
         [],
         [('b', [4])],
         [('a', [2]), ('a', [3]), ('b', [2]), ('b', [3]), ('b', [4])],
         [('b', [1]), ('b', [5]), ('b', [6])],
         [('a', [6]), ('b', [6])],
         [('a', [1]), ('a', [6]), ('b', [1]), ('b', [6])]]

dfa = []

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma, delta, f)
dfa.extend([actual_sigma, actual_states, actual_delta, actual_f])

print("DFA: \n" + str(dfa) + "\n\n")


print("Test 2:\n")
sigma = ['a', 'b', 'c']
f = [0, 1, 2]
delta = [[('a', [3])],
         [],
         [('a', [3])],
         [('b', [1]), ('b', [2]), ('c', [1]), ('c', [2])]]

dfa = []

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma, delta, f)
dfa.extend([actual_sigma, actual_states, actual_delta, actual_f])

print("DFA: \n" + str(dfa) + "\n\n")


print("Test 3:\n")
sigma = ['a', 'b']
f = [1]
delta = [[('a', [1]), ('a', [4]), ('b', [1]), ('b', [5])],
         [],
         [('b', [1])],
         [('a', [2])],
         [('a', [2]), ('a', [4]), ('b', [1])],
         [('a', [1]), ('b', [3]), ('b', [5])]]

dfa = []

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma, delta, f)
dfa.extend([actual_sigma, actual_states, actual_delta, actual_f])

print("DFA: \n" + str(dfa) + "\n\n")


print("Test 4:\n")
sigma = ['a', 'b', 'c']
f = [0, 1, 2, 3, 4, 5, 6]
delta = [[('a', [3]), ('b', [5]), ('c', [6])],
         [],
         [('b', [5]), ('c', [6])],
         [('a', [1]), ('a', [2]), ('a', [3]), ('a', [4]), ('a', [5]), ('a', [6]), ('b', [5]), ('c', [6])],
         [('c', [6])],
         [('b', [1]), ('b', [4]), ('b', [5]), ('b', [6]), ('c', [6])],
         [('c', [1]), ('c', [6])]]

dfa = []

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma, delta, f)
dfa.extend([actual_sigma, actual_states, actual_delta, actual_f])

print("DFA: \n" + str(dfa) + "\n\n")
