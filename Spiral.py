def main():
    spiralWidth = input("Enter spiral width: ")
    drawSpiral(spiralWidth)
    main()

def drawSpiral(spiralWidth):
    spiralWidth = int(spiralWidth)
    maxLen = int(spiralWidth)
    spiral = []
    for i in range(0, spiralWidth - 1):
        spiral.append([])

    for i in range(0, spiralWidth - 1):
        spiral[0][i] = "*"
    
    for i in range(0, spiralWidth - 1):
        for j in range (0, spiralWidth - 1):
            print(spiral[i][j])

if __name__ == "__main__":
	main()
	exit()
