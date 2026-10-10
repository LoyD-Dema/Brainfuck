cells = {
    0 : 0
}

i = 0
numOfCells = 3000

while i < numOfCells : 
    cells[i] = 0
    i += 1

i = 0

text = input("""Welcome to Brainfuck

Rules:
+ [Increment] Add 1 to the current cell. If the cell is at 255, it wraps back to 0.
- [Decrement] Subtract 1 from the current cell. If the cell is at 0, it wraps to 255.
> [Move Right] Move the pointer one cell to the right.
< [Move Left] Move the pointer one cell to the left.
. [Output] Print the current cell's value as an ASCII character.
, [Input] Read one byte of input and store its value in the current cell.
[ [Loop Start] If the current cell is 0, skip ahead to the instruction after the matching ]. Otherwise, continue into the loop.
] [Loop End] If the current cell is not 0, jump back to the matching [. Otherwise, continue past the loop.

Write your text here:
""") 

textToPrint = ""
iText = 0
isValid = True

loopsQueue = []
skip = False

while iText < len(text) :
    c = text[iText]

    if(skip):
          if c == ']' :
                skip = False
          continue


    match c:
        case '+':
                cells[i] += 1
                if cells[i]>255:
                     cells[i] = 0


        case '-':
                cells[i] -= 1
                if cells[i]<0:
                    cells[i] = 255

        case '>':
                i += 1
                if(i > numOfCells):   
                   i = numOfCells

        case '<':
                i -= 1
                if(i < 0):   
                    i = 0
        case '.':
                 textToPrint += chr(cells[i])
        case ',':
                charToIns = ''
                while True:
                    userInput = input("Enter a single character as input: ")
                    if len(userInput) == 1:
                        charToIns = userInput
                        cells[i] = ord(charToIns)
                        break
                    print("Please enter a single character to continue\n")

        case '[':
                if(cells[i] > 0):
                    if(iText not in loopsQueue):
                        loopsQueue.append(iText)
                else: 
                      skip = True
        case ']':
                if(cells[i] > 0):
                      iText = loopsQueue[-1]
                else :
                      loopsQueue.pop()
        case _:
                textToPrint = f"String not valid, found this char({c})"
                isValid = False
                break        
    iText += 1


if isValid :
    print(f"Result:\n{textToPrint}")
else :
    print(textToPrint)
    
