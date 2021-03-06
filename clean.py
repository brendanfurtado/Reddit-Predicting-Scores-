from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
pd.options.display.width = 0


###### Loading the data ######
with open("./data/data.json") as file:
    data = json.load(file)

dataframe = pd.DataFrame.from_dict(data, orient='columns')
data = dataframe.copy()

clean_text = []  # array to store text after it has been cleaned
tokenizer = WordPunctTokenizer()


###### Cleaning the data ######

# Setting up pattern matching text we want to get rid of
pattern1 = r'https?://[^ ]+'
www_pattern = r'www.[^ ]+'
contractions_dict = {"isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
                     "haven't": "have not", "hasn't": "has not", "hadn't": "had not", "won't": "will not",
                     "wouldn't": "would not", "don't": "do not", "doesn't": "does not", "didn't": "did not",
                     "can't": "can not", "couldn't": "could not", "shouldn't": "should not", "mightn't": "might not",
                     "mustn't": "must not"}  # Dictionary for contractions, to prevent accidental removal after an apostrophe

contract_pattern = re.compile(
    r'\b(' + '|'.join(contractions_dict.keys()) + r')\b')

# Function that will take in the text data and clean it


def text_cleaner(text_data):
    soup = BeautifulSoup(text_data, 'lxml')  # HTML encoding
    getSoup = soup.get_text()

    try:
        # UTF-BOM Removal, process any strings of this form as a ?
        bom_removed = getSoup.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        bom_removed = getSoup

        # Remove URL links, special characters and numbers. Lower case all words too

        stripped = re.sub(pattern1, '', bom_removed)
        stripped = re.sub(www_pattern, '', stripped)
        lower_case = stripped.lower()
        contractions_handled = contract_pattern.sub(
            lambda x: contractions_dict[x.group()], lower_case)

        letters_only = re.sub("[^a-zA-Z]", " ", contractions_handled)

        # Tokenize and join together
        words = [x for x in tokenizer.tokenize(letters_only) if len(x) > 1]
        return (" ".join(words)).strip()


def clean():
    for i in range(0, len(data)):
        if((i+1) % 1000 == 0):
            print("Comments %d of %d has been processed" % (i+1, len(data)))

        clean_text.append(text_cleaner(data['text'][i]))


clean()  # call clean on the dataset

data_clean = pd.DataFrame(clean_text, columns=['text'])

# combine data_clean & original dataset
data_clean['is_root'] = data.is_root
data_clean['controversiality'] = data.controversiality
data_clean['children'] = data.children
data_clean['popularity_score'] = data.popularity_score

# Encode is_root & children columns
data_clean['is_root'] = data_clean['is_root'].astype(int)
data_clean['children'] = data_clean['children'].astype(int)


# Export to JSON
data_clean.to_json('./data/clean_data.json', orient='records')
