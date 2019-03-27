import random

import turingarena as ta

NUM_MACHINES = 100

for tc in range(7):
    memoM = []
    for i in range(0,NUM_MACHINES):
        memoM.append([random.randint(0, 1) for _ in range(0,NUM_MACHINES)])
        for n in range(0,i+1):
            memoM[i][n] =  1 - memoM[n][n]
    if tc % 3: 
        random.shuffle(memoM)
    if tc % 2:
        perm = list(range(0,NUM_MACHINES))
        random.shuffle(perm)
        for i in range(0,NUM_MACHINES):
            bits_to_be_permuted = memoM[i][:]
            for n in range(0,NUM_MACHINES):
                memoM[i][n] = bits_to_be_permuted[perm[n]]

    memoP = []
    for n in range(0,NUM_MACHINES):
        with ta.run_algorithm(ta.submission.source) as process:
            def M(i, n):
                return memoM[i][n] 
            try:
                memoP.append(process.functions.P(n, callbacks = [M]))
            except ta.AlgorithmError as e:
                ta.goals["correct"] = False
                print(e)
        print(f"Your P({n}) = {memoP[n]}")

    P_is_new = True
    first_n_diff = None
    for i in range(0,NUM_MACHINES):
        P_and_Pi_differ = False
        for j in range(0,i+1):
            if memoM[i][j] != memoP[j]:
                P_and_Pi_differ = True
                first_n_diff = j
                break
        if P_and_Pi_differ:
            print(f"The first diff with machine P_{i} is on the natural {first_n_diff}. Here, P({first_n_diff}) = {memoP[first_n_diff]} whereas P({i}) = {memoM[i][first_n_diff]}")
        else:
            ta.goals.setdefault("correct", False)
            print(f"NO: your property P coincides with our property P_{i} for all n <= {i}. Indeed, P[0..{i}] = {memoP[:i+1]} and P_{i}[0..{i}] = {memoM[i][:i+1]}")
        
ta.goals.setdefault("correct", True)
print(ta.goals)

