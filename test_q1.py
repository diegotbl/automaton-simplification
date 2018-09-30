from q1 import nfa2dfa

print('\nTest 1:')

sigma = ['a', 'b']
delta = [[('a', 0), ('b', 0), ('a', 1)], [('b', 0)]]
f = [1]

print('NFA:')
print(f'sigma = {sigma}')
print(f'Q = {[_ for _ in range(len(delta))]}')
print(f'delta = {delta}')
print(f'F = {f}\n')

expected_sigma = sigma
expected_states = [[0],[0,1]]
expected_delta = [[('a', [0,1]), ('b', [0])], [('a', [0,1]), ('b', [0])]]
expected_f = [[0,1]]

print('Expected DFA:')
print(f'sigma = {expected_sigma}')
print(f'Q = {expected_states}')
print(f'delta = {expected_delta}')
print(f'F = {expected_f}\n')

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma,delta,f)

print('Actual DFA:')
print(f'sigma = {actual_sigma}')
print(f'Q = {actual_states}')
print(f'delta = {actual_delta}')
print(f'F = {actual_f}\n')

print('\nTest 2:')

sigma = ['0', '1']
delta = [[('1', 1), ('1', 2)], [('0', 3)], [('1', 3)], []]
f = [3]

print('NFA:')
print(f'sigma = {sigma}')
print(f'Q = {[_ for _ in range(len(delta))]}')
print(f'delta = {delta}')
print(f'F = {f}\n')

expected_sigma = sigma
expected_states = [[0],[],[1,2],[3]]
expected_delta = [[('0',[]),('1',[1,2])], [('0',[]),('1',[])], [('0',[3]),('1',[3])], [('0',[]),('1',[])]]
expected_f = [[3]]

print('Expected DFA:')
print(f'sigma = {expected_sigma}')
print(f'Q = {expected_states}')
print(f'delta = {expected_delta}')
print(f'F = {expected_f}\n')

actual_sigma, actual_states, actual_delta, actual_f = nfa2dfa(sigma,delta,f)

print('Actual DFA:')
print(f'sigma = {actual_sigma}')
print(f'Q = {actual_states}')
print(f'delta = {actual_delta}')
print(f'F = {actual_f}')
