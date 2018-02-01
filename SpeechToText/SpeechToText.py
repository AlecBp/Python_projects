#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alec
#
# Created:     07/04/2015
# Copyright:   (c) Alec 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import speech_recognition as sr
r = sr.Recognizer("en-US")
replaceList = ["u'", "[", "]", "'"]
import wikipedia
pageContent = ""
#pageTitle = ""

def audioStuff():
    print "Started recog process"
    with sr.WavFile("teste4.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        list = r.recognize(audio,True)                  # generate a list of possible transcriptions
        #print("Possible transcriptions:")
        result = []
        for prediction in list:
            #print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
            result.append(prediction["text"])
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")

    result = str(result)
    for word in replaceList:
        result = result.replace(word, "")
    result = result.split(",")
    return result[0]

def getPage():
    pageContentArray = []

    page = wikipedia.page(audioStuff())

    pageTitle = page.title
    pageContentArray.append(pageTitle)

    pageContent = page.content
    pageContentArray.append(pageContent)

    pageContentSplited = pageContent.split("== Forms ==")
    pageContentFirstParagraph = pageContentSplited[0]
    pageContentArray.append(pageContentFirstParagraph)

    return pageContentArray

dataOutput = getPage()
print dataOutput[1]
