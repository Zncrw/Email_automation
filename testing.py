import requests
response = requests.get('https://newsapi.org/v2/everything?q=python&from=2024-03-18&language=en&apiKey=ca47475b409c4a9cb05f45a5a8cf6bae')
content = response.json()
# final string for email body
make_str = ''
# loop for 'how_many' messages
for i in range(10):
    # add results to variable
    make_str += (content['articles'][i]['title']) + "\n"
    make_str += (content['articles'][i]['url'])
    make_str += "\n\n"
print(make_str)
