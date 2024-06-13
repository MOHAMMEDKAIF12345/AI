can_fly(hawk).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

can_fly_bird(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.'),
    nl.
can_fly_bird(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.'),
    nl.