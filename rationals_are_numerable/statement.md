# Rationals are numerable 

We say that a set $S$ is (e)numerable when we can list its elements one by one, making sure that every single element will be reached soon or later.
As such, the question is whether we can design a machine or process that yields and outputs the elements of $S$ one by one.
Thinking in terms of machines may facilitate the task of proving the numerability of certain sets.
Indeed, suppose we already have a machine for enumerating the elements of a superset $T$ of $S$ and a second machine $F$ which, given an element of $T$, recognizes in finite time whether it belongs also to $S$ or not.
Then we can compose the two machines placing them in cascade, the first will yield the elements of $T$ and send out them in streaming, the second will take in this stream, one element at the time, and will act as a filter streaming out only the elements of $S$.
Since we assumed that every element of $T$ will, soon or later, be produced by the first machine, then every element of $S\subseteq T$ will soon or later come out by the composed machine.
We already said that in order to prove the numerability of a set it suffices to find out an injective function from it to the naturals.
But this machine designing approach offers a second advantage:
it is not a problem if some (or all) of the elements of $S$ get streamed out more thano once: as long as every element of $S$ is streamed out soon or later then we can conclude that $S$ is numerable.
Indeed, numerability is the lowest degree of infinity into Cantor's gallery of the infinites.


Write a function that streams out all the rational numbers (as pairs of integers, the first is the numerator and the second is the denominator).

Give a machine that streams them out only when they are in some reasonable canonical form. For example, avoid to have both the numerator and the denominator among the negative numbers. Even better: there is no need to use negative numbers for the denominator.

Filter them more: write a filter machine that lets a pair $(N,D)$ go only if $N$ and $D$ are relatively prime.
Combining the two machines we will get a precise enumeration of the rationals.

Write a single machine that directly enumerates the rationals precisely, that is, not only every rational will come out soon or later but also non natural will ever be repeated.



### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- ???.
Inventiamoci sfide belle ed interessanti che esplorino eventuali questioni naturali.


