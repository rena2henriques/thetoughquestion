# The answer to the tough question
import pandas
import os
import datetime as dt

# getting stock market info
import pandas_datareader.data as web

# for text to voice features
from gtts import gTTS

# getting current currency rates
from forex_python.converter import CurrencyRates
c = CurrencyRates()

# hardcoded for the win
entry_point = 7.31
holdings = 100

today = dt.date.today()
yesterday = today - dt.timedelta(days = 1)

df = web.DataReader('ACB.TO', 'yahoo', yesterday, today)

earnings = ((df.iloc[0]['Close'] - 7.31) * 100)*c.get_rate('CAD','USD')

print('You have earned {0:.2f} from your investments'.format(earnings))

# tells you how much you earned
if (earnings > 0):
    theanswer = "You have earned {:.2f} American Dollars from your investments. Have a nice day!".format(earnings)
else:
    theanswer = "You are losing {:.2f} American Dollars from your investments. Please reconsider your life choices!".format(earnings)

tts = gTTS(text=theanswer, lang='en')
tts.save("answer.mp3")
os.system("mpg123 answer.mp3")
