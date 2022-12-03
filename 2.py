# opponent:
# A Rock
# B Paper
# C Scissors
#
# player:
# X Rock
# Y Paper
# Z Scissors

# Points
# Rock 1
# Paper 2
# Scissors 3

# Lose 0
# Draw 3
# Win 6

def points_for_player(opponentHand, playerHand):
    # XYZ to ABC for player
    playerHandNormalized = chr(ord(playerHand)+ord('A')-ord('X'))
    score = 0
    #draw
    if (opponentHand == playerHandNormalized):
        score += 3
    #win
    elif (opponentHand == 'A' and playerHandNormalized == 'B') or\
    (opponentHand == 'B' and playerHandNormalized == 'C') or\
    (opponentHand == 'C' and playerHandNormalized == 'A'):
        score += 6

    score += 1 if playerHandNormalized == 'A' else 0
    score += 2 if playerHandNormalized == 'B' else 0
    score += 3 if playerHandNormalized == 'C' else 0
    return score

#part two
def points_for_playerv2(opponentHand, winType):
    score = 0
    playerHand = ''

    #lose
    if winType == 'X':
        #score += 0
        if opponentHand == 'A':
            playerHand = 'C'
        elif opponentHand == 'B':
            playerHand = 'A'
        else:
            playerHand = 'B'
    #draw
    elif winType == 'Y':
        score += 3
        playerHand = opponentHand
    #win
    else:
        score += 6
        if opponentHand == 'A':
            playerHand = 'B'
        elif opponentHand == 'B':
            playerHand = 'C'
        else:
            playerHand = 'A'

    score += 1 if playerHand == 'A' else 0
    score += 2 if playerHand == 'B' else 0
    score += 3 if playerHand == 'C' else 0
    return score

total_score = 0
with open('input2.txt') as f:
    lines = f.readlines()
    for line in lines:
        opponentHand = line[0:1]
        playerHand = line[2:3]
        # total_score += points_for_player(opponentHand, playerHand)
        total_score += points_for_playerv2(opponentHand, playerHand)

print(total_score)
