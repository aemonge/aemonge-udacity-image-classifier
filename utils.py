import re

def isntHiddenFile(path):
    return not re.search(r"(\.[^\.\/]+)", path)

def parse_pet_label(filename = ""):
    label = re.sub(r"(\d*)|(\.png)|(\.jpeg)|(\.jpg)", "", filename.lower().replace("_", " "))
    return label.strip()
