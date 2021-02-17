import polib
import json


# replace print statements with console.log
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

                    print("Speaker Match: \n%s\n->\n%s" %
                          (entry.msgid.rstrip(), speakerTranslation.rstrip()))
                    print("JSON ID:", dialog['id'])

                if entry.msgid == dialog["text"]:
                    textTranslation = entry.msgstr
                    print("Text Match: \n%s\n->\n%s\n\n" %
                          (entry.msgid.rstrip(), textTranslation.rstrip()))
                    print("JSON ID:", dialog['id'])
                    print('')
                    print('')

                    if int(dialog['id']) == int(id):
                        print("Found the translated version!")
                        print(textTranslation)
                        return speakerTranslation, textTranslation


# english_po("0207", "0")
