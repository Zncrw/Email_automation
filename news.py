# API key: ca47475b409c4a9cb05f45a5a8cf6bae
import requests


class NewsFeed:
    """ gets news data via restful API"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "ca47475b409c4a9cb05f45a5a8cf6bae"

    def __init__(self, theme, date, language='en', how_many=5):
        # set how many articles user wants
        self.how_many = how_many
        # set language preferences
        self.language = language
        # set the date
        self.date = date
        # set the theme of interest
        self.theme = theme

    def get(self, api_key=api_key):
        # obtain link based on user given arguments
        link = self._get_link()

        response = requests.get(link)
        # get content as dictionary
        content = response.json()
        # final string for email body
        make_str = ''
        # try block to prevent IndexError
        try:
            # loop for 'how_many' messages
            for i in range(int(self.how_many)):
                # add results to variable
                make_str += (content['articles'][i]['title']) + "\n"
                make_str += (content['articles'][i]['url'])
                make_str += "\n\n"
        except IndexError:
            print('There is not this many articles, try less or another theme!')
        return make_str

    def _get_link(self):
        link = (f'{self.base_url}q={self.theme}&from={self.date}'
                f'&language={self.language}&apiKey={self.api_key}')
        return link


if __name__ == "__main__":
    feed = NewsFeed(theme='python', date='2024-04-17', language='en', how_many=5)
    print(feed.get())
