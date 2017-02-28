# Hao Wang Assignment2 CS132a
from entry import Entry
class Extraction:
    

    
    
    def loadData(self):
        from wikitools import wiki
        from wikitools import category
        
        wikiobj = wiki.Wiki("https://en.wikipedia.org/w/api.php")
        wikicat = category.Category(wikiobj, title = "2016_films")
        self.wikipages = wikicat.getAllMembers()
        
    # Get each film object in the film category
    # For loop to get the object in list
    # for element in wikipages:
    #     print type(element)
    
    # test to get the first film
    def run(self):
        bigDic = {}
        i = 1
        for eachPage in self.wikipages:
            entry = self.extractEachPage(eachPage.getWikiText())
            dic = self.transferToDic(entry)
            bigDic[i] = dic
            i += 1
        self.sendToJsonFile(bigDic)
        ###################testing#####################   
#         eachPage = self.wikipages[344].getWikiText()
#         entry = self.extractEachPage(eachPage)
#         bigDic[344] = self.transferToDic(entry)
#         self.sendToJsonFile(bigDic)
        #############################################
        
    # get the all useful info in each film webpage    
    def extractEachPage(self,string):
        title = ""
        director = ""
        starring = ""
        runningTime = ""
        country = ""
        language = ""
        time = ""
        location = ""
        categories = ""
        text = ""
        
        arr = string.split("\n")

        for index in range(len(arr)):

            line = arr[index]
            
            if "| name" in line:
                title = self.splitLine(line, "| name")
                #print title
            if "| director" in line:
                director = self.splitLine(line, "| director")
                #print director
            if "| starring" in line:
                starring = self.splitLine(line, "| starring")
                #print starring
            if "| runtime" in line:
                runningTime = self.splitLine(line, "| runtime")
                #print runningTime
            if "| country" in line:
                country = self.splitLine(line, "| country")
                #print country
            if "| language" in line:
                language = self.splitLine(line, "| language")
                #print language
            
            # time
            
            # location
            
            
            
            # category   
            if "[[Category:" in line:
                categories += (line.strip("[[Category:").strip("]]") + "<br />")
                #print categories
                
            # text
            str = "'''''"
            if str in line:
        
                line = line.replace("'''''","")
                line = line.replace("[[", "")
                line = line.replace("]]", "")
                line = self.stringInBrac("<ref>", "</ref>", line)
                #print line
                text += line
                #print text
        
            if "==" in line and not("==References==" in line) and not("==External links==" in line):
                text += ("\n" + line)
                #checkArray = True
                try:#check whether index + 1 is out of size
                    while(arr[index + 1] != ""):
                        index += 1
                        afterClean = self.cleanText(arr[index])
                        if(not afterClean == ""):
                            text += ("\n" + afterClean)
                except IndexError:
                    pass                
            
            
            
        entry = Entry(title, director, starring, runningTime, country, language, time, location, categories, text)
        
        
        return entry
    # delete unnecessary things for data in infobox
    def splitLine(self, line, delete):
        afterSplit = (line.strip(delete)).strip("= ")
        return afterSplit
        
    # clean the unnecessary stuffs in String
    def cleanText(self, line):
        line = line.replace("'''''", "")
        line = line.replace("[[", "")
        line = line.replace("]]", "")
    
        line = line.replace("*", "")
        line = line.replace("{|", "")
        line = line.replace("|}","")
    
        line = line.replace("!", "")
        line = line.replace("|-", "") 
        line = line.replace("|", "")
    
        line = self.stringInBrac("<ref>", "</ref>", line)
        line = self.stringInBrac("{{", "}}", line)
    
        # line = line.replace("{{Won}}", "")
        # line = line.replace("{{won}}", "")
        # line = line.replace("{{nom}}", "")
        line = line.strip()
        return line
    
    # delete all data in some certain bracket with brackets
    def stringInBrac(self, leftBrac, rightBrac, line):
        lengthOfEndBrac = len(rightBrac)
        startbrac = line.find(leftBrac)
        endbrac = line.find(rightBrac)
        if startbrac != -1 and endbrac != -1:
            stringInBrac = line[startbrac:endbrac + lengthOfEndBrac]
            line = line.replace(stringInBrac, "")
    
        return line
    # transfer an object to a dictionary
    def transferToDic(self, entry):
        title = entry.getTitle()
        director = entry.getDirector()
        starring = entry.getStarring()     
        runningTime = entry.getRunningTime()
        country = entry.getCountry()
        language = entry.getLanguage()
        time = entry.getTime()
        location = entry.getLocation()
        categories = entry.getCategories()
        text = entry.getText()
        
        listOfStarring = self.split_line(starring)
        listOfTime = self.split_line(time)
        listOfLocation = self.split_line(location)
        listOfCategories = self.split_line(categories)
        
        
        
        dic = {}
        dic["language"] = language
        dic["title"] = title
        dic["country"] = country
        dic["time"] = listOfTime
        dic["director"] = director
        dic["location"] = listOfLocation
        dic["starring"] = listOfStarring
        dic["text"] = text
        dic["runtime"] = runningTime
        dic["categories"] = listOfCategories
        
        return dic
    # split the string into a list    
    def split_line(self, line):
        return line.split("<br />")

    def sendToJsonFile(self, dic):
        import json
        #print "done1"
        with open('2016_movies.json','w') as f:
            f.write(json.dumps(dic))
            print "done"
        
        

