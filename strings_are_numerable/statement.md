# Strings are numerable 

An alphabet is a finite set, like for example $\{A,C,G,T\}$ or $\{0,1\}$ or the uppercase characters of the english alphabet.
A string is a finite sequence of characters.
When $\Sigma$ denotes an alphabet, then $\Sigma^k$ denotes the strings of length $k$ over $\Sigma$ (e.g., $\{0,1\}^2 = \{00,01,10,11\}$) and $\Sigma^* := \bigcup_{k \in \mathbf{N}} \Sigma^k$ denotes the set of all possible strings over $\Sigma$.
Notice that whereas $\Sigma$ and $\Sigma^k$ are finite, the set of all possible strings, $\Sigma^*$, is infinite. (Thus you can write and compile a potentially infinite set of different programs, or of different proofs, or statements, or poetry.)

In this exercise we ask you to assess the order of this infinity, proving that $\Sigma^*$ is actually numerable for every $\Sigma$. One way to achieve this is to design a convenient listing of the whole set of the strings.

Write a function that, given a string, returns its position in the above listing.

Write the inverse function that, given a position, returns the string in that position.

Of course, TuringArena will make sure that the two functions are one the invers of the other, thus assessing your proposed enumeration is effective (every integer gets its own place, tht is, function rank is injecetive).
We call them the ranking and the unranking functions.
The ranking function encodes the integer numbers as naturals. The unranking function performs the decoding.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- ???


