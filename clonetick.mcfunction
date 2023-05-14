scoreboard players add #cloneTimer cloneTimer 1
scoreboard players operation #cloneInterval cloneTimer = #cloneTimer cloneTimer
scoreboard players set #secondsBetweenCheck cloneTimer 400
scoreboard players operation #cloneInterval cloneTimer %= #secondsBetweenCheck cloneTimer
execute if score #cloneInterval cloneTimer matches 0 run function hardpoint:clone/checkclones
