if :x < :y 
[
    right 90
    if :z < 80 
    [
       
        forward 100
    ]
    else
    [
        
        backward 100
    ]
]
else
[
    left 90
    if :y < 80 
    [
        
        forward 100
    ]
    else
    [
        left 90
        backward 100
    ]
]