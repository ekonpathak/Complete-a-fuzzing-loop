
    if (:x < 10)
	[
        if (:y < 70)
		[
			if (:z > 10)
			[
				left 90
				backward 70
				
			]
			else
			[
				right 45
				forward 30
			]
			
		]
		else
		[
			left 90
			forward 100
		]
		
	]
	else
	[
		if (:y< 30)
		[
			if (:z < 30)
			[
				forward 20
				
			]
			else
			[
				backward 30
			]
		]	
		else
			[	
			right 90
			backward 50
			]
		
	]
	
