# Mary and Joseph

When we count the elements of a finite set $S$, one by one,
we establish a bijection (or $1,1$-correspondence) between the elements of $S$
 and a prefix $1,2,3,\ldots , n$ of the infinite sequence $1,2,3,\ldots$
 comprising the positive natural numbers enlisted in their usual order. Then we call $n$, the number where we stopped,  the cardinality of $S$ and denote it by $|S|$.
Since bijections are invertible and compose into bijections, then two finite sets have the same cardinality iff there is a bijection between them.
Cantor extended this notion of equicardinality to infinite sets: what tells whether two sets are of the same cardinality is whether there exists a bijection between them.
It so happens for finite sets that dropping some elements inevitably reduces its cardinality by the precise number of elements dropped.
The first puzzling issue about infinite sets is whether a set $T$ could be of the same cardinality as a proper subset $S\subsetneq T$.

Some time ago there was a couple in visit of a foreign city for resolving some burocratic issues, she was pregnant, but they had no place where to stay for the night. The city had an incredible hotel, with an infinite number of rooms, and when I say infinite, I mean it literally. They had a room for every natural number starting from $0$.
Just say a number ... Hm 423124? They had room~$423124$, and any other you might ask for.

Unfortunately, there was big movement in those days, or maybe the couple was not that nicely dressed, so they were told that every room was already taken.

CLearly, is not good policy for an hotel to trow out a guest to let in somebody else, but the true question is: couldn't they have rearranged the guests so that each one would have been assigned some new room and yet a room would have got free for guesting the newcomer family?

Can you help here designing a $1,1$-correspondence between the set $\mathbf{N}$ of the natural numbers and its proper subset $\mathbf{N}_0 := \mathbf{N} \setminus \{0\}$ obained from it by dropping number $0$. Can you let room numbered $0$ free for the holy couple in the holy night?

Write a function $f$ that given a natural $n$ in $\mathbf{N}$ assigns to the guest originally placed in room $n$ a new room $f(n)$ in $\mathbf{N}\setminus \{0\}$.
Make sure that your function $f$ is *injective*, tat is, $f(n_1) = f(n_2)$ implies $n_1 = n_2$. In other words, make sure that no two previous guests are mapped into the same room. Also, make sure to let room $0$ free.
Prove that your function owns the required injectivity property by also offering the inverse function $f^{-1}$.

TuringArena will check whether the two functions `f` and `f_inv`  you will offer (with quite some freedom) are indeed the inverse one of the other. In other words, we will also check whether $f$ is surjective, though injectivity is really the key issue here.


# Maria e Giuseppe

Quando contiamo gli elementi di un insieme finito $S$, uno ad uno,
stiamo stabilendo una biezione (una corrispondenza uno ad uno, anche detta una $1,1$-corrispondenza) tra gli elementi di $S$ ed un prefisso $1,2,3,\ldots , n$ della sequenza infinita $1,2,3,\ldots $ dei numeri naturali positivi elencati nel loro solito ordine. Poi, dove $n$ è il numero naturale col quale ci siamo arrestati avendo esaurito gli elementi in $S$, concludiamo che la cardinalità di $S$ (ossia il numero di elementi contenuti in $S$) è $n$.
La cardinalità di un insieme $S$ viene sovente indicata scrivendo $|S|$.
Poichè le funzioni biunivoce sono invertibili e quando composte danno luogo a nuove biezioni, allora due insiemi finiti hanno la stessa cardinalità se e solo se esiste una $1,1$-corrispondenzatra tra di loro che consenta di vedere gli elementi dell'uno come meri rappresentanti degli elementi dell'altro.
Cantor estese questa nozione di equicardinalità agli insiemi infiniti:
due insiemi (finiti od infiniti che siano) hanno per noi la stessa cardinalità se e solo se esiste una biezione tra di loro.
E' un fatto che quando rimuoviamo un elemento da un insieme finito la sua cardinalità cala precisamente del numero di elementi rimossi.
La prima osservazione spiazzante è che invece, passando a considerare insiemi infiniti, possa benissimo accadere che un insieme $T$ sia equicardinale ad un suo sottoinsieme proprio $S\subsetneq T$.

