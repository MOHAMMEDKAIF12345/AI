% Define the database with facts for name and DOB.
person('John Doe', '1980-05-15').
person('Jane Smith', '1992-11-23').
person('Alice Johnson', '1985-01-30').
person('Bob Brown', '1979-07-22').

% Query to find a person's DOB given their name.
find_dob(Name, DOB) :-
    person(Name, DOB).

% Query to find a person's name given their DOB.
find_name(DOB, Name) :-
    person(Name, DOB).