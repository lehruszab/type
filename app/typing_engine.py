from time import sleep


TYPING_DELAY = 0.05
TYPING_SYMBOL = "▒"


def type_text(text: str, edit_message) -> None:
    typed_text = ""

    for char in text:
        typed_text += char

        edit_message(typed_text + TYPING_SYMBOL) 
        sleep(TYPING_DELAY)

    edit_message(typed_text)