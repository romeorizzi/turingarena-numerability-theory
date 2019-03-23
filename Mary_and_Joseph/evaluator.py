import random
import numpy as np

import turingarena as ta

fixed_points = []
for n in list(range(20)) + list(np.random.choice(range(20,1000000),100)):
    try:
        with ta.run_algorithm(ta.submission.source) as process:
            fp = process.functions.fixed_point_num(n)
            m = process.functions.f(n)
            nn = process.functions.f_inv(m)
    except ta.AlgorithmError as e:
        ta.goals["room_zero_made_free"] = False
        ta.goals["bijectivity"] = False
        ta.goals["declared_fixed_points_for_every_index"] = False
        print(e)
    if m == 0:
       ta.goals.setdefault("room_zero_made_free", False)
       print(f"Pias menga! Abbiamo verificato che f({n}) = {m}. La tua riallocazione degli ospiti non riesce quindi a liberare la stanza numero zero.")        
    elif n == nn:
       print(f"Bijectivity OK! Hai codificato in numero intero {n} nel numero naturale {m} e la tua decodifica ti ha correttamente decodificato {m} come {nn}")
    else:
       ta.goals.setdefault("bijectivity", False)
       print(f"Pias menga! Abbiamo verificato che f({n}) = {m} mentre f_inv({m}) = {nn} e come vedi {nn} != {n}.")
    if fp >= 0:
        ta.goals.setdefault("declared_fixed_points_for_some_index", True)
        if fp in fixed_points:
            ta.goals.setdefault("all_declared_fixed_points_are_different", False)
            print(f"fixed_point_num({n}) = {fp}. Mhhh ... . Mi stai offrendo lo stesso fixed point per due indici diversi. Pias menga!")
        else:
            fixed_points.append(fp)
    else:
        ta.goals.setdefault("declared_fixed_points_for_every_index", False)

for n in fixed_points:
    try:
        with ta.run_algorithm(ta.submission.source) as process:
            trash = process.functions.fixed_point_num(n)
            m = process.functions.f(n)
            nn = process.functions.f_inv(m)
    except ta.AlgorithmError as e:
        ta.goals["avoid-moving-all"] = False
        print(e)
    if m==n:
       print(f"Fixed point {n} checked! It holds indeed that f({n}) = {n}.")
    else:
       ta.goals["all_declared_fixed_points_are_correct"] = False
       print(f"Problem! You have listed {n} among the fixed point of f. However, f({n}) = {m}.")        
    if m == 0:
       ta.goals.setdefault("room_zero_made_free", False)
       print(f"Pias menga! Abbiamo verificato che f({n}) = {m}. La tua riallocazione degli ospiti non riesce quindi a liberare la stanza numero zero.")        
    elif n == nn:
       print(f"Bijectivity OK! Hai codificato in numero intero {n} nel numero naturale {m} e la tua decodifica ti ha correttamente decodificato {m} come {nn}")
    else:
       ta.goals.setdefault("bijectivity", False)
       print(f"Pias menga! Abbiamo verificato che f({n}) = {m} mentre f_inv({m}) = {nn} e come vedi {nn} != {n}.")    
        
ta.goals.setdefault("room_zero_made_free", True)
ta.goals.setdefault("bijectivity", True)
ta.goals.setdefault("all_declared_fixed_points_are_correct", True)
ta.goals.setdefault("declared_fixed_points_for_every_index", True)
ta.goals.setdefault("declared_fixed_points_for_some_index", False)

print(ta.goals)

