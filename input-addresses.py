from addresses import *

seed = 681154853
number_of_addresses = 5

# Set the seed
random.seed(seed)

# Create a list of random addresses
addresses = []
for i in range(number_of_addresses):
    addresses.append(generateAddress(148))

# Write the list to a file
with open("input-addresses.txt", "w") as f:
    for address in addresses:
        f.write(address + "\n")