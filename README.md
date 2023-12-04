# Causal-Inference-on-E-Scooter-Adoption-A-Study-on-Sociodemographic-and-Behavioral-Factors
README for R Code (Structural Equation Modeling)
Title: E-Scooter Usage Analysis using SEM
Description:
This R script performs Structural Equation Modeling (SEM) to analyze factors influencing the adoption and sustained use of electric scooters (e-scooters). The script uses the lavaan package for SEM and the readxl package for reading Excel data.

How to Run:
Install Required Packages: Ensure lavaan and readxl are installed.
Load the Script: Open the script in RStudio or your preferred R environment.
Set the File Path: Modify the file path in the script to point to your dataset.
Run the Script: Execute the script to perform the SEM analysis.
Key Components:
Data Loading: Reads the e-scooter usage data from an Excel file.
Model Definition: Defines the SEM model with latent variables (Intent, Pease, PUse, Penjoy) and their relationships.
Model Fitting: Applies the SEM model to the dataset.
Output: Generates a summary of the model fit, including path coefficients and fit indices.


README for Python Code (Causal Analysis)
Title: Causal Analysis of E-Scooter Usage Factors
Overview
This Python script conducts a causal analysis to understand the effects of various factors on e-scooter usage. It uses factor analysis to create latent variables and then applies causal inference techniques to determine the effects of variables like Pease, PUse, and Penjoy on e-scooter usage intentions.
Dependencies
Python environment (preferably Anaconda)
Pandas for data manipulation
FactorAnalyzer for factor analysis
Seaborn and Matplotlib for data visualization
dowhy library for causal inference
Data
The data file Data_final.xlsx should include both the observed indicators for factor analysis and the variables needed for causal inference.
Instructions
Import necessary libraries.
Load the data using Pandas.
Perform factor analysis to create latent variables and append them to the DataFrame.
Generate a correlation heatmap for an overview of variable relationships.
Define the causal relationships based on the SEM model.
For each defined relationship, construct a causal model using CausalModel from the dowhy library, identify the estimand, and estimate the causal effect.
Perform refutation tests (Random Common Cause, Placebo Treatment, Data Subset) for each causal relationship and record the outputs.
