pendown
left 90
:move = 90
if(:x>:y)[
    if(:y>:z)[
        right 45
        forward :move
    ]else[
        left 45
        backward :move]]
    if(:w>:x)[
        right 45
        forward :move]    
else[
    if(:x>:z)[
       right 45 
       forward :move]
    else[
        left  45
        backward :move]]
    if(:w<:x)[
        right 45
        backward :move]