from difflib import SequenceMatcher

from rich.console import Console
import polib

console = Console()


def compare(OCRspeaker, OCRstring, entireScript):

    results = {}

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
                    console.log("Found highest match:", similarityRatio, "in script", x)          
                    highestRatio['script'] = x
                    highestRatio['ratio'] = similarityRatio
                    highestRatio['id'] = i['id']

    results['similarity_ratio'] = similarityRatio
    results['ocr_speaker'] = OCRspeaker
    results['ocr_string'] = OCRstring

    return highestRatio, results

def compare_results(highestRatio, entireScript, results):
    #print(len(highestRatio))

    console.log("")
    results['ratio'] = highestRatio['ratio']
    console.log("Highest match with a ratio of:", results['ratio'])
    results['script'] = highestRatio['script']
    console.log("Script found in:", results['script'])
    results['id'] = highestRatio['id']
    console.log("JSON ID:", results['id'])
    console.log('')

    entireScriptContents = entireScript[highestRatio['script']][int(highestRatio['id'])]

    console.log("Weblate script contents:")
    results['weblate_speaker'] = entireScriptContents['speaker']
    console.log("Speaker:", results['weblate_speaker'])
    results['weblate_string'] = entireScriptContents['text']
    console.log("String:", results['weblate_string'])
    # Odd behavior with id numbers, sometimes does not show correct strings based on id

    #print("Current english translation:",)


    weblateURL = "https://weblate.lolc.at/translate/uchuujin/script-" + \
        highestRatio['script'] + "/en_US/?type=all&offset=" + str(highestRatio['id'])
        # look into offset values, might often be + 1
        # id 3 is skipped on weblate for 0207
    results['weblate_url'] = weblateURL

    console.log("URL on Weblate: " + weblateURL)
    console.log('')

    # https://weblate.lolc.at/translate/uchuujin/script-0207/en_US/?type=all&offset=1

    return results

