forceload add -15000 1000 -15160 779
forceload add -300 1000 -140 1221
scoreboard objectives add finishedClones dummy
scoreboard objectives add checkclonesflag dummy
scoreboard objectives add cloneTimer dummy
scoreboard players set #checkclonesflag checkclonesflag 1
say starting clone
function hardpoint:clone/data
