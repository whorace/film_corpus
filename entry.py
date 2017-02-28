class Entry:
    def __init__(self, title, director, starring, runningTime, country, language, time, location, categories, text):
        self.title = title
        self.director = director
        self.starring = starring
        self.runningTime = runningTime
        self.country = country
        self.language = language
        self.time = time
        self.location = location
        self.categories = categories
        self.text = text
    def getTitle(self):
        return self.title
    def getDirector(self):
        return self.director
    def getStarring(self):
        return self.starring
    def getRunningTime(self):
        return self.runningTime
    def getCountry(self):
        return self.country
    def getLanguage(self):
        return self.language
    def getTime(self):
        return self.time
    def getLocation(self):
        return self.location
    def getCategories(self):
        return self.categories
    def getText(self):
        return self.text
    