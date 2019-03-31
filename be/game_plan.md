# Setting up the Game

Collection of player hands (type: list<playerHand)
	in order they'll play
	first player determined by who has least card

	activeRound (type: Round)
	and list of previous rounds

	State of game (over? with winner?)
		- keep in mind multiple winners/win order

	Do you need to know the full deck, or could you
	just use the union of the cards in the hands
		Why you need the full deck:
			For test scenarios, playing scenarios, etc,
			if there was never a 3 of Diamonds, a diamond flush is less likely

# Setting up the Round

