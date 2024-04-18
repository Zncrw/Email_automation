import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def main():
    # read .xlsx file to obtain data
    try:
        df = pandas.read_excel('people.xlsx')
    except FileNotFoundError:
        print('Not valid name of excel file')

    # obtain yesterdays date
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(format='%Y-%m-%d')
    # iterate for data
    for index, row in df.iterrows():
        # initialize class NewsFeed with arguments from people.xlsx
        feed = NewsFeed(theme=row['interest'], date=yesterday, language='en', how_many=5)
        # e-mail, that message come from
        email = yagmail.SMTP(user='pythoncourse04@gmail.com', password='qwrn mpqa atzn itdn')
        # send e-mail to contacts from xlsx
        email.send(to=row['email'],
                   subject=f'Your news from {row["interest"]}',
                   contents=f'Hi, {row["name"]} \n See what is new in {row["interest"]} \n {feed.get()}')


# making script to send the news every morning 9:00
while True:
    # check for current hour and minute, if its 9:00 then send the emails
    if datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 0:
        main()
    # sleep for 60sec to prevent sending again and again whole minute
    time.sleep(60)
