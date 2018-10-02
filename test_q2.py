from q2 import dfa_minimization


alphabet = ['a', 'b']
states = [[0], [3, 4], [2]]
final_states = [[2]]
states_transitions = [[('a', [3, 4]), ('b', [0])], [('a', [3, 4]), ('b', [2])], [('a', [3, 4]), ('b', [2])]]
automaton = (alphabet, states, states_transitions, final_states)

print(dfa_minimization(automaton))
print()


alphabet = ['a', 'b']
states = [[0], [1], [2], ['abobrinha'], [4], [5]]
final_states = [['abobrinha'], [5]]
states_transitions = [[('a', [1]), ('b', [2])], [('a', [4]), ('b', ['abobrinha'])], [('a', [4]), ('b', [5])],
                      [('a', ['abobrinha']), ('b', ['abobrinha'])], [('a', [4]), ('b', [4])], [('a', [5]), ('b', [5])]]
automaton = (alphabet, states, states_transitions, final_states)

print(dfa_minimization(automaton))
print()


alphabet = ['a', 'b']
states = [[0], [1], [2], [3], [4], [5], [6], [7]]
final_states = [[1], [2], [3], [4], [5], [6]]
states_transitions = [[('a', [1]), ('b', [4])], [('a', [2]), ('b', [3])], [('a', [7]), ('b', [7])],
                      [('a', [7]), ('b', [3])], [('a', [5]), ('b', [6])], [('a', [7]), ('b', [7])],
                      [('a', [7]), ('b', [6])], [('a', [7]), ('b', [7])]]
automaton = (alphabet, states, states_transitions, final_states)

print(dfa_minimization(automaton))
print()


alphabet = ['a']
states = [[0], [3], [4], [1, 2]]
final_states = [[0], [1, 2]]
states_transitions = [[('a', [3])], [('a', [4])], [('a', [1, 2])], [('a', [3])]]
automaton = (alphabet, states, states_transitions, final_states)

print(dfa_minimization(automaton))
print()


alphabet = ['a']
states = [[3], [0], [4], [1, 2]]
final_states = [[0], [1, 2]]
states_transitions = [[('a', [4])], [('a', [3])], [('a', [1, 2])], [('a', [3])]]
automaton = (alphabet, states, states_transitions, final_states)

print(dfa_minimization(automaton))
print()
