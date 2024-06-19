% Define the diet suggestions for different diseases
diet(sugar_diabetes, 'Eat foods rich in fiber, such as fruits, vegetables, and whole grains. Avoid sugary drinks and processed foods.').
diet(cholesterol, 'Eat foods low in saturated fats, such as lean meats, fish, and vegetables. Avoid fried foods and fatty meats.').
diet(hypertension, 'Eat foods low in sodium, such as fruits, vegetables, and whole grains. Avoid processed foods and canned soups.').
diet(osteoporosis, 'Eat foods rich in calcium and vitamin D, such as dairy products, leafy greens, and fortified foods. Avoid excessive caffeine and alcohol.').
diet(anemia, 'Eat foods rich in iron, such as red meat, spinach, and lentils. Avoid drinking tea or coffee with meals, as they can inhibit iron absorption.').
diet(gastritis, 'Eat foods that are easy to digest, such as bananas, rice, applesauce, and toast. Avoid spicy, acidic, or fatty foods.').

% Predicate to suggest a diet based on a disease
suggest_diet(Disease) :-
    diet(Disease, Diet),
    write('For '), write(Disease), write(', '), nl,
    write('You should: '), nl,
    write(Diet), nl.