'''Assemble the algorithm to calculate how long it will take for me tofinish a
gallon of water in a day if i rehydrate every 15 min.'''
mouthCapacity = 70 #ml
swigs = mouthCapacity * 3 #ml per 3 full mouth capacity
day = 8 #8 hours of work
rehydrate = 15 #every 15 min
gallon = 3785 #ml in gallon
microBreak = 5 # 5 min
print("Theoretical Quuantity: ", round(3785/(4*210)*8))
mouths = gallon / mouthCapacity
hydroHour = 4 #hydrate 4 times per hour
swigsPerHour = hydroHour * mouthCapacity #how many gulps (ml) per hour
swigsPerDay = swigsPerHour * day #how many gulps (ml) per
#quantityOfSwigs = gallon/swigsPerDay #how many swigs needed to finish the gallon
print("Mouths to finish gallon = ",round(mouths), " mouths.")
print("Swigs Per Hour = ",swigsPerHour)
print("Swigs Per Day = ",swigsPerDay)
print("Quantity Of Swigs to finish gallon = ", round(gallon/((hydroHour * swigs)*day)), " hydrations.")






