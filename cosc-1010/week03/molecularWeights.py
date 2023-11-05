# molecularWeights.py 
# This program calculates the molecular weights for a small set of 
# hydrocarbons, carbohydrates, and related molecules
# NB: For all you chemists out there: Apparently these values should be referred 
# to as "molar masses" but we're simply following the Zelle textbook's terminology, 
# page 80, problem 3.

def main():
  # molecular weights of selected atoms in grams per mole
  HYDROGEN_WGT = 1.00794
  CARBON_WGT = 12.0107
  OXYGEN_WGT = 15.9994 
  CALCIUM_WGT = 40.078  # note only 3 digits of precision
  
  # water: H2O (two hydrogen, one oxygen)
  water = (2 * HYDROGEN_WGT) + OXYGEN_WGT
  print("The raw calculation for molecular weight of water is:", water)
  # round to four decimal digits
  water = round(water, 4)
  print("The precision-rounded molecular weight of water is:", water)
  print()
  
  
  # propane: C3H8
  propane = (3 * CARBON_WGT) + (8 * HYDROGEN_WGT)
  print("The raw calculation for molecular weight of propane is:", propane)
  propane = round(propane, 4)
  print("The precision-rounded molecular weight of propane is:", propane)
  print()
  
  # glucose: C6H12O6
  glucose = (6 * CARBON_WGT) + (12 * HYDROGEN_WGT) + (6 * OXYGEN_WGT)
  print("The raw calculation for molecular weight of glucose is:", glucose)
  glucose = round(glucose, 4)
  print("The precision-rounded molecular weight of glucose is:", glucose)
  print()
  
  # calcium hydroxide: Ca(OH)2 (one calcium atom, two oxygen-hydrogen molecules)
  ca_hydroxide = (OXYGEN_WGT + HYDROGEN_WGT) * 2 + CALCIUM_WGT
  print("The raw calculation for molecular weight of calcium hydroxide is:", ca_hydroxide)
  ca_hydroxide = round(ca_hydroxide, 3)
  print("The precision-rounded molecular weight of calcium hydroxide is:", ca_hydroxide)

main()