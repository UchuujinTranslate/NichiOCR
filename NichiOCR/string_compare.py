from difflib import SequenceMatcher

def compare(OCRoutput, entireScript):
    OCRspeaker = OCRoutput[0]
    OCRstring = ''
    #OCRstring = str(OCRoutput[1:])

    for i in OCRoutput[1:]:
        OCRstring = OCRstring + str(i)

    print("OCR Speaker: " + OCRspeaker)
    print("OCR String: " + OCRstring)
    print('')

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    highestRatio = {}
    highestRatio['ratio'] = float()

    for x, y in entireScript.items():
        #print(x, y) 
        for i in y:
            #print(i['text'])
            weblateString = i['text']
            weblateSpeaker = i['speaker']

            # string and speaker similarity
            similarityRatio = similar(weblateString, OCRstring) + similar(weblateSpeaker, OCRspeaker)
            if similarityRatio >= highestRatio["ratio"]:
                if similarityRatio > 0.0:
                    print("Found highest match:", similarityRatio, "in script", x)          
                    highestRatio['script'] = x
                    highestRatio['ratio'] = similarityRatio
                    highestRatio['id'] = i['id']

    return highestRatio

def compare_results(highestRatio, entireScript):
    print("")
    print("Highest match with a ratio of:", highestRatio["ratio"])
    print("Script found in:", highestRatio["script"])
    print("ID:", highestRatio['id'])
    print('')

    print("Weblate script contents:")
    print("Speaker:", entireScript[highestRatio["script"]][int(highestRatio['id']-1)]['speaker'])
    print("String:", entireScript[highestRatio["script"]][int(highestRatio['id']-1)]['text'])

    #print("Current english translation:",)

    weblateLink = "https://weblate.lolc.at/translate/uchuujin/script-" + \
        highestRatio['script'] + "/en_US/?type=all&offset=" + str(highestRatio['id']+1)
        # look into offset values, might often be + 1

    print("Link on Weblate:", weblateLink)
    print('')

    # https://weblate.lolc.at/translate/uchuujin/script-0207/en_US/?type=all&offset=1