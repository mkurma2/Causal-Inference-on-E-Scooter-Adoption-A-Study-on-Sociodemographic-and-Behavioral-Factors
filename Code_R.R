library(lavaan)
library(readxl)

# Load your data
Rdata_2020 <- read_excel("C:/Users/mjava/Box/Today/E-scooter/e-scooter_transit_myself/Code_data/Rdata_2020.xlsx")

# Define the model
model <- ' 
  # latent variable definitions
  Intent =~ Intent1 + Intent2
  Pease =~ PEase1 + PEase2 + PEase3
  PUse =~ PUse1   + PUse7 + PUse8
  Penjoy =~ PEnjoy1 + PEnjoy2 + PEnjoy3 + PEnjoy4

  # regressions
  Intent  ~ Pease + PUse +frqncy_access_2_5_min
  PUse ~ Pease +Female+Graduate_Degree+frqncy_access_2_5_min
  Pease ~ Penjoy

'

# Fit the model
fit <- sem(model, data = Rdata_2020)

# Get a detailed summary of model fit
summary(fit, fit.measures = TRUE, standardized = TRUE)
