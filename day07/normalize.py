import unicodedata

def normalization(text):
    # Protect "ñ" before stripping accents — NFD would decompose it into n + combining tilde (Mn),
    # which would then be discarded, turning "ñ" into "n"
    text = text.replace("ñ", "NN")
    
    # NFD decomposes accented characters into base letter + combining mark (e.g. "ó" → "o" + "́")
    # The generator filters out combining marks (category "Mn"), leaving only base letters
    result = "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    ).lower()
    
    # Restore "ñ" from its placeholder
    return result.replace("nn", "ñ")