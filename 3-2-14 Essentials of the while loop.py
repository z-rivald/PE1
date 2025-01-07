blocks = int(input("Enter the number of blocks: "))
height = 0
block_changed = 0
j = 1 #metric shows when the height should be increased (difference btw act block number and block when the height increased)
block = 1 #1-st block to build pyramid
while blocks:
    if block - block_changed == j:
        block_changed = block #memorize block when the height increased
        height += 1
        j += 1
    block += 1
    blocks -= 1

print("The height of the pyramid:", height)

