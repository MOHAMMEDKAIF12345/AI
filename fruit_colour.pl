% Facts defining the color of various fruits
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(lemon, yellow).

% Rule to find the color of a given fruit
find_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

