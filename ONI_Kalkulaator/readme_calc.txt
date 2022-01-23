!!This calculator is currently only for domesticated plants, not wild
? maybe also include how much irrigation is required (next to plant requirement)
-- calculator is not taking cooking into consideration

Python
	-- plants: input
		-- cycle: plant id (json)
	-- duplicants: input

	output:
		-- required plants
		-- required calories
		-- Actually generated food
	
Json
	-- in this file we have plants and foods categorized
	-- meat, sucrose, fish, water are an exception!
		-- meat located under lettuce, frost burger
			-- 4000 barbeque = 3200 meat
		-- fish 
		-- sucrose located under grubfruit, grubfruit preserve
			-- in the list its written in grams! not kg, so 4000g = 4kg
		-- water located under tofu and liceloaf
			-- in the list its written in kilograms! not grams, so 1kg = 1000g
	-- each plant has the following
		--quantity
		--calories
		--cycle
		--food
			--calories
			--required
			
calculate how many plants, and what plants, are required for specific amount of cooked foods
