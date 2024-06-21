import spacy
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    time_start = datetime.now()
    print("Start", time_start)
    # Load the English model
    nlp = spacy.load("en_core_web_sm")

    # Read the CSV file
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\NoneCsv\EmptyBase_drug.csv')

    # Extract the 'sentence_without_drug' column
    sentences = read_csv_file['sentence_without_drug']

    # Process all sentences and collect proper nouns
    proper_nouns = {token.text for doc in nlp.pipe(sentences[:]) for token in doc if token.pos_ == "PROPN"}

    # Print the proper nouns
    print("Proper Nouns:", proper_nouns)
    time_end = datetime.now()
    print("End", time_end)
    time_diff = time_end - time_start
    print("time diff", time_diff)
