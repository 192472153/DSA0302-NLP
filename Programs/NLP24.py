def dialog_act(sentence):

    sentence = sentence.lower()

    if "hello" in sentence or "hi" in sentence:
        return "Greeting"

    elif "?" in sentence:
        return "Question"

    elif "thank" in sentence:
        return "Thanking"

    elif "bye" in sentence:
        return "Goodbye"

    else:
        return "Statement"


text = input("Enter a dialog: ")

print("Dialog Act:", dialog_act(text))
