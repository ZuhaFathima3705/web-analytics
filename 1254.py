import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
reviews = [
    "The hotel room was very clean and spacious. Staff were friendly.",
    "Clean rooms and very friendly staff. The location was perfect!",
    "The hotel was dirty and the staff was rude.",
    "Spacious room with excellent service and clean bathroom.",
    "Amazing hospitality and quick check-in process.",
    "The bed was uncomfortable and the AC was not working.",
    "Beautiful view from the balcony and great food.",
    "The reception staff was helpful and polite.",
    "Room service was slow but the food tasted good.",
    "Very noisy environment during the night.",
    "Affordable price with decent facilities.",
    "The swimming pool was clean and well maintained.",
    "WiFi connection was very poor in the room.",
    "Breakfast buffet had many delicious options.",
    "The bathroom was small but very clean.",
    "Parking facility was convenient and secure.",
    "The hotel lobby looked luxurious and modern.",
    "Housekeeping service was excellent and prompt.",
    "The room had a bad smell and dirty sheets.",
    "Comfortable stay with friendly customer service.",
    "Air conditioning worked perfectly and the room was cool.",
    "The hotel location is near the railway station.",
    "Staff behavior was very professional and respectful.",
    "The elevator was slow and sometimes not working.",
    "The restaurant inside the hotel served tasty meals.",
    "Check-in process was very slow and frustrating.",
    "The mattress was soft and very comfortable.",
    "Hot water was not available in the morning.",
    "The hotel was worth the money spent.",
    "Excellent ambiance and peaceful surroundings."
]
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens
processed_reviews = [preprocess(review) for review in reviews]
print("Processed Reviews:")
for review in processed_reviews:
    print(review)
def jaccard_similarity(doc1, doc2):
    set1 = set(doc1)
    set2 = set(doc2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
print("\nJaccard Similarity Between All Reviews:\n")
n = len(processed_reviews)
for i in range(n):
    for j in range(i+1, n):
        similarity = jaccard_similarity(processed_reviews[i], processed_reviews[j])
        print(f"Similarity between Review {i+1} and Review {j+1}: {similarity:.2f}")
