import requests

class YoutubeSearch(object):

	def __init__(self, term):
		self.query_url = 'https://gdata.youtube.com/feeds/api/videos'
		self.query_params = {
			'q': term,
			'alt': 'json',
			'orderby': 'relevance',
			'v': '2'
		}

	def _do_request(self):
		return requests.get(self.query_url, params=self.query_params).json

	def __iter__(self):
		for video in self._do_request().get('feed').get('entry'):
			result = {}
			result['title'] = video.get('title').get('$t')
			result['url'] = video.get('link')[0].get('href')
			yield result


if __name__=='__main__':
	yt = YoutubeSearch('seo taiji')
	for x in yt:
		print yt

