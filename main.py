def maksymaLokalneIndeksy(blocks):

    maksymaLokalneBloki = []

    for i in range(0, len(blocks)):
        if i == 0:
            if blocks[i] > blocks[i+1]:
                maksymaLokalneBloki.append(i)
        if i < len(blocks) - 1 and i > 0:
            if blocks[i] > blocks[i-1] and blocks[i] > blocks[i+1]:
                maksymaLokalneBloki.append(i)
        if i == len(blocks) - 1:
            if blocks[i] > blocks[i-1]:
                maksymaLokalneBloki.append(i)

    return maksymaLokalneBloki

def maksymaLokalneWysokosci(blocks):
    maksymaLokalneBloki = []

    for i in range(0, len(blocks)):
        if i == 0:
            if blocks[i] > blocks[i + 1]:
                maksymaLokalneBloki.append(blocks[i])
        if i < len(blocks) - 1 and i > 0:
            if blocks[i] > blocks[i - 1] and blocks[i] > blocks[i + 1]:
                maksymaLokalneBloki.append(blocks[i])
        if i == len(blocks) - 1:
            if blocks[i] > blocks[i - 1]:
                maksymaLokalneBloki.append(blocks[i])

    return maksymaLokalneBloki

def highestBlock(blocks):

    maxBlock = 0

    for block in blocks:
        if block > maxBlock:
            maxBlock = block
    return maxBlock

def material(blocks):

    startingBlock = highestBlock(blocks)

    capacityOnTheLeft = 0
    capacityOnTheRight = 0

    #counting capacity on the right

    blocksOnTheLeft = blocks[0:blocks.index(startingBlock)]
    indeksyMaksym = maksymaLokalneIndeksy(blocksOnTheLeft)
    wysokosciMaksym = maksymaLokalneWysokosci(blocksOnTheLeft)
    currentMaxIndex = blocks.index(startingBlock)

    while len(blocksOnTheLeft) != 0 and len(wysokosciMaksym) != 0:
        nextMaxIndex = blocksOnTheLeft.index(highestBlock(wysokosciMaksym))
        for i in reversed(range(nextMaxIndex, currentMaxIndex)):
            capacityOnTheLeft += blocksOnTheLeft[nextMaxIndex] - blocksOnTheLeft[i]

        del wysokosciMaksym[wysokosciMaksym.index(blocksOnTheLeft[nextMaxIndex]):len(wysokosciMaksym)]
        del blocksOnTheLeft[currentMaxIndex:len(blocksOnTheLeft)]
        currentMaxIndex = nextMaxIndex


    blocksOnTheRight = blocks[blocks.index(startingBlock)+1:len(blocks)]
    indeksyMaksym = maksymaLokalneIndeksy(blocksOnTheRight)
    wysokosciMaksym = maksymaLokalneWysokosci(blocksOnTheRight)
    currentMaxIndex = blocks.index(startingBlock)

    while len(blocksOnTheRight) != 0 and len(wysokosciMaksym) != 0:
        nextMaxIndex = blocksOnTheRight.index(highestBlock(wysokosciMaksym))
        for i in range(0, nextMaxIndex):
            capacityOnTheRight += blocksOnTheRight[nextMaxIndex] - blocksOnTheRight[i]

        del wysokosciMaksym[0:wysokosciMaksym.index(blocksOnTheRight[nextMaxIndex])+1]
        del blocksOnTheRight[0:nextMaxIndex+1]
        currentMaxIndex = nextMaxIndex


    capacity = capacityOnTheLeft + capacityOnTheRight
    return capacity


test1 = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
test2 = [6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0]
print('First test case: material([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]) = 83')
print(f'Result = {material(test1)}')
print('Second test case: material([6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0]) = 50')
print(f'Result = {material(test2)}')



