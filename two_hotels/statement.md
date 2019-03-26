# Packing the guests of two infinite hotels into just one

John D. Rockerduck and Scrooge McDuck are the richest men in town, which calls them rivals both for the top title and in the chaise for the most rewarding opportunities and bergains.
They both own a money bin filled up with billets and coins, where they practice their daily money swimming, and where the respective number ones hold their very special place.
What is less known, for fiscality reasons, is that they also hold one hotel each having an infinite number of rooms.
Thus, for example, there exists a room~$21351$ both in Rockerduck's hotel and in Scrooge's one, and, similarly, you can find out a room~$n$ in both hotels, for evey natural $n$ you might have thought of.
Both hotels are filled up to completion, none of them has got empty rooms, but it so happens that Rockerduck's hotel must now be closed for a whole month, some say for restructuring reasons but voices are about some fiscal nuisances.
In this occasion, warmly moved in solidarity by these voices, but actually with his own interest, of course, Scrooge McDuck wants to help his rival at his best possible: no one guest of either hotel must remain on the street for one single free night.
Scrooge has asked Gyro Gearloose and his Little Helper to find out how to achieve this task to reaccomodate the guests of the two hotels into a single one.
Little Helper is in charge to assign the generic guest of either hotel with a room of Scrooge's hotel. But we also want to reconstruct, for every room, where its guest comes from. 

Write a function `new_room_number` that, given a natural $n$, and $h\in \{-1,1\}$,
assigns a natural (the new room number in Scrooge's hotel) to the former $n$-th guest in hotel~$h$.

Write two functions,
`former_hotel` and `former_room`,
that, given a natural $n$, keep track of where each guest comes from.

Of course, TuringArena will make sure that the two functions are one the invers of the other.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `injective_new_room_number`.
- `inverse`.

Puoi lasciare dei vecchi ospiti dell'albergo di Scrooge nella loro vecchia stanza? Puoi farlo per un numero infinito di ospiti? Puoi farlo in modo che il programma di valutazione non riscontri che alcun vecchio ospite di Scrooge è stato spostato?
