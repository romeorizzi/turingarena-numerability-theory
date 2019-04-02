# Integers are numerable 

Every natural number is an integer, but the opposite is not true.
With this, you might be lead to belive that there are more integer numbers than natural ones.
However, Cantor tought us that, in a certain sense, this is not that true, after all.
According to Cantor the infinite set of the naturals and the infinite set of the integers are equicardinal in that there is a 1,1-correspondence between the two.
In this way, you can name all the integers as:
the first integer (the one in 1,1-correspondence with $0$), the second one (the one in 1,1-correspondence with $1$), and so forth, ...

that is, you can (e)numerate the integers one by one.

Write a function that, given an integer, returns its position in the above listing.

Write the inverse function that, given a position, returns the integer in that position.

Of course, TuringArena will make sure that the two functions are one the invers of the other, thus assessing your proposed enumeration is effective (every integer gets its own place, tht is, function rank is injecetive).
We call them the ranking and the unranking functions.
The ranking function encodes the integer numbers as naturals. The unranking function performs the decoding.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `correct`: $N<=1000$, $|Z| \leq 500$.


