import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def summon_sacred_texts(file_path):
    return pd.read_csv(file_path)

def get_recommendations(band_name, grimoire):
    grimoire['sonic_invocation'] = grimoire['genre'].fillna('') + ' ' + grimoire['lyrical_themes'].fillna('')
    
    riff_vectorizer = TfidfVectorizer(stop_words='english')
    heavy_matrix = riff_vectorizer.fit_transform(grimoire['sonic_invocation'])
    
    blood_pact_matrix = cosine_similarity(heavy_matrix, heavy_matrix)
    
    summoned_entities = grimoire['band_name'].str.lower().tolist()
    target_entity = band_name.lower()
    
    if target_entity not in summoned_entities:
        echoes_in_the_abyss = difflib.get_close_matches(target_entity, summoned_entities, n=1, cutoff=0.5)
        if echoes_in_the_abyss:
            target_entity = echoes_in_the_abyss[0]
            print(f"Entity not found. Summoning nearest match from the abyss: {target_entity.title()}")
        else:
            raise ValueError("Band not found in the sacred texts, nor were any echoes detected in the abyss.")

    entity_index = summoned_entities.index(target_entity)
    
    trve_kvlt_scores = list(enumerate(blood_pact_matrix[entity_index]))
    sorted_rituals = sorted(trve_kvlt_scores, key=lambda discordance: discordance[1], reverse=True)
    
    mosh_pit_indices = [ritual[0] for ritual in sorted_rituals[1:6]]
    
    pit_neighbors = grimoire.iloc[mosh_pit_indices].copy()
    pit_neighbors['trve_similarity'] = [ritual[1] for ritual in sorted_rituals[1:6]]
    
    return pit_neighbors[['band_name', 'genre', 'lyrical_themes', 'trve_similarity']]
