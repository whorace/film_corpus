Building a Corpus(Python)
===================================================
    CS132a 2017Spring A2: Building a Corpus
    
    Author: Hao Wang <haowang@brandeis.edu>
    Date: 2/1/2017

    Description: The program extracts pages from Wikipedia, identify fielded data,  
                 clean unstructured data, and store the results in json format

---

###Dependencies:
####OS: OSX(macOS Sierra)
####Python:2.7.10
####Python Package: wikitools <https://github.com/alexz-enwp/wikitools>

---

###Build Instructions:
The first step is setting up the wikitools package for the python environment.
The second step is writing the python file to get the Wikipedia pages of the category “2016 films” and extract the following fields:
Title, Director, Starring, Running_time, Country, Language, Time, Location, Categories and Text.
The third step is to save it into the json format.

###Run Instructions:
You just need to run the control.py without any input. It will output a json file called “2016_movies.json”

---

###Modules:
There are three python files in my project. In “control.py”, this is the python file which we run the whole extraction system. I use the time package here to count the running time. In “entry.py”, it is an Entry class in the file which is useful to create the object which stores the extracted field from each page. In “extraction.py”, it has the Extraction class which includes two parts, loading the data, extracting the data, and sending the data to json file. At first, I use “loadData” function to import the wikitools package for getting the webpages. Second, I use “extractEachPage” function to deal with the extraction job for each page and create an object for saving the extracted data. In the function, there are many small functions to work with it to deal with some cleaning job for data like “splitLine”, “cleanText”, “stringInBrac”. Then we transfer the data (saving in an entry project) to the dictionary format which is friendly to json. We accumulate all pages’ dictionary into an upper dictionary.  Third, we export the upper dictionary into a json file.

---

###Testing:
Considering the time consuming of the whole system, we just extract one page for testing each time. After all sets, I run the programmer on campus. It takes less than 10 minutes to finish it. At home, it takes about 29 minutes to finish it.
