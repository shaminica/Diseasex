class Transition:
    def __init__(self, currentState, nextState, currentString, writeString, direction):
        self.currentState = currentState
        self.nextState = nextState
        self.currentString = currentString
        self.writeString = writeString
        self.direction = direction

def parseTransition(tmString):
        lines = tmString.split('\n')

        for line in lines:
            currentState = line.split(':')[0].split('->')[0]
            nextState = line.split(':')[0].split('->')[1]
            currentString = line.split(':')[1].split(';')[0]
            if ',' in line:
                writeString = line.split(';')[1].split(',')[0]
                direction = line.split(';')[1].split(',')[1]
            else:
                writeString = currentString
                direction = line.split(';')[1]
            
            transition = Transition(currentState, nextState, currentString, writeString, direction)
            #trantsions.append(transition)
        
        return transition

def simulateTM(tmString, inString):
    return parseTransition(tmString)