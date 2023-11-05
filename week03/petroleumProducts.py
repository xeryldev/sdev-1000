# petroleumProducts (v1.0)
#
# A 42-gallon barrel of crude oil (input) can be refined into almot 45 gallons 
# of petroleum products (output). This is due to processing gain
# (also called volumetric gain). 
# For details see: https://www.eia.gov/energyexplained/oil-and-petroleum-products/

# Step 1: Calculate the ratio of input volume to output volume for each of the six 
# petroleum products shown on the above web page and store each value in a 
# variable. Use meaningful variable names. Do not round result or on output.
gasolineRatio = 20.0/42
print("gasoline ratio is:", gasolineRatio)
distillateRatio = 12.5/42
print("distillate ratio is:", distillateRatio)
jetfuelRatio = 3.5/42
print("jet fuel ratio is: ", jetfuelRatio)
otherproductsRatio = 6.3/42
print("ratio of other products is: ", otherproductsRatio)
hydrocarbongasRatio = 1.7/42
print("the hydrocarbon liquid gas ratio is: ", hydrocarbongasRatio)
residualfuelRatio = 0.6/42
print("the ratio of residual fuel is: ", residualfuelRatio)
print()

# Step 2: Check your work above by calculating the total output volume from
# one 42-gallon barrel of oil. Your answer should be 44.6
# Print your answer with a suitable label.
# Then, print a line showing the total yield (output volume to input volume) followed by a blank line
inputVolume = 42.0
# *** ToDo: extend this formula to compute the total volume of all products.
oneBarrelOutputVolume = (gasolineRatio * inputVolume) + (distillateRatio * inputVolume) + (jetfuelRatio * inputVolume) + (otherproductsRatio * inputVolume) + (hydrocarbongasRatio * inputVolume) +  (residualfuelRatio * inputVolume)
print("Total output volume for one 42-gallon barrel of input:", oneBarrelOutputVolume, "gallons")
# Calculate and show the overall yield ratio (output volume to input volume) followed by a blank line
yieldRatio = oneBarrelOutputVolume/inputVolume     # Don't round calculated value
# Do round output to look nice for the reader
print("Ratio of yield is: ", round(yieldRatio,2))
print()

# Step 3: Calculate the output volumes for each product given 100 gallons of input
# Print the output volumes, one per line, suitably labeled.
# Then, print two lines giving the total output volume and the ratio of yield, followed by a blank line
inputVolume = 100
print("Given", inputVolume, "gallons of input oil, the following gallons of petroleum product will be produced")
gasolineOut = gasolineRatio * inputVolume
print(round(gasolineOut,2),"gallons of gasoline")
distillateOut = distillateRatio * inputVolume
print(round(distillateOut,2),"gallons of distillate")
jetfuelOut = jetfuelRatio * inputVolume
print(round(jetfuelOut, 2),"gallons of jet fuel")
otherproductsOut = otherproductsRatio * inputVolume
print(round(otherproductsRatio * inputVolume),"gallons of other products")
hydrocarbongasOut = hydrocarbongasRatio * inputVolume
print(round(hydrocarbongasRatio * inputVolume, 2),"gallons of liquid hydrocarbon gas")
residualfuelOut = residualfuelRatio * inputVolume
print(round(residualfuelRatio * inputVolume, 2),"gallons of residual fuel")
totalVolume = gasolineOut + distillateOut + jetfuelOut + otherproductsOut + hydrocarbongasOut + residualfuelOut
print("Total output volume will be: ", round(totalVolume, 2))
print("Ratio of yield is: ", round(totalVolume/inputVolume, 2))
print()

# Step 4: Repeat Step 3 for 10,000,000 gallons of input oil
# *** ToDo: replace this line with needed code 

inputVolume = 10000000
print("Given", inputVolume, "gallons of input oil, the following gallons of petroleum product will be produced")
gasolineOut = gasolineRatio * inputVolume
print(round(gasolineOut,2),"gallons of gasoline")
distillateOut = distillateRatio * inputVolume
print(round(distillateOut,2),"gallons of distillate")
jetfuelOut = jetfuelRatio * inputVolume
print(round(jetfuelOut, 2),"gallons of jet fuel")
otherproductsOut = otherproductsRatio * inputVolume
print(round(otherproductsRatio * inputVolume),"gallons of other products")
hydrocarbongasOut = hydrocarbongasRatio * inputVolume
print(round(hydrocarbongasRatio * inputVolume, 2),"gallons of liquid hydrocarbon gas")
residualfuelOut = residualfuelRatio * inputVolume
print(round(residualfuelRatio * inputVolume, 2),"gallons of residual fuel")
totalVolume = gasolineOut + distillateOut + jetfuelOut + otherproductsOut + hydrocarbongasOut + residualfuelOut
print("Total output volume will be: ", round(totalVolume, 2))
print("Ratio of yield is: ", round(totalVolume/inputVolume, 2))
print()