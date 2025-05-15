import pandas as pd
import requests

df = pd.read_csv("folder_contents_my_audio.csv")


def get_isbn(title, author):
    try:
        response = requests.get(
            f"https://openlibrary.org/search.json?title={title}&author={author}")
        return response.json()['docs'][0]['isbn'][0]
    except:
        return None


df['ISBN'] = df.apply(lambda row: get_isbn(
    row['Title'], row['Author']), axis=1)
df.to_csv("books_with_isbn.csv", index=False)
