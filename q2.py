def dfa_minimization(dfa):
    """
    :param dfa: tuple containing Σ, Q, δ, F as specified at q1.py
    :return: tuple containing Σ, Q', δ', F'
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
    for i, state in enumerate(q):
        for j in range(i):
            if d[i][j] == 0:
                new_q.remove(q[i])
                new_q.remove(q[j])
                new_q.append([q[i], q[j]])

                for transition in aux_delta:
                    for index, t in enumerate(transition):
                        if t[1] == q[i] or t[1] == q[j]:
                            aux = list(t)
                            aux[1] = [q[i], q[j]]
                            aux = tuple(aux)
                            transition[index] = aux

                for final in f:
                    if state == final:
                        new_f.remove(q[i])
                        new_f.remove(q[j])
                        new_f.append([q[i], q[j]])

    for new_state in new_q:
        if new_state not in q:
            new_delta.append(aux_delta[new_state[0][0]])
        elif new_state in q:
            new_delta.append(aux_delta[q.index(new_state)])

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

    # Step 2: For every pair (i, j) with i < j, if one of these states is an accepting state and the other is not an
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
                if flag == 0:
                    if i != m < n != j:
                        s[n][m].append([i, j])
                    elif j != m > n != i:
                        s[m][n].append([i, j])

    print(d)
    iterate = [x for x in range(len(q))]
    del iterate[0]
    for index in iterate:
        if d[index][0] == 0:
            print("This case may cause some problem! Please change q's and delta's original order")

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
