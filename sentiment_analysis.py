import csv
import matplotlib.pyplot as plt
from textblob import TextBlob

def classify_comment(comment):
    analysis = TextBlob(comment)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'


csv_files = ['lilmiquela_bmw.csv', 'rocky_barnes_amazon.csv', 'rocky_barnes_calvin.csv', 'lilmiquela_eyewear.csv']


for csv_file in csv_files:
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}  
    

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        total_comments = sum(1 for row in reader)
        file.seek(0)
        
        for row in reader:
            comment = row['Comment']
            classification = classify_comment(comment)
            sentiment_counts[classification] += 1

    percentages = [sentiment_counts[sentiment] / total_comments * 100 for sentiment in ['Positive', 'Negative', 'Neutral']]
    

    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['lightgreen', 'lightcoral', 'lightskyblue']
    
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'Sentiment Analysis of Comments - {csv_file}')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
