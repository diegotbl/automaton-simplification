def nfa2dfa(*nfa):
  """Expects NFA to be in a (Sigma, Delta, F), where Sigma is a a list with the symbols
  of the alphabet, like [a, b]; Delta is the transistion function, specified as
  a list of lists of tuples, like [[(a,0), (b,1)], [(a,1), (b,1)]] - where 0 and
  1 are the states and 'a' and 'b' are the symbols, this means that if the tape
  is in state 0 and receives an 'a' it will go to state 0 again and if it recei-
  ves a 'b' it will go to state 1, and if the state is 1 it remains 1; and F is
  a list with the final states, like [1]. The states are assumed to be from 0
  to len(Delta), with 0 being the initial state. The function returns (Sigma, Q, delta, F),
  which represents the equivalent DFA with a format identical to the one
  described here."""

  sigma = nfa[0]
  delta = nfa[1]
  f = nfa[2]

  new_sigma = sigma
  new_delta = []
  new_f = []

  new_states = [[0]]
  computed = [[0]]

  # Computes the DFA using the powerset construction
  for new_state in new_states:
    final = False
    new_delta.append([])
    for symbol in sigma:
      next_state = set()
      for state in new_state:
        for transition in delta[state]:
          if transition[0] == symbol:
            next_state.add(transition[1])
            if transition[1] in f:
              final = True

      next_state = list(next_state)
      new_delta[-1].append((symbol, next_state))
      if not (next_state in computed):
        computed.append(next_state)
        new_states.append(next_state)
        if final:
          new_f.append(next_state)

  if 0 in f:
    new_f.insert(0,[0])

  return (new_sigma, new_states, new_delta, new_f)
