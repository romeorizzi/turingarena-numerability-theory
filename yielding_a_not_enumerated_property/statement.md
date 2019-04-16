# There are wide limits to our ambitions

A property of the natural numbers, like "being a prime number", can be regarded as a subset of the numbers (those endoved by the property).
Indeed, the extensability axiom of set theory says precisely this:
a subset of a set can be defined by specifying the filtering out property characterizing the subset within the larger set.
As we saw, the naturals are in 1,1-correspondence with the strings over any alphabet $\Sigma$, and actually this bijection is quite effective (you have realized efficient machines for computing is), thus, considered alaso that machines can be combined, then, when we are interested in studying a specific propery over a set, that is, a specific subset of it, we are actually interested in telling out a subset of $\Sigma^* $ (aka a language, in theoretical computer science terminology).
Ideally, we would like to dispose of a machine for the effective recognition of every possible language, like the language of those strings over $\Sigma = \{0,1\}$ encoding a prime.
Clearly, since the strings are infinite (numerable) also the laguages, that is, the possible subsets of $\Sigma^* $, come in infinite varieties.
Luckily, there is an infinite (numerable) number of finite programs we can write and compile, so maybe we have just enough of them for every possible task.

In this problem we will discover that, unfortunately, there are much more problems than machines available for solving them.

According to Galileo, since science is due to be essoteric, and, being math, and its subsets like computer science, the queen of science, it is a corollary that machines must have a precise univocal and finite description. One should be able to reconstruct them from their description, for no more cold fusions coming about. This is actually a quite weak form of the Church-Turing thesis, and, anyhow, no patent office will patent your amazing machine if you do not provide them with a precise finite description, that is, ultimately, a string.
Thus the machines are enumerable, we have no escape from this.

Your task is to prove that the properies of the naturals (or the languages over an alphabet) are not numerable.
By absurd, we claim that we have produced such enumeration, and you are asked to disporove its validity.

We claim we have enumerated all possible properies as

\[
P_0, P_1, P_2, \ldots
\]

and offer you a machine (a procedure `M(i,n)`) that, when you pass it two natural numbers $i$ and $n$, will answer $1$ if $n\in P_i$ and $0$ otherwise.
You are asked to construct a new property $P$ which is different from any of the properties $\{P_i \; : \; i\in \mathbb{N}$ we listed above, in the sense that, for every $i\in \mathbb{N}$, there exists an $n$ in the symmetric difference $P_i \Delta P$.
We ask you for more, provide us with a machine `P(n)` that, given $n$, returns $n\in P_i$ and $0$ otherwise and help us in our careful checkings as follows:
make sure that, for every $i\in \mathbb{N}$, there exists an $n\leq i$ with $i\in P_i \Delta P$.
Of course, you can query machine`M(i,n)` from within your machine `P(n)`. (These are what we call _callback functions_ in TuringArena terminology.)



### Goals

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- ???.
Inventiamoci sfide belle ed interessanti che esplorino eventuali questioni naturali.
