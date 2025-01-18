"""
Faozia Abedin
251358251
fabedin4
November 17th 2023
"""

# Importing necessary functions from the sentiment_analysis module
from sentiment_analysis import read_keywords, read_tweets, make_report, write_report


def main():
    try:
        # Get file names from user
        keyword_file = input("Input keyword filename (.tsv file): ")
        tweet_file = input("Input tweet filename (.csv file): ")
        output_file = input("Input filename to output report in (.txt file): ")

        # Validate file extensions
        if not keyword_file.endswith('.tsv'):
            raise Exception("Must have tsv file extension!")
        if not tweet_file.endswith('.csv'):
            raise Exception("Must have csv file extension!")
        if not output_file.endswith('.txt'):
            raise Exception("Must have txt file extension!")

        # Read in keywords and tweets
        keyword_dict = read_keywords(keyword_file)
        tweets = read_tweets(tweet_file)

        if not keyword_dict:
            raise Exception("Keyword dictionary is empty!")
        if not tweets:
            raise Exception("Tweet list is empty!")

        # Perform analysis and create report
        report = make_report(tweets, keyword_dict)

        # Write report to file
        write_report(report, output_file)
    except FileNotFoundError as e:
        raise Exception(f"Error: {e.filename} not found.")

    except Exception as e:
        raise Exception(f"Error: {e}")

main()
