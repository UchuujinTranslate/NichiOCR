import polib
import json
from rich.console import Console

console = Console()


def english_search(script, id):
    jsonFile = json.load(
        open("scripts/" + script + ".json", 'r', encoding='utf-8'))
    po = polib.pofile("scripts/en_US/" + script + ".po")

    # modified from sc_patch_translations.py on the main project
    for i in range(0, len(jsonFile)):
        dialog = jsonFile[i]

        dialog["speaker"] = dialog["speaker"].replace('\\n', '\n')
        dialog["text"] = dialog["text"].replace('\\n', '\n')

        speakerTranslation = ""
        textTranslation = ""

        for entry in po:
            if len(entry.msgstr) > 0:

                if entry.msgid == dialog["speaker"]:
                    speakerTranslation = entry.msgstr

                    console.log("Speaker Match: \n%s\n->\n%s" %
                                (entry.msgid.rstrip(),
                                    speakerTranslation.rstrip()))
                    console.log("JSON ID:", dialog['id'])

                if entry.msgid == dialog["text"]:
                    textTranslation = entry.msgstr
                    console.log("Text Match: \n%s\n->\n%s\n\n" %
                                (entry.msgid.rstrip(),
                                    textTranslation.rstrip()))
                    console.log("JSON ID:", dialog['id'])
                    console.log('')
                    console.log('')

                    if int(dialog['id']) == int(id):
                        console.log("Found the translated version!")
                        console.log(textTranslation)
                        return speakerTranslation, textTranslation


# english_po("0207", "0")
