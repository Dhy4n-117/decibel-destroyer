from recommender import summon_sacred_texts, get_recommendations

sacred_texts = summon_sacred_texts('sample_bands.csv')

print("Testing exact match for 'Meshuggah'...\n")
pit_neighbors = get_recommendations('Meshuggah', sacred_texts)
print(pit_neighbors)

print("\n\nTesting slight typo for 'Goojira'...\n")
pit_neighbors_typo = get_recommendations('Goojira', sacred_texts)
print(pit_neighbors_typo)
