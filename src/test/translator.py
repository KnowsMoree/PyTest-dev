from translate import Translator
import os

is_next = True
while is_next:
    os.system('clear')
    print(13 * "=" + " Text Translator " + 13 * "=")

    translate_from = input('Translate From? (nation code: id/en/es): ')
    translate_to = input('Translate To? (nation code: id/en/es): ')

    text = input(f"Text ({translate_from} -> {translate_to}): ")

    translator = Translator(to_lang=translate_to, from_lang=translate_from)
    translations = translator.translate(text)

    if len(translations) > 20:
        print(translations)
    else:
        print(f"{text} => {translations}")

    con = input(f"\nLanjut? (y/n): ")
    is_next = True if con == "y" else False
