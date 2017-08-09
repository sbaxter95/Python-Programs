import urllib

def readText():
    quotes = open("C:\Users\sbaxt\Documents\Python\movie_quotes.txt")
    contentsOfFile = quotes.read()
    print (contentsOfFile)
    checkProfanity(contentsOfFile)

def checkProfanity(textToCheck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + textToCheck)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no swear words")
    else:
        print("Could not scan the document")
    
readText()
