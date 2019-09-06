print("X for plsyer 1")
print("0 for player 2")


def calcWin(i):
    if (i == 1) or (i == 3) or (i == 5) or (i == 7):
        return checkHorizontalAndVerticalWin(i)
    else:
        return checkHorizontalVerticalAndDiagonalWin(i)


def checkHorizontalAndVerticalWin(i):
    # Vertical win check
    if (list[i] == list[(i + 3) % 9]) and (list[(i + 3) % 9] == list[(i + 6) % 9]):
        return True
    # Horizontal win check for first row
    if ((i / 3) < 1):
        if (list[0] == list[1]) and (list[1] == list[2]):
            return True
    # Horizontal win check for second row
    elif (i / 3) >= 1 and (i / 3) < 2:
        if (list[3] == list[4]) and (list[4] == list[5]):
            return True
    # Horizontal win check for third  row
    else:
        if (list[6] == list[7]) and (list[7]) == list[8]:
            return True
    return False


def checkHorizontalVerticalAndDiagonalWin(i):
    if (checkHorizontalAndVerticalWin(i)):
        return True
    if (i == 0) or (i == 4) or (i == 8):
        if list[0] == list[4] and list[4] == list[8]:
            return True
    if (i == 4) or (i == 2) or (i == 6):
        if list[2] == list[4] and list[4] == list[6]:
            return True
    return False


list = ["p"] * 9
pos = 0
for pos in range(8):
    if pos % 2 == 0:
        entered_position = int(input("Enter for player 1  ")) - 1
        list[entered_position] = "X"
    else:
        entered_position = int(input("Enter for player 2  ")) - 1
        list[entered_position] = "0"
    for i in range(0, 9, 3):
        print(list[i] + " " + list[i + 1] + " " + list[i + 2])
        # if(i%3==2):
        #     print("\n")
    if calcWin(entered_position):
        if pos % 2 == 0:
            print("Player 1 won")
        else:
            print("Player 2 won")
        break
    else:
        continue

