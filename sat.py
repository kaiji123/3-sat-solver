from pysat.formula import CNF
from pysat.solvers import Glucose3
from pysat.solvers import Solver, Minisat22
# Create a CNF formula
formula = CNF()

# Add clauses to the formula
clause1 = [1, 2, -3]
clause2 = [-1, 3, -4]
clause3 = [1, 3, -4]
print(formula.clauses ==[])
formula.append(clause1)
formula.append(clause2)
formula.append(clause3)
print(formula.clauses ==[])

assignment = {}
import os
print(os.getcwd())
cnf1 = CNF()

cnf1.from_file('./data/uf20-01.cnf')
print(cnf1.clauses)
formula = cnf1
while True:
    min_level = 10000
    for clause in formula.clauses:
        print(clause)
        if len(clause) < min_level :
            min_level = len(clause)

    dictio = {}
    for clause in formula.clauses:
        print(clause)
        if len(clause) == min_level :
            vars = set(clause)
    for i in vars :
        dictio[i] =0
        dictio[-i]=0
    for clause in formula.clauses:
        for var in clause:
            if var in dictio:
                dictio[var] += 1
    
    print(dictio)



    # Find the key with the maximum value
    print(dictio)
    print(formula.clauses)
    key_with_max_value = max(dictio, key=dictio.get)
   
    assignment[abs(key_with_max_value)] = (key_with_max_value > 0)
    print(key_with_max_value)  # Output: 'David'
    new_formula = CNF()

    # removing the occurences of variable if positive skip the clause if negative remove variable else add whole clause
    for clause in formula.clauses:
        if key_with_max_value in clause:
            continue
        elif -key_with_max_value in clause :
            clause.remove(-key_with_max_value)
            if clause != []:
        
                new_formula.append(clause)
        else:
            new_formula.append(clause)
    formula = new_formula
    if formula.clauses ==[]:
        break
    
print(assignment)
# Solve and check satisfiability
s = Solver(name='g4')

# s.solve(formula)

# # Print the result
# if is_satisfiable:
#     print("SATISFIABLE")
#     variable_assignments = solver.get_model()
#     print("Variable Assignments:", variable_assignments)
# else:
#     print("UNSATISFIABLE")

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



# Specify the number of variables and clauses for the random formula
num_variables = 10
num_clauses = 20

# Create a random formula
formula = CNF()
print(formula)






# from pysat.formula import CNF
# import random

# # Specify the number of variables and clauses for the random formula
# num_variables = 10
# num_clauses = 20

# # Create a random formula
# formula = CNF()

# for _ in range(num_clauses):
#     clause = []
#     for _ in range(random.randint(1, num_variables)):
#         # Randomly generate positive or negative literal
#         literal = random.choice([random.randint(1, num_variables), -random.randint(1, num_variables)])
#         clause.append(literal)
#     formula.append(clause)

# # Print the generated formula
# print(formula.clauses)

