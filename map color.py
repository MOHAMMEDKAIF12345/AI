def select_unassigned_variable(assignment, variables):
    for variable in variables:
        if variable not in assignment:
            return variable
    return None

def is_consistent(assignment, variable, value, constraints):
    for neighbor in constraints[variable]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def backtrack(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment
    
    variable = select_unassigned_variable(assignment, variables)
    for value in domains[variable]:
        if is_consistent(assignment, variable, value, constraints):
            assignment[variable] = value
            result = backtrack(assignment, variables, domains, constraints)
            if result is not None:
                return result
            del assignment[variable]
    
    return None

def map_coloring(variables, domains, constraints):
    assignment = {}
    return backtrack(assignment, variables, domains, constraints)

if __name__ == "__main__":
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

    domains = {
        "WA": ["Red", "Green", "Blue"],
        "NT": ["Red", "Green", "Blue"],
        "SA": ["Red", "Green", "Blue"],
        "Q": ["Red", "Green", "Blue"],
        "NSW": ["Red", "Green", "Blue"],
        "V": ["Red", "Green", "Blue"],
        "T": ["Red", "Green", "Blue"]
    }

    constraints = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }
    
    solution = map_coloring(variables, domains, constraints)
    
    if solution:
        print("Solution found:")
        for region in solution:
            print(f"{region}: {solution[region]}")
    else:
        print("No solution found")
