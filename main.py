import func


if __name__=="__main__":
    while True:
        text = func.micro("ru")
        t_text = func.translate(text,"en")
        func.text_voice(t_text)