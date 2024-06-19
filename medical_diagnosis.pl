% Symptoms
symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, sore_throat).
symptom(jane, cough).
symptom(mary, fever).
symptom(mary, cough).
symptom(mary, fatigue).

% Rules for diagnosis
diagnosis(Patient, influenza) :-
    symptom(Patient, fever),
    symptom(Patient, cough).
diagnosis(Patient, common_cold) :-
    symptom(Patient, headache),
    symptom(Patient, sore_throat),
    symptom(Patient, cough).
diagnosis(Patient, unknown) :-
    \+ diagnosis(Patient, influenza),
    \+ diagnosis(Patient, common_cold).


