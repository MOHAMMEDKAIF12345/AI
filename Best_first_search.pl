% Define edges of the graph with their respective costs
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 3).
edge(c, d, 1).
edge(c, e, 5).
edge(d, e, 1).

% Define heuristic values for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 0).

% Best-First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    heuristic(Start, H),
    bfs([(H, 0, Start, [Start])], Goal, Path, Cost).

% Base case: if the first element in the priority queue is the goal
bfs([(_, Cost, Goal, Path) | _], Goal, Path, Cost).

% Recursive case: expand the first node and add its neighbors to the priority queue
bfs([(_, CostSoFar, Node, Path) | Rest], Goal, FinalPath, FinalCost) :-
    findall((H, NewCost, Neighbor, NewPath),
            (edge(Node, Neighbor, EdgeCost),
             \+ member(Neighbor, Path), % avoid cycles
             append(Path, [Neighbor], NewPath),
             NewCost is CostSoFar + EdgeCost,
             heuristic(Neighbor, H)),
            Neighbors),
    append(Rest, Neighbors, NewQueue),
    insertion_sort(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, FinalPath, FinalCost).

% Insertion sort based on heuristic value
insertion_sort(List, Sorted) :- i_sort(List, [], Sorted).
i_sort([], Acc, Acc).
i_sort([(H, C, N, P) | T], Acc, Sorted) :-
    insert((H, C, N, P), Acc, NAcc),
    i_sort(T, NAcc, Sorted).

insert((H, C, N, P), [(H1, C1, N1, P1) | T], [(H1, C1, N1, P1) | NT]) :-
    H > H1, !, 
    insert((H, C, N, P), T, NT).
insert((H, C, N, P), T, [(H, C, N, P) | T]).

% Query example: best_first_search(a, e, Path, Cost).
