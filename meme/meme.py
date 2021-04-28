import requests

class Meme:
    def __init__(self):
        self.url = 'https://meme-api.herokuapp.com/gimme'
        meme = requests.get(url=self.url)
        meme = meme.json()
        self.postLink = meme['postLink']
        self.subreddit = meme['subreddit']
        self.title = meme['title']
        self.url = meme['url']
        self.nsfw = meme['nsfw']
        self.spoiler = meme['spoiler']
        self.author = meme['author']
        self.ups = meme['ups']
        self.total = meme
