from q1 import nfa2dfa

sigma = []
sigma.append(['a', 'b'])
sigma.append(['0', '1'])
sigma.append(['a'])

delta = []
delta.append([[('a', 0), ('b', 0), ('a', 1)], [('b', 0)]])
delta.append([[('1', 1), ('1', 2)], [('0', 3)], [('1', 3)], []])
delta.append([[('a', 3)], [], [('a', 3)], [('a', 2), ('a', 1)]])

f = []
f.append([1])
f.append([3])
f.append([0, 1, 2])

expected_states = []
expected_states.append([[0],[0,1]])
expected_states.append([[0],[],[1,2],[3]])
expected_states.append([[0], [3], [1,2]])

expected_delta = []
expected_delta.append([[('a', [0,1]), ('b', [0])], [('a', [0,1]), ('b', [0])]])
expected_delta.append([[('0',[]),('1',[1,2])], [('0',[]),('1',[])], [('0',[3]),('1',[3])], [('0',[]),('1',[])]])
expected_delta.append([[('a', [3])], [('a', [1,2])], [('a', [3])]])

expected_f = []
expected_f.append([[0,1]])
expected_f.append([[3]])
expected_f.append([[0], [1,2]])

for i in range(len(sigma)):
  print(f'\nTest {i+1}:')

  print('NFA:')
  print(f'sigma = {sigma[i]}')
  print(f'Q = {[_ for _ in range(len(delta[i]))]}')
  print(f'delta = {delta[i]}')
  print(f'F = {f[i]}\n')

  print('Expected DFA:')
  print(f'sigma = {sigma[i]}')
  print(f'Q = {expected_states[i]}')
  print(f'delta = {expected_delta[i]}')
  print(f'F = {expected_f[i]}\n')

  actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma[i],delta[i],f[i])

  print('Actual DFA:')
  print(f'sigma = {actual_sigma}')
  print(f'Q = {actual_states}')
  print(f'delta = {actual_delta}')
  print(f'F = {actual_f}\n')
