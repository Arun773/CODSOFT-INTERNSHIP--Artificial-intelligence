import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Fight Club'],
    'description': [
        'A computer hacker learns from mysterious rebels about the true nature of his reality.',
        'A thief who steals corporate secrets through the use of dream-sharing technology.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'Batman faces a psychopathic criminal mastermind known as the Joker.',
        'An insomniac office worker and a devil-may-care soap maker form an underground fight club.'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Vectorize descriptions
tiff = TfidfVectorizer(stop_words='english')
tfidf_matrix = tiff.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df.index[df['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 recommendations (excluding the input movie)
    
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Test the recommendation system
print(get_recommendations('Inception'))