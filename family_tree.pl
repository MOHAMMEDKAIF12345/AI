% Define family relationships
parent(john, 'mary').
parent(john, 'bob').
parent('mary', 'anne').
parent('mary', 'susan').
parent('bob', 'lily').
parent('bob', 'jack').
parent('jack', 'joe').

% Rules to define different relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

child(Child, Parent) :-
    parent(Parent, Child).

grandparent(GP, GC) :-
    parent(GP, Parent),
    parent(Parent, GC).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediary),
    ancestor(Intermediary, Descendant).

% Define genders
male('john').
male('bob').
male('jack').
male('joe').

female('mary').
female('anne').
female('susan').
female('lily').
