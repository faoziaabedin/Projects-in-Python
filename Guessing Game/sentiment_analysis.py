"""
Faozia Abedin
251358251
fabedin4
November 17th 2023
"""


# Function to read keywords and their sentiment values from a TSV file
def read_keywords(keyword_file_name):
    try:
        with open(keyword_file_name, 'r') as file:
            keyword_dict = {}
            for line in file:
                # Splitting each line into word and value
                word, value = line.strip().split('\t')
                # Storing the word and its sentiment value in a dictionary
                keyword_dict[word] = int(value)
            return keyword_dict
    except IOError:  # error if file cannot be opened
        print(f"Could not open file {keyword_file_name}!")
        return {}


# Function to clean tweet text, removing non-alphabetical characters and converting to lowercase
def clean_tweet_text(tweet_text):
    return ''.join([char.lower() for char in tweet_text if char.isalpha() or char.isspace()])


# Function to calculate the sentiment score of a tweet
def calc_sentiment(tweet_text, keyword_dict):
    score = 0
    words = tweet_text.split()
    for word in words:
        score += keyword_dict.get(word, 0)  # adding teh score fo each word in the dictionary
    return score


# Function to classify the sentiment score into positive, negative, or neutral categories
def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


# Function to read tweet data from a CSV file
def read_tweets(tweet_file_name):
    tweets_data = []
    try:
        with open(tweet_file_name, 'r') as tweet_file:
            for tweet_line in tweet_file:
                data = tweet_line.strip().split(',')
                # Creating a dictionary for each tweet
                tweet = {
                    'date': data[0],
                    'text': clean_tweet_text(data[1]),
                    'user': data[2],
                    'retweet': int(data[3]),
                    'favorite': int(data[4]),
                    'lang': data[5],
                    'country': data[6],
                    'state': data[7],
                    'city': data[8],
                    'lat': float(data[9]) if data[9] != 'NULL' else 'NULL',
                    'lon': float(data[10]) if data[10] != 'NULL' else 'NULL',

                }
                tweets_data.append(tweet)
    except FileNotFoundError:
        # Error handling if the tweet file is not found
        print(f"File {tweet_file_name} could not be found.")
    return tweets_data


# Function to generate a report based on the sentiment analysis of the tweets
def make_report(tweet_list, keyword_dict):
    # Initializing a dictionary to store the report data
    report = {
        'num_tweets': len(tweet_list),
        'num_positive': 0,
        'num_negative': 0,
        'num_neutral': 0,
        'num_favorite': 0,
        'avg_favorite': 0,
        'num_retweet': 0,
        'avg_retweet': 0,
        'avg_sentiment': 0,
        'top_five': ''
    }

    # Variables to calculate averages
    total_sentiment = 0
    total_favorite_sentiment = 0
    total_retweet_sentiment = 0

    # Country sentiment tracking
    country_sentiment = {}
    country_counts = {}

    # Calculating sentiment score for each tweet
    for tweet in tweet_list:
        sentiment_score = calc_sentiment(tweet['text'], keyword_dict)
        total_sentiment += sentiment_score

        # Classify and count sentiments
        classification = classify(sentiment_score)
        if classification == 'positive':
            report['num_positive'] += 1
        elif classification == 'negative':
            report['num_negative'] += 1
        else:
            report['num_neutral'] += 1

        # Track favorited tweets
        if tweet['favorite'] > 0:
            report['num_favorite'] += 1
            total_favorite_sentiment += sentiment_score

        # Track retweeted tweets
        if tweet['retweet'] > 0:
            report['num_retweet'] += 1
            total_retweet_sentiment += sentiment_score

        # Track sentiment by country
        country = tweet['country']
        if country != 'NULL':
            country_sentiment[country] = country_sentiment.get(country, 0) + sentiment_score
            country_counts[country] = country_counts.get(country, 0) + 1

    # Calculate averages
    if report['num_tweets'] > 0:
        report['avg_sentiment'] = round(total_sentiment / report['num_tweets'], 2)
    if report['num_favorite'] > 0:
        report['avg_favorite'] = round(total_favorite_sentiment / report['num_favorite'], 2)
    if report['num_retweet'] > 0:
        report['avg_retweet'] = round(total_retweet_sentiment / report['num_retweet'], 2)

    # Determine top 5 countries
    country_avg_sentiment = {country: country_sentiment[country] / country_counts[country]
                             for country in country_sentiment}
    top_countries = sorted(country_avg_sentiment, key=country_avg_sentiment.get, reverse=True)[:5]
    report['top_five'] = ', '.join(top_countries)

    return report


# Function to write the sentiment analysis report to a file
def write_report(report, output_file):
   try:
        with open(output_file, 'w') as file:
            file.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
            file.write(f"Total number of tweets: {report['num_tweets']}\n")
            file.write(f"Number of positive tweets: {report['num_positive']}\n")
            file.write(f"Number of negative tweets: {report['num_negative']}\n")
            file.write(f"Number of neutral tweets: {report['num_neutral']}\n")
            file.write(f"Number of favorited tweets: {report['num_favorite']}\n")
            file.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
            file.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
            file.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
            file.write(f"Top five countries by average sentiment: {report['top_five']}\n")
            print(f"Wrote report to {output_file}")
   except IOError:
        print(f"Could not open file {output_file}!")