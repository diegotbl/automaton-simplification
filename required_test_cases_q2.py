from q2 import dfa_minimization


print("Test 1:\n")
automaton = [['a', 'b'],
             [[0], [3], [3, 4], [2, 3], [2, 3, 4], [1, 2, 3, 4, 5, 6], [1, 2, 3, 6], [1, 2, 3, 4, 6]],
             [[('a', [3]), ('b', [3, 4])], [('a', [2, 3]), ('b', [2, 3, 4])], [('a', [2, 3]), ('b', [1, 2, 3, 4, 5, 6])], [('a', [2, 3]), ('b', [2, 3, 4])], [('a', [2, 3]), ('b', [1, 2, 3, 4, 5, 6])], [('a', [1, 2, 3, 6]), ('b', [1, 2, 3, 4, 5, 6])], [('a', [1, 2, 3, 6]), ('b', [1, 2, 3, 4, 6])], [('a', [1, 2, 3, 6]), ('b', [1, 2, 3, 4, 5, 6])]],
             [[1, 2, 3, 4, 5, 6], [1, 2, 3, 6], [1, 2, 3, 4, 6]]]

print(dfa_minimization(automaton))
print()

print("Test 2: [0] and [3] were switched\n")
automaton = [['a', 'b', 'c'],
             [[3], [0], [], [1, 2]],
             [[('a', []), ('b', [1, 2]), ('c', [1, 2])], [('a', [3]), ('b', []), ('c', [])], [('a', []), ('b', []), ('c', [])], [('a', [3]), ('b', []), ('c', [])]],
             [[0], [1, 2]]]

print(dfa_minimization(automaton))
print("Final answer: (['a', 'b', 'c'], [[[1, 2], [0]], [], [3]], [[('a', [3]), ('b', []), ('c', [])], [('a', []), ('b', []), ('c', [])], [('a', []), ('b', [[1, 2], [0]]), ('c', [[1, 2], [0]])]], [[[1, 2], [0]]])")
print()

print("Test 3:\n")
automaton = [['a', 'b'],
             [[0], [1, 4], [1, 5], [2, 4], [1], [3, 5], [], [1, 2]],
             [[('a', [1, 4]), ('b', [1, 5])], [('a', [2, 4]), ('b', [1])], [('a', [1]), ('b', [3, 5])], [('a', [2, 4]), ('b', [1])], [('a', []), ('b', [])], [('a', [1, 2]), ('b', [3, 5])], [('a', []), ('b', [])], [('a', []), ('b', [1])]],
             [[1, 4], [1, 5], [1], [3, 5], [1, 2]]]

print("Final answer: " + str(dfa_minimization(automaton)))
print()

print("Test 4:\n")
automaton = [['a', 'b', 'c'],
             [[0], [3], [5], [6], [1, 2, 3, 4, 5, 6], [], [1, 4, 5, 6], [1, 6]],
             [[('a', [3]), ('b', [5]), ('c', [6])], [('a', [1, 2, 3, 4, 5, 6]), ('b', [5]), ('c', [6])], [('a', []), ('b', [1, 4, 5, 6]), ('c', [6])], [('a', []), ('b', []), ('c', [1, 6])], [('a', [1, 2, 3, 4, 5, 6]), ('b', [1, 4, 5, 6]), ('c', [1, 6])], [('a', []), ('b', []), ('c', [])], [('a', []), ('b', [1, 4, 5, 6]), ('c', [1, 6])], [('a', []), ('b', []), ('c', [1, 6])]],
             [[0], [3], [5], [6], [1, 2, 3, 4, 5, 6], [1, 4, 5, 6], [1, 6]]]
print(dfa_minimization(automaton))
print()
