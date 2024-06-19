person('John Doe', '1980-05-15').
person('Jane Smith', '1992-11-23').
person('Alice Johnson', '1985-01-30').
person('Bob Brown', '1979-07-22').

find_dob(Name, DOB) :-
    person(Name, DOB).

find_name(DOB, Name) :-
    person(Name, DOB).
