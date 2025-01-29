class Transition:
    def __init__(self, currentState, nextState, currentString, writeString, direction):
        self.currentState = currentState
        self.nextState = nextState
        self.currentString = currentString
        self.writeString = writeString
        self.direction = direction


class TuringMachine:
    def __init__(self, tmString, inString):
        self.tmString = tmString
        self.inString = inString

    def parseTransition(self):
        tmString = self.tmString
        lines = tmString.split('\n')

        for line in lines:
            currentState = lines.split(':')[0].split('->')[0]
            nextState = lines.split(':')[0].split('->')[1]
            currentString = lines.split(':')[1].split(';')[0]
            if ',' in line:
                writeString = lines.split(';')[1].split(',')[0]
                direction = lines.split(';')[1].split(',')[1]
            else:
                direction = lines.split(';')[1]
            
            transition = Transition(currentState, nextState, currentString, writeString, direction)
            #trantsions.append(transition)
        
        return transitions