from q1 import nfa2dfa

sigma = ['a', 'b']
delta = [[('a', 0), ('b', 0), ('a', 1)], [('b', 0)]]
f = [1]

print('NFA:')
print(f'sigma = {sigma}')
print(f'delta = {delta}')
print(f'F = {f}\n')

new_sigma, new_states, new_delta, new_f = nfa2dfa(sigma,delta,f)

print('DFA:')
print(f'sigma = {new_sigma}')
print(f'Q = {new_states}')
print(f'delta = {new_delta}')
print(f'F = {new_f}')
