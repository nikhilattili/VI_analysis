import csv
import matplotlib.pyplot as plt
from textblob import TextBlob

# Function to classify comment polarity
def classify_comment(comment):
    analysis = TextBlob(comment)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# CSV file paths
csv_files = ['lilmiquela_bmw.csv', 'rocky_barnes_amazon.csv', 'rocky_barnes_calvin.csv', 'lilmiquela_eyewear.csv']  # List of CSV files containing comments

# Plot sentiment analysis for each CSV file
for csv_file in csv_files:
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}  # Initialize counts for each sentiment category
    
    # Count sentiment categories for current CSV file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        total_comments = sum(1 for row in reader)  # Count total number of comments
        file.seek(0)  # Reset file pointer
        
        for row in reader:
            comment = row['Comment']
            classification = classify_comment(comment)
            sentiment_counts[classification] += 1
    
    # Calculate percentages for each sentiment category
    percentages = [sentiment_counts[sentiment] / total_comments * 100 for sentiment in ['Positive', 'Negative', 'Neutral']]
    
    # Plot pie chart for sentiment percentages
    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['lightgreen', 'lightcoral', 'lightskyblue']
    
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'Sentiment Analysis of Comments - {csv_file}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()
