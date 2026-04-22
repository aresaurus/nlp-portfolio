import unicodedata

def normalization(text):
    text = text.replace("ñ", "NN")
    result = "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    ).lower()
    return result.replace("nn", "ñ")