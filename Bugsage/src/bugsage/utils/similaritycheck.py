from difflib import SequenceMatcher

def similaritycheck(text1,text2):
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity>=0.9