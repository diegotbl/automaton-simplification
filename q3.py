import nfa_generator, q1, q2


def regex2nfa(regex):
  """
  Expects a regex as a string and returns a NFA (Σ, Δ, F)
  """
  graph = nfa_generator.Graph(regex)

  sigma = []
  delta = []
  f = []

  for idx, node in enumerate(graph.nodes):
    delta.append([])
    for symbol, node in node.children:
      delta[idx].append((symbol, node.number))
      if not symbol in sigma:
        sigma.append(symbol)  
  
  for node in graph.end:
    f.append(node.number)
  
  return (sigma, delta, f)
  

def enfa2nfa(enfa):
  """
  Expects an eps-NFA (Σ, Δ, F) and returns a NFA (Σ, Δ', F')
  """
  sigma = enfa[0]
  delta = enfa[1]
  f = enfa[2]
  
  eclosures = []
  parents = []
  
  for state in range((len(delta))):
    parents.append([])
  
  for state in range((len(delta))):
    eclosures.append([state])
    for transition in delta[state]:
      parents[transition[1]].append(state)

  def calculate_eclosure(state):
    transitions = delta[state] 
    idx = 0

    while idx < len(transitions):
      if transitions[idx][0] == '&':
        next_state = transitions[idx][1]
        transitions.pop(idx)
        eclosures[state].extend(calculate_eclosure(next_state))
        if next_state in f:
          f.append(state)
      
      else:
        idx += 1      

    return eclosures[state]

  for state in range(len(delta)):    
    calculate_eclosure(state)

  for state in range(len(delta)):
    for transition in delta[state]:
      for estate in eclosures[transition[1]][1:]:
        delta[state].append((transition[0], estate))
        parents[estate].append(state)

    for estate in eclosures[state][1:]:
      for transition in delta[estate]:
        delta[state].append((transition[0], transition[1]))  
        parents[estate].append(state)

  
  for state in range(1, len(delta)):
    if not parents[state]:
      delta[idx] = []

  return (sigma, delta, f)


def nfa2dfa(nfa):
  """
  Expects a NFA (Σ, Δ, F) and returns a minimized DFA (Σ, Q, δ, F)
  """  
  return(q1.nfa2dfa(*nfa))


def regex2dfa(regex):
  """
  Expects a regex as a string and returns a DFA (Σ, Q, δ, F)
  """
  return(nfa2dfa(regex2nfa(regex)))


def enfa2dfa(enfa):
  """
  Expects a eps-NFA (Σ, Δ, F) and returns a minimized DFA (Σ, Q, δ, F)
  """
  return(nfa2dfa(enfa2nfa(enfa)))


def dfa2nfa(dfa):
  """
  Expects a DFA (Σ, Q, δ, F) and enumerates its states assuming the 
  format (Σ, Δ, F)
  """

  sigma = dfa[0]
  states = dfa[1]
  delta = dfa[2]
  f = dfa[3]

  states_map = {tuple(key): value for (value, key) in enumerate(states)}
  
  new_delta = []
  for idx, transitions in enumerate(delta):
    new_delta.append([])
    for transition in transitions:
      new_delta[idx].append((transition[0], states_map[tuple(transition[1])]))
  
  new_f = []
  for state in f:
    new_f.append(states_map[tuple(state)])
  
  return(sigma, new_delta, new_f)


def union_regex(regex1, regex2):
  return regex2dfa(regex1 + '+' + regex2)


def union_dfa(dfa1, dfa2):
  nfa1 = dfa2nfa(dfa1)
  nfa2 = dfa2nfa(dfa2)
  
  new_sigma = list(set(nfa1[0] + nfa2[0]))
  
  nstates1 = len(nfa1[1])
  
  new_delta = [[('&', 1), ( '&', nstates1 + 1)]]
  for idx, transitions in enumerate(nfa1[1]):
    new_delta.append([])
    for transition in transitions:
      new_delta[idx+1].append((transition[0], transition[1] + 1))  

  for idx, transitions in enumerate(nfa2[1]):
    new_delta.append([])
    for transition in transitions:
      new_delta[idx+nstates1+1].append((transition[0], transition[1] + nstates1 + 1)) 
  
  new_f = []

  for state in nfa1[2]:
    new_f.append(state + 1)

  for state in nfa2[2]:
    new_f.append(state + nstates1 + 1)
  
  enfa = [new_sigma, new_delta, new_f]
  return enfa2dfa(enfa)


def complement_dfa(dfa): 
  sigma = dfa[0]
  states = dfa[1]
  delta = dfa[2]
  f = dfa[3]

  new_f = []
  
  for state in states:
    if state not in f:
      new_f.append(state)

  return (sigma, states, delta, new_f)


def complement_regex(regex):
  dfa = regex2dfa(regex)  
  return complement_dfa(dfa)


def complement_nfa(nfa):
  dfa = nfa2dfa(nfa)
  return complement_dfa(dfa)


def intersect_regex(regex1, regex2):
  dfa1 = complement_regex(regex1)
  dfa2 = complement_regex(regex2)

  return complement_dfa(union_dfa(dfa1, dfa2)) 
