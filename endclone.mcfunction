forceload remove -15000 1000 -15160 779
forceload remove -300 1000 -140 1221
scoreboard objectives remove cloneTimer
scoreboard objectives remove cloneInterval
scoreboard objectives remove checkclonesflag
tellraw @a {"text":"The value of finishedClones for cloneCount is: ","color":"green","extra":[{"score":{"name":"cloneCount","objective":"finishedClones"}}]}
scoreboard objectives remove finishedClones
