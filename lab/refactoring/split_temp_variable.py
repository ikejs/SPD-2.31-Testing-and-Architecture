# by Kami Bigdely
# Split temporary variable

patty = 70 * 2 # [gr]
pickle = 20 * 4 # [gr]
tomatoes = 25 * 3 # [gr]
lettuce = 15 * 2 # [gr]
buns = 95 # [gr]
kimchi = 30 # [gr]
mayo = 5 # [gr]
golden_fried_onion = 20 # [gr]

sandwich_weight = (
  patty + 
  pickle + 
  tomatoes + 
  buns + 
  lettuce
)

print("NY Burger Weight", sandwich_weight)
sandwich_weight = (
  patty + 
  pickle + 
  tomatoes + 
  buns + 
  kimchi + 
  mayo + 
  golden_fried_onion
)
print("Seoul Kimchi Burger Weight", sandwich_weight)

