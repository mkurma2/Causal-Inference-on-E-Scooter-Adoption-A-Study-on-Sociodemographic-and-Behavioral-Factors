# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:55:26 2023
@author: mjava
"""

import pandas as pd
from factor_analyzer import FactorAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt
from dowhy import CausalModel
import warnings


# Suppress specific FutureWarnings from pandas
warnings.filterwarnings('ignore', category=FutureWarning, module='pandas.*')
warnings.filterwarnings('ignore')

# Your existing code
# ...



# Load your data
file_path = 'C:/Users/mjava/Box/Today/CS/Casual_Inference/Project/Data_final.xlsx'
data = pd.read_excel(file_path)

# Factor Analysis to Create Latent Variables
fa = FactorAnalyzer(n_factors=1, rotation=None)
latent_vars = {
    "Intent": ['Intent1', 'Intent2'],
    "Pease": ['PEase1', 'PEase2', 'PEase3'],
    "PUse": ['PUse1', 'PUse7', 'PUse8'],
    "Penjoy": ['PEnjoy1', 'PEnjoy2', 'PEnjoy3', 'PEnjoy4'],
}

# Create latent variables and append them to the original DataFrame
for latent_var, observed_vars in latent_vars.items():
    fa.fit(data[observed_vars])
    data[latent_var] = fa.transform(data[observed_vars])

# Now, create a heatmap including both latent variables and other variables
plt.figure(figsize=(15, 12))
sns.heatmap(data.corr(), annot=True, fmt=".2f")
plt.title('Correlation Matrix of All Variables')
plt.show()




# Define Relationships for Causal Analysis (based on SEM model)
relationships = [
    {"treatment": "Pease", "outcome": "Intent", "common_causes": ['PUse', 'frqncy_access_2_5_min']},
    {"treatment": "PUse", "outcome": "Intent", "common_causes": ['Pease', 'frqncy_access_2_5_min']},
    {"treatment": "Penjoy", "outcome": "Pease", "common_causes": []},
    {"treatment": "Pease", "outcome": "PUse", "common_causes": ['Female', 'Graduate_Degree', 'frqncy_access_2_5_min']},
    {"treatment": "Female", "outcome": "PUse", "common_causes": ['Pease', 'Graduate_Degree', 'frqncy_access_2_5_min']},
    {"treatment": "Graduate_Degree", "outcome": "PUse", "common_causes": ['Pease', 'Female', 'frqncy_access_2_5_min']},
    {"treatment": "frqncy_access_2_5_min", "outcome": "Intent", "common_causes": ['Pease', 'PUse']},
    # Add more relationships as needed based on your SEM model
]


# Perform Causal Analysis for Each Relationship
for relationship in relationships:
    model = CausalModel(
        data=data,
        treatment=relationship['treatment'],
        outcome=relationship['outcome'],
        common_causes=relationship['common_causes'],
        instruments=[],      # Specify instruments if any
        effect_modifiers=[]  # Specify effect modifiers if any
    )
    identified_estimand = model.identify_effect()
    causal_estimate = model.estimate_effect(identified_estimand,
                                            method_name="backdoor.linear_regression")
    print(f"Causal Estimate for {relationship['treatment']} -> {relationship['outcome']}:")
    print(causal_estimate)

    # Refutation tests
    # Random common cause
    refutation_random = model.refute_estimate(identified_estimand, causal_estimate, method_name="random_common_cause")
    print("Refutation by Random Common Cause:")
    print(refutation_random)

    # Placebo treatment
    refutation_placebo = model.refute_estimate(identified_estimand, causal_estimate, method_name="placebo_treatment_refuter", placebo_type="permute")
    print("Refutation by Placebo Treatment:")
    print(refutation_placebo)

    # Data subset
    refutation_data_subset = model.refute_estimate(identified_estimand, causal_estimate, method_name="data_subset_refuter", subset_fraction=0.9)
    print("Refutation by Data Subset:")
    print(refutation_data_subset)