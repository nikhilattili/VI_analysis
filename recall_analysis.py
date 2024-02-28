import spacy
from collections import Counter
import csv

nlp = spacy.load("en_core_web_sm")

csv_files = ['rocky_barnes_amazon.csv', 'rocky_barnes_calvin.csv', 'lilmiquela_eyewear.csv', 'lilmiquela_bmw.csv']

brand_recalls = {
    'lilmiquela_bmw.csv': [
        'bmw', 'x2', 'car', 'vehicle', 'luxury', 'performance', 'design',
        'sporty', 'compact', 'suv', 'crossover', 'driving', 'innovation',
        'technology', 'style', 'elegance', 'comfort', 'features', 'handling',
        'prestige', 'buy', 'purchase', 'own', 'get', 'acquire', 'test drive',
        'interested', 'shopping', 'deal', 'offer', 'price', 'payment', 'finance'
    ],
    'rocky_barnes_calvin.csv': [
        'calvin klein', 'ck', 'fashion', 'clothing', 'apparel', 'style', 'designer',
        'brand', 'underwear', 'perfume', 'fragrance', 'cologne', 'jeans', 'accessories',
        'calvinklein', 'calvin klein collection', 'calvin klein jeans', 'calvin klein underwear',
        'ck one', 'ck all', 'ck be', 'ck eternity', 'ck obsession', 'buy', 'purchase', 'own',
        'get', 'acquire', 'shop', 'shopping', 'deal', 'offer', 'price', 'payment', 'finance', 'jewelry', 'style', 'pants'
    ],
    'lilmiquela_eyewear.csv': [
        'alexander mcqueen', 'mcqueen', 'eyewear', 'sunglasses', 'glasses', 'eyeglasses',
        'bags', 'handbags', 'purses', 'fashion', 'luxury', 'designer', 'brand', 'accessories',
        'alexander mcqueen eyewear', 'alexander mcqueen bags', 'alexander mcqueen sunglasses',
        'alexander mcqueen handbags', 'buy', 'purchase', 'own', 'get', 'acquire', 'shop',
        'shopping', 'deal', 'offer', 'price', 'payment', 'finance', 'fashion', 'style', 'trend', 'bag', 'shopping', 'shop', 'outfit'
    ],
    'rocky_barnes_amazon.csv': [
        'amazon', 'online shopping', 'e-commerce', 'retail', 'marketplace', 'buy', 'purchase',
        'shop', 'shopping', 'deal', 'offer', 'discount', 'price', 'payment', 'add to cart',
        'add to basket', 'checkout', 'order', 'prime', 'amazon prime', 'free shipping',
        'next day delivery', 'two-day shipping', 'same-day delivery', 'subscribe and save',
        'amazon fresh', 'amazon basics', 'amazon essentials', 'amazon fashion', 'amazon devices',
        'alexa', 'kindle', 'fire tv', 'fire tablet', 'echo', 'ring', 'prime video', 'prime music',
        'amazon prime day', 'amazon smile', 'wishlist', 'review', 'feedback', 'customer service',
        'robe', 'bathrobe', 'dressing gown', 'blanket', 'throw', 'comforter', 'quilt', 'coverlet',
        'bedspread', 'duvet', 'snuggle', 'cozy', 'warm', 'soft', 'plush', 'fleece', 'sherpa', 'nap', 'storefront', 'robe'
    ]
}

for csv_file in csv_files:
    keyword_mentions = Counter()
    total_comments = 0
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            comment = row['Comment']
            doc = nlp(comment.lower()) 
            tokens = [token.text for token in doc if token.is_alpha]
            keyword_mentions.update([token for token in tokens if token in brand_recalls[csv_file]])
            total_comments += 1

    total_keyword_mentions = sum(keyword_mentions.values())
    print(f"CSV File: {csv_file}")
    print(f"Total Comments: {total_comments}")
    print(f"Total Keyword Mentions: {total_keyword_mentions}")
    print(f"Ratio of Keyword Mentions to Total Comments: {total_keyword_mentions / total_comments if total_comments > 0 else 0}\n")
