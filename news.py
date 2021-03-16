import requests
import json

def speak(str):
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.SpVoice")
	speak.Speak(str)

if __name__ == '__main__':
	speak("welcome to the times of india")
	url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=7fd3d480c7a0419fa129feb32f92293c"
	news = requests.get(url).text
	news_dict = json.loads(news)
	art = news_dict['articles']
	for article in art:
		speak(article['title'])
		speak("Next news is..")
	speak("Thank you Have a nice day")