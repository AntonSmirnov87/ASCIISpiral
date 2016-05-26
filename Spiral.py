def main():
    while True:
        spiralWidth = input("Enter spiral width: ")
        if(spiralWidth.isdigit() == True):
            drawSpiral(spiralWidth)
        elif(spiralWidth[0].lower() == "q"):
            exit()
        else:
            print("Please enter a positive integer")

def drawSpiral(spiralWidth):
    spiralWidth = int(spiralWidth)
    maxLen = int(spiralWidth)
    sideCount = 1
    xDir = 1
    xPos = 0
    yDir = 1
    yPos = 0

    # Initialize array
    spiral = []
    for i in range(0, spiralWidth):
        spiral.append([])
        for j in range(0, spiralWidth):
            spiral[i].append(" ")

    # Draw spiral
    for sideLen in range(spiralWidth, 0, -1):
        for pos in range(0, sideLen):
            spiral[yPos][xPos] = "*"
            if(sideCount % 2 == 1):
                xPos += xDir
            else:
                yPos += yDir
        if(sideCount % 2 == 1):
            xDir *= -1
            xPos += xDir
            yPos += yDir
        else:
            yDir *= -1
            yPos += yDir
            xPos += xDir
        sideCount += 1

    # Print spiral
    for i in range(0, spiralWidth):
        for j in range (0, spiralWidth):
            print(spiral[i][j], end="   ")
        print("\n")

if __name__ == "__main__":
	main()
	exit()
