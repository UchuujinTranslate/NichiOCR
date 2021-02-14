from difflib import SequenceMatcher

from rich.console import Console
from rich.table import Table

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
                    print("Found highest match:", similarityRatio, "in script", x)          
                    highestRatio['script'] = x
                    highestRatio['ratio'] = similarityRatio
                    highestRatio['id'] = i['id']

    results['similarity_ratio'] = similarityRatio
    results['ocr_speaker'] = OCRspeaker
    results['ocr_string'] = OCRstring

    return highestRatio, results

def compare_results(highestRatio, entireScript, results):
    #print(len(highestRatio))

    print("")
    results['ratio'] = highestRatio['ratio']
    print("Highest match with a ratio of:", results['ratio'])
    results['script'] = highestRatio['script']
    print("Script found in:", results['script'])
    results['id'] = highestRatio['id']
    print("JSON ID:", results['id'])
    print('')

    entireScriptContents = entireScript[highestRatio['script']][int(highestRatio['id'])]

    print("Weblate script contents:")
    results['weblate_speaker'] = entireScriptContents['speaker']
    print("Speaker:", results['weblate_speaker'])
    results['weblate_string'] = entireScriptContents['text']
    print("String:", results['weblate_string'])
    # Odd behavior with id numbers, sometimes does not show correct strings based on id

    #print("Current english translation:",)


    weblateURL = "https://weblate.lolc.at/translate/uchuujin/script-" + \
        highestRatio['script'] + "/en_US/?type=all&offset=" + str(highestRatio['id'])
        # look into offset values, might often be + 1
        # id 3 is skipped on weblate for 0207
    results['weblate_url'] = weblateURL

    print("URL on Weblate:", weblateURL)
    print('')

    # https://weblate.lolc.at/translate/uchuujin/script-0207/en_US/?type=all&offset=1

    return results

def results_table(results):

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Source", style="dim")
    table.add_column("Content")

    # Stats
    table.add_row(
        "Script",
        results['script'],
    )
    table.add_row(
        "JSON ID",
        str(results['id']),
    )
    table.add_row(
        "Similarity Ratio",
        str(results['similarity_ratio']),
    )
    table.add_row()
    

    # OCR 
    table.add_row(
        "OCR Speaker",
        results['ocr_speaker'],
    )
    table.add_row(
        "OCR String",
        results['ocr_string'],
    )
    table.add_row()
    

    # Weblate
    table.add_row(
        "Weblate Speaker",
        results['weblate_speaker']
    )
    table.add_row(
        "Weblate String",
        results['weblate_string']
    )
    table.add_row(
        "Weblate Translation",
        "To be added..."
    )
    table.add_row()
    table.add_row(
        "Weblate URL",
        results['weblate_url']
    )

    console.print(table)
    return table
