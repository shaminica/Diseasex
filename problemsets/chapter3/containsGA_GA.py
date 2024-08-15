def containsGA_GA(inString):
    if 'GAG' in inString:
        idx = inString.find('GAG')
        if inString[idx+3] == 'A':
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'
