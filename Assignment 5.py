# Step 1: Import necessary libraries
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 2: Define the structure of the Bayesian Network (DAG)
# Example: A simple network with three nodes - "Rain", "Sprinkler", and "Wet Grass"
model = BayesianNetwork([('Rain', 'Wet Grass'),
                         ('Sprinkler', 'Wet Grass')])

# Step 3: Define the Conditional Probability Distributions (CPDs)
# Rain CPD: P(Rain)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])

# Sprinkler CPD: P(Sprinkler)
cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2, values=[[0.6], [0.4]])

# Wet Grass CPD: P(Wet Grass | Rain, Sprinkler)
cpd_wet_grass = TabularCPD(variable='Wet Grass', variable_card=2,
                           values=[[0.99, 0.9, 0.8, 0.0],
                                   [0.01, 0.1, 0.2, 1.0]],
                           evidence=['Rain', 'Sprinkler'],
                           evidence_card=[2, 2])

# Step 4: Add CPDs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wet_grass)

# Step 5: Validate the model (check for correctness of the structure and CPDs)
assert model.check_model(), "The model is invalid"

# Step 6: Perform inference (e.g., what is the probability that the grass is wet given it's raining?)
inference = VariableElimination(model)

# Query: P(Wet Grass | Rain=1)
result = inference.query(variables=['Wet Grass'], evidence={'Rain': 1})
print(result)
