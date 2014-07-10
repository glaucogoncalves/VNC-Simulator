\* The Whiskas Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.013 Ingr_CHICKEN + 0.008 Ingr_BEEF
 + 0.01 Ingr_MUTTON + 0.002 Ingr_RICE + 0.005 Ingr_WHEAT + 0.001 Ingr_GEL
Subject To
FatRequirement: 0.08 Ingr_CHICKEN + 0.1 Ingr_BEEF + 0.11 Ingr_MUTTON
 + 0.01 Ingr_RICE + 0.01 Ingr_WHEAT >= 6
FibreRequirement: 0.001 Ingr_CHICKEN + 0.005 Ingr_BEEF + 0.003 Ingr_MUTTON
 + 0.1 Ingr_RICE + 0.15 Ingr_WHEAT <= 2
PercentagesSum: Ingr_CHICKEN + Ingr_BEEF + Ingr_MUTTON + Ingr_RICE
 + Ingr_WHEAT + Ingr_GEL = 100
ProteinRequirement: 0.1 Ingr_CHICKEN + 0.2 Ingr_BEEF + 0.15 Ingr_MUTTON
 + 0.04 Ingr_WHEAT >= 8
SaltRequirement: 0.002 Ingr_CHICKEN + 0.005 Ingr_BEEF + 0.007 Ingr_MUTTON
 + 0.002 Ingr_RICE + 0.008 Ingr_WHEAT <= 0.4
Bounds
0 <= Ingr_BEEF
0 <= Ingr_CHICKEN
0 <= Ingr_MUTTON
0 <= Ingr_RICE
0 <= Ingr_WHEAT
0 <= Ingr_GEL
End
