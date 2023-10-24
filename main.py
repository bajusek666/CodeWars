def localMaximumBlocksIndexes(blocks):

    localMaxIndexes = []

    for i in range(0, len(blocks)):
        if i == 0:
            if blocks[i] > blocks[i+1]:
                localMaxIndexes.append(i)
        if i < len(blocks) - 1 and i > 0:
            if blocks[i] > blocks[i-1] and blocks[i] > blocks[i+1]:
                localMaxIndexes.append(i)
        if i == len(blocks) - 1:
            if blocks[i] > blocks[i-1]:
                localMaxIndexes.append(i)

    return localMaxIndexes

def localMaximaBlocksHeights(blocks):
    localMaxHeights = []

    for i in range(0, len(blocks)):
        if i == 0:
            if blocks[i] > blocks[i + 1]:
                localMaxHeights.append(blocks[i])
        if i < len(blocks) - 1 and i > 0:
            if blocks[i] > blocks[i - 1] and blocks[i] > blocks[i + 1]:
                localMaxHeights.append(blocks[i])
        if i == len(blocks) - 1:
            if blocks[i] > blocks[i - 1]:
                localMaxHeights.append(blocks[i])

    return localMaxHeights

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
    leftsideMaxHeights = localMaximaBlocksHeights(blocksOnTheLeft)
    currentMaxIndex = blocks.index(startingBlock)

    while len(blocksOnTheLeft) != 0 and len(leftsideMaxHeights) != 0:
        nextMaxIndex = blocksOnTheLeft.index(highestBlock(leftsideMaxHeights))
        for i in reversed(range(nextMaxIndex, currentMaxIndex)):
            capacityOnTheLeft += blocksOnTheLeft[nextMaxIndex] - blocksOnTheLeft[i]

        del leftsideMaxHeights[leftsideMaxHeights.index(blocksOnTheLeft[nextMaxIndex]):len(leftsideMaxHeights)]
        del blocksOnTheLeft[currentMaxIndex:len(blocksOnTheLeft)]
        currentMaxIndex = nextMaxIndex


    blocksOnTheRight = blocks[blocks.index(startingBlock)+1:len(blocks)]
    rightsideMaxHeights = localMaximaBlocksHeights(blocksOnTheRight)

    while len(blocksOnTheRight) != 0 and len(rightsideMaxHeights) != 0:
        nextMaxIndex = blocksOnTheRight.index(highestBlock(rightsideMaxHeights))
        for i in range(0, nextMaxIndex):
            capacityOnTheRight += blocksOnTheRight[nextMaxIndex] - blocksOnTheRight[i]

        del rightsideMaxHeights[0:rightsideMaxHeights.index(blocksOnTheRight[nextMaxIndex])+1]
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



