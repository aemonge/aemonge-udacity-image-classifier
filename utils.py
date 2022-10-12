import re

def parse_pet_label(filename = ""):
    label = re.sub(r"(\d*)|(\.png)|(\.jpeg)|(\.jpg)", "", filename.lower().replace("_", " "))
    return label.strip()
