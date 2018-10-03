def dfa_minimization(dfa):
    """
    :param dfa: tuple containing Sigma, Q, delta, F as specified at q1.py
    :return: tuple containing Sigma, Q', delta', F'
    """

    sigma = dfa[0]
    q = dfa[1]
    delta = dfa[2]
    f = dfa[3]

    d = indistinguishable(sigma, q, delta, f)

    new_sigma = sigma
    new_delta = []
    new_f = f.copy()
    new_q = q.copy()
    aux_delta = delta.copy()

    # Percorrer d. Quando achar um 0 concatenar os estados e alterar o delta. Se esses estados forem finais, alterar f
    for i, state in enumerate(new_q):
        new_q[i] = [state]

    for transitions in aux_delta:
        for i, t in enumerate(transitions):
            aux = list(t)
            aux[1] = [aux[1]]
            aux = tuple(aux)
            transitions[i] = aux

    for i, final in enumerate(new_f):
        new_f[i] = [final]

    for i, state in enumerate(q):
        for j in range(i):
            if d[i][j] == 0:
                eq1 = []
                eq2 = []
                for eq in new_q:
                    if q[i] in eq:
                        new_q.remove(eq)
                        eq1 = eq
                  
                    elif q[j] in eq:
                        new_q.remove(eq)
                        eq2 = eq
                
                new_eq = eq1 + eq2
                new_q.append(new_eq)

                for transition in aux_delta:
                        for index, t in enumerate(transition):
                            if t[1] == eq1 or t[1] == eq2:
                                aux = list(t)
                                aux[1] = new_eq
                                aux = tuple(aux)
                                transition[index] = aux

                for final in f:
                    if state == final:
                        if eq1 in new_f:
                          new_f.remove(eq1)
                        if eq2 in new_f:
                           new_f.remove(eq2)
                        new_f.append(new_eq)

    for eq in new_q:
        transitions = []
        for state in eq:
            transitions.extend(aux_delta[q.index(state)]) 
        new_delta.append(transitions)

    # Eliminate repeated transitions in new_delta
    for transitions in new_delta:
        while len(transitions) > len(new_sigma):
            transitions.pop()

    return (new_sigma, new_q, new_delta, new_f)
 

def indistinguishable(sigma, q, delta, f):
    """
    Executes algorithm to find equivalent states on DFA
    :param sigma: alphabet
    :param q: all states
    :param delta: transitions
    :param f: final accepted states
    :return: Matrix d to determine which states are distinguishable and which aren't
    """

    # Step 1: Initialization
    d = [[0 for j in range(i)] for i, state in enumerate(q)]
    s = [[[] for j in range(i)] for i, state in enumerate(q)]

    # Step 2: For every pair (i, j) with i > j, if one of these states is an accepting state and the other is not an
    # accepting state, set D[i, j] = 1
    for i, state in enumerate(q):
        for j in range(i):
            if ((state not in f) and (q[j] in f)) or ((q[j] not in f) and (state in f)):
                d[i][j] = 1

    # Step 3: Add states to S and finish updating D
    for i, state in enumerate(q):
        for j in range(i):
            if d[i][j] == 0:
                # 3.1
                flag = 0
                for symbol in sigma:
                    delta_state = delta[i]
                    for transition in delta_state:
                        if transition[0] == symbol:
                            m = q.index(transition[1])
                    delta_state = delta[j]
                    for transition in delta_state:
                        if transition[0] == symbol:
                            n = q.index(transition[1])
                    # to avoid range problems
                    m2 = m
                    n2 = n
                    if m < n:
                        m2 = n
                        n2 = m

                    if m2 != n2:
                        if d[m2][n2] == 1:
                            dist(i, j, d, s)
                            flag = 1
                            break

                for symbol in sigma:
                    delta_state = delta[i]
                    for transition in delta_state:
                        if transition[0] == symbol:
                            m = q.index(transition[1])
                    delta_state = delta[j]
                    for transition in delta_state:
                        if transition[0] == symbol:
                            n = q.index(transition[1])
                    if flag == 0:
                        if j != m < n != i:
                            s[n][m].append([i, j])
                        elif i != m > n != j:
                            s[m][n].append([i, j])

    return d


def dist(i, j, d, s):
    """
    Checks if the states i end j are distinguishable and fills D with 1's
    :param i: state index
    :param j: another state index
    :param d: distinguishability matrix
    :param s: the 'other' matrix
    :return: Updated matrix D
    """

    d[i][j] = 1
    for [m, n] in s[i][j]:
        d = dist(m, n, d, s)
    return d
