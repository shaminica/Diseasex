import re

def TFmatch(match):
    if match is None:
        return "No"
    return "Yes"

def q9_14(inString, i):
    if i == 1:
        match = re.fullmatch(r"[a-zA-Z1-9]+", inString)
        return TFmatch(match)
    if i == 2:
        match = re.fullmatch(r"[CATG]+", inString)
        return TFmatch(match)
    if i == 3:
        match = re.match(r".*(GAGA).*(CTTCC).*", inString)
        return TFmatch(match)
    if i == 4:
        match = re.fullmatch(r"(AA(CG)?(T?))?|GGT", inString)
        return TFmatch(match)
    if i == 5:
        pattern = re.compile(r".*(\n|\s)*def [a-zA-Z1-9][a-zA-Z1-9_]+\(([a-zA-Z1-9][a-zA-Z1-9=\s,]+)*\):(.|\s|\n)*")
        match = re.match(pattern, inString)
        return TFmatch(match)


def isValidPassword(password):
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!-/:-@[-`{-~])[!-~]{8,100}$")
    match = re.match(pattern, password)
    if match is None:
        return "InVaild"
    else:
        return "Valid"