Qualche tempo fa una coppia che si era portata in un'altra città per risolvere delle questioni burocratiche legate ad un censimento si ritrovò a non avere un posto dove passare la notte, e lei era incinta.
La città vantava un hotel incredibile, con un numero infinito di stanze, e quando dico infinito va inteso in senso letterale. L'hotel disponeva di una stanza per ogni numero che vi possa venire in mente, a partire dallo $0$. Una per ogni numero naturale quindi. Provate a dire un numero ... Hm 423124? Ebbene ecco la chiave della $423124$. Essi avevano davvero la stanza~$423124$, e così per ogni altro numero naturale che vi possa venire in mente di chiedere.

Sfortunatamente c'era un grande via vai in quei giorni, o forse la coppia apparve vestita in modo non adeguato per un hotel così prestigioso, e così venne detto loro che in quel momento ogni singola stanza era già occupata.

In effetti non sarebbe politica opportuna per un hotel buttare fuori degli ospiti per farne entrare altri, ma la vera questione quì è:
non avrebbero potuto spostare gli ospiti di stanza in stanza rimappandoli in modo tale da liberarne una, ed al tempo stesso evitando di mettere due ospiti provenienti da stanze diverse dentro una stessa stanza?

Puoi aiutare nel progettare e realizzare una $1,1$-corrispondenza tra l'insieme $\mathbf{N}$ dei numeri naturali ed il suo sottoinsieme proprio $\mathbf{N}_0 := \mathbf{N} \setminus \{0\}$ ottenuto da esso rimuovendo il numero~$0$? Potresti liberare la stanza numero~$0$ per ospitare la sacra famiglia nella notte santa?

Scrivi una funzione $f$ che mappi ogni numero naturale preso da $\mathbf{N}$ in una nuova stanze in $\mathbf{N}\setminus \{0\}$, assicurandoti che $f(n_1) = f(n_2)$ possa valere solo quando $n_1 = n_2$, ossia, assicurandoti che che non ci siano due vecchi ospiti che vadano a ritrovarsi in una stessa stanza.
Confermaci che la tua funzione $f$ possiede tale proprietà di iniettività che ti richiediamo offrendoci inoltre la sua funzione inversa $f^{-1}$ che avremo modo di verificare.

TuringArena controllerà se la funzione `f_inv` applicata a `f`$(n)$ è in grado di ricostruire $n$, ossia di riportare l'ospite $n$, che ora si trova nella stanza `f`$(n)$, alla sua stanza originaria `f_inv`(`f`$(n)$). Questo ci consente di verificare in modo operativo che la `f` da te proposta è effettivamente iniettiva.
Anche se l'iniettività della `f` è in realtà il solo aspetto che ci preme davvero in questo contesto (se poi vuoi liberare ulteriori stanza per i re magi tanto meglio) abbiamo previsto anche un *goal* dove verifichiamo se la `f` ci appare suriettiva, cosa che ci sarà più facile controllare andando a vedere se `f_inv` è definita per ogni numero naturale positivo.



### Goals

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `room_zero_made_free`: $f(n) \neq 0$ for every $n\in \mathbf{N}$.
- `bijectivity`: `f` and `f_inv` are indeed inverse functions.
- `injectivity`: $f(n_1) = f(n_2)$ implies $n_1 = n_2$.
- `surjectivity`: for every $n'\in $\mathbf{N}_0$ there exists an $n\in $\mathbf{N}$ such that $f(n) = n'$.

Moreover, if you can, let $f(n) = n$ for as many numbers as possible. Can you let $f(n) = n$ for an infinite number of $n$'s?
Suppose you coud design an $f$ with $5$ fixed points, let them be $7$, 14$, $5$, $3$, and $21$, taken in some order. Then implement `fixed_point_num`$(i)$ do that it returns the $(i+1)$-th fixed point for $i=0,1,2,3,4$ and $-1$ for $i > 4$.
That is:

* `fixed_point_num`$(0) = 7$
* `fixed_point_num`$(1) = 14$
* `fixed_point_num`$(2) = 5$
* `fixed_point_num`$(3) = 3$
* `fixed_point_num`$(4) = 21$

You are not allowed to sell a same fixed point twice: to avoid declaring a fixed point return -1 in function `fixed_point_num(i)`.

In this way you can also go for the following goals:

- `all_declared_fixed_points_are_correct`
- `all_declared_fixed_points_are_different`
- `declared_some_fixed_points`
- `declared_fixed_points_for_every_index`

The last goal means that you could allow to an infinite number of guests the benefit to stay in their old room.
