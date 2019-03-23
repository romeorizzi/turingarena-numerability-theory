import random

import turingarena as ta

for _ in range(10):
    z = random.randint(-500, 500)

    try:
        with ta.run_algorithm(ta.submission.source) as process:
            n = process.functions.rank(z)
            zz = process.functions.unrank(n)
    except ta.AlgorithmError as e:
        ta.goals["correct"] = False
        print(e)
    if z == zz:
       print(f"Correct! Hai codificato in numero intero {z} nel numero naturale {n} e la tua decodifica ti ha correttamente decodificato {z}")
    else:
       print(f"PIas menga! Hai codificato in numero intero {z} nel numero naturale {n} ma poi, mi decodifichi {n} come  {zz}")
        
ta.goals.setdefault("correct", True)
