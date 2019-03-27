# Packing the guests of an infinite number of infinite hotels into just one

Nowadays the richest are becoming even richer.
It so happens that Scrooge McDuck now owns a different hotel for each one of the natural numbers. And each one of these hotels has a different room for each one of the natural numbers.
Since living beings have been turned in (possibly virtual) machines, all these hotels are full, that is, each room has got its own guest. 
For tax reasons, and for reducing the expenses, Scrooge wants to close up all its hotels without loosing any one of his paying guests.


Write a function `new_room_number` that, given two naturals $n$ and $h$,
assigns a natural (the new room number in Scrooge's hotel Number One) to the former $n$-th guest from hotel~$h$.

Write two functions,
`former_hotel` and `former_room`,
that, given a natural $n$, keep track of where each guest comes from.

Of course, TuringArena will make sure that the two functions are one the invers of the other.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `injective_new_room_number`.
- `inverse`.

Puoi lasciare dei vecchi ospiti dell'albergo mantenuto attivo da Scrooge nella loro vecchia stanza? Puoi farlo per un numero infinito di ospiti? Puoi farlo in modo che il programma di valutazione utilizzato da TuringArena non riscontri che alcun vecchio ospite di Scrooge è stato spostato?
