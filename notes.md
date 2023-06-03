clauses of smaller size are more important and try to make the first assignment truthful
you don't want to leave the truthful assignment for the last
it is also like independent set problem - but we think it is inefficient, we can give counterexample that sat is not independent set but is satisfiable
once you make first truthful assignment eg x1 remove all the clause that has x1 in it, for the clauses that have !x1, we keep it but trim it to make a shorter clause, then we look for shortest clause and try to make the first assignment truthful
try to count the number of negatives and positives if the number of variables in clauses are equal, in order words choose the one variable that has most truth values on shortest level


we will also assume the minimality of clauses meaning one variable can only have positive and negative once 


```py
from pysat.formula import CNF
from pysat.solvers import Glucose3

# Create a CNF formula
formula = CNF()

# Add clauses to the formula
clause1 = [1, 2, -3]
clause2 = [-1, 3, -4]
formula.append(clause1)
formula.append(clause2)

# Solve and check satisfiability
solver = Glucose3()
is_satisfiable = solver.solve(formula)

# Print the result
if is_satisfiable:
    print("SATISFIABLE")
    variable_assignments = solver.get_model()
    print("Variable Assignments:", variable_assignments)
else:
    print("UNSATISFIABLE")

def is_satisfiable(formula, assignment):
    for clause in formula:
        clause_satisfied = False
        for literal in clause:
            variable, polarity = abs(literal), literal > 0
            if assignment[variable] == polarity:
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True
```