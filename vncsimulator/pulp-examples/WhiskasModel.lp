\* The Whiskas Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.013 ChickenPercent + 0.008 BeefPercent
Subject To
FatRequirement: 0.08 ChickenPercent + 0.1 BeefPercent >= 6
FibreRequirement: 0.001 ChickenPercent + 0.005 BeefPercent <= 2
PercentagesSum: ChickenPercent + BeefPercent = 100
ProteinRequirement: 0.1 ChickenPercent + 0.2 BeefPercent >= 8
SaltRequirement: 0.002 ChickenPercent + 0.005 BeefPercent <= 0.4
Bounds
0 <= ChickenPercent
Generals
ChickenPercent
End
