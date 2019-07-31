class BasePage(object):
	def __init__(self, browser, url): #self - Это аналог this в С++/Java.
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)