import sys
import math
#args <begin: x y z> <end: x y z> <destination: x y z> [maskMode: MaskMode] [cloneMode: CloneMode]
#example: python script.py 0 0 0 15 15 15 40 20 30 replace normal

if(len(sys.argv) != 12):
    print("incorrect number of args")
    sys.exit()

beginX = int(sys.argv[1])
beginY = int(sys.argv[2])
beginZ = int(sys.argv[3])
endX = int(sys.argv[4])
endY = int(sys.argv[5])
endZ = int(sys.argv[6])
destinationX = int(sys.argv[7])
destinationY = int(sys.argv[8])
destinationZ = int(sys.argv[9])
maskMode = sys.argv[10]
cloneMode = sys.argv[11]


#finds the inside-edge of the chunk you are in 
def findBorder(num,direction):
    if num >= 0 and num < 16:
        if direction == 1:
            return 15
        else:
            return 0

    if num >= -16 and num < 0:
        if direction == 1:
            return -1
        else:
            return -16
        
    nearest = num / 16


    if direction == 1:
        if nearest > 0:
            return (math.ceil(nearest)*16)-1
        else:
            return (math.ceil(nearest)*16)-1
        

    if direction == -1:
        if nearest > 0:
            return (math.floor(nearest)*16)
        else:
            return (math.floor(nearest)*16)



if beginX < endX:
    directionX = 1
else:
    directionX = -1

if beginZ < endZ:
    directionZ = 1
else:
    directionZ = -1

if beginX < 0:
    partialChunkOne = beginX % 16
else:
    partialChunkOne = (beginX+1) % 16

if endX < 0:
    partialChunkTwo = endX % 16
else:
    partialChunkTwo = (endX+1) % 16

if beginZ < 0:
    partialChunkThree = beginZ % 16
else:
    partialChunkThree = (beginZ+1) % 16

if endZ < 0:
    partialChunkFour = endZ % 16
else:
    partialChunkFour = (endZ+1) % 16


numChunksX = math.ceil(abs(beginX-endX)/16)
numChunksX += (partialChunkOne!= 0)+(partialChunkTwo!=0)
if((partialChunkOne+partialChunkTwo)>=16):
    numChunksX -= 1

numChunksZ = math.ceil(abs(beginZ-endZ)/16)
numChunksZ += (partialChunkThree!=0)+(partialChunkFour!=0)
if((partialChunkThree+partialChunkFour)>=16):
    numChunksZ -= 1


selection = [[0 for x in range(numChunksX)] for z in range(numChunksZ)]

def solve():
    file = open("clone.mcfunction","w")

    counterX = 0
    counterZ = 0
    x,y,z,end_x,end_y,end_z,destx,desty,destz = 0,0,0,0,0,0,0,0,0
    firstFullChunkX = 0
    firstFullChunkZ = 0
    for row in selection:
        for chunk in row:

            if counterX == 0:
                x = beginX
                firstFullChunkX = findBorder(beginX,directionX)
                end_x = firstFullChunkX
            if counterX >0:
                x = (firstFullChunkX+directionX)+(16*(counterX-1)*directionX)
                end_x = x + (15*directionX)
            if counterX == numChunksX:
                end_x = endX
                x = findBorder(end_x,directionX*-1)

            if counterZ == 0:
                z = beginZ
                firstFullChunkZ = findBorder(beginZ,directionZ)
                end_z = firstFullChunkZ
            if counterZ >0:
                z = (firstFullChunkZ+directionZ)+(16*(counterZ-1)*directionZ)
                end_z = z + (15*directionZ)
            if counterZ == numChunksZ:
                end_z = endZ
                z = findBorder(end_z,directionZ*-1)
            
            y = beginY
            end_y = endY

            destx = destinationX + x-beginX
            desty = destinationY
            destz = destinationZ + z-beginZ
            command = "clone {x} {y} {z} {end_x} {end_y} {end_z} {destx} {desty} {destz} {maskMode} {cloneMode}\n".format(x=x,y=y,z=z,end_x=end_x,end_y=end_y,end_z=end_z,destx=destx,desty=desty,destz=destz,maskMode=maskMode,cloneMode=cloneMode)
            file.write(command)

            counterX += 1
        counterX = 0
        counterZ += 1
    file.close()

solve()