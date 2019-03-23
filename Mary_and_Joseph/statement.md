# Mary and Joseph

When we count the elements of a finite set $S$, one by one,
we establish a bijection (or $1,1$-correspondence) between the elements of $S$
 and a prefix $1,2,3,\ldots , n$ of the infinite sequence $1,2,3,\ldots $ comprising the positive natural numbers. Then we call $n$, the number where we stopped,  the cardinality of $S$ and denote it by $|S|$.
Since bijections are invertible and compose into bijections, then two finite sets have the same cardinality iff there is a bijection between them.
Cantor extended this notion of equicardinality to infinite sets: what tells whether two sets are of the same cardinality is whether there exists a bijection between them.
It so happens for finite sets that dropping some elements inevitably reduces its cardinality by the precise number of elements dropped.
The first puzzling issue about infinite sets is whether a set $T$ could be of the same cardinality as a proper subset $S\subsetneq T$. 

Some time ago there was a couple in visit of a foreign city for resolving some burocratic issues, she was pregnant, but they had no place where to stay for the night. The city had an incredible hotel, with an infinite number of rooms, and when I say infinite, I mean it literally. They had a room for every natural number starting from $0$.
Just say a number ... Hm 423124? They had room~$423124$, and any other you might ask for.

Unfortunately, there was big movement in those days, or maybe the couple was not that nicely dressed, so they were told that every room was already taken.

CLearly, is not good policy for an hotel to trow out a guest to let in somebody else, but the true question is: couldn't they have rearranged the guests so that each one would have been assigned some new room and yet a room would have got free for guesting the newcomer family?

Can you help here designing a $1,1$-correspondence between the set $\mathbf{N}$ of the natural numbers and its proper subset $\mathbf{N}_0 := \mathbf{N} \setminus \{0\}$ obained from it by dropping number $0$. Can you let room numbered $0$ free for the holy couple in the holy night?

Write a function $f$ that given a natural in $\mathbf{N}$ assigns to it a new room in $\mathbf{N}\setminus \{0\}$, making sure that $f(n_1) = f(n_2)$ implies $n_1 = n_2$, that is, making sure no two previous guests are mapped into the same room.
Prove that your function owns the required injectivity property by also offering the inverse function $f^{-1}$.

TuringArena will check whether the two functions `f` and `f_inv`  you will offer (with quite some freedom) are indeed the inverse one of the other. In other words, we will also check whether $f$ is surjective, though injectivity is really the key issue here.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `room_zero_made_free`: $f(n) \neq 0$ for every $n\in \mathbf{N}$.
- `bijectivity`: `f` and `f_inv` are indeed inverse functions. 
- `injectivity`: $f(n_1) = f(n_2)$ implies $n_1 = n_2$.
- `surjectivity`: for every $n'\in $\mathbf{N}_0$ there exists an $n\in $\mathbf{N}$ such that $f(n) = n'$.

Moreover, if you can, let $f(n) = n$ for as many numbers as possible. Can you let $f(n) = n$ for an infinite number of $n$'s?
This corresponds to the following goals:

- `all_declared_fixed_points_are_correct`
- `all_declared_fixed_points_are_different`
- `declared_some_fixed_points`
- `declared_fixed_points_for_every_index`

To avoid declaring a fixed point return -1 in function `fixed_point_num(index)`. 
