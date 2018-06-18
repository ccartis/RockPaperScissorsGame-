print("Rock...")
print("Paper...")
print("Scissor...")

player1=input("Player1, make your move:")
player2=input("Player2, make your move:")

if player1=="rock":
	if player2=="scissors":
		print("player1 wins!")
	elif player2=="paper":
		print("player2 wins!")
	elif player2=="rock":
		print("Its a tie")
	else:
		print("Not a valid input player 2")
		
		
elif player1=="paper":
	if player2=="scissors":
		print("player 2 wins")
	elif player2=="rock":
		print("player1 wins")
	elif player2=="paper":
		print("Its a tie")
	else:
		print("Not a valid input player 2")
		
		
	
		
elif player1=="scissors":
	if player2=="rock":
		print("player 2 wins")
	elif player2=="paper":
		print("player 1 wins")
	elif player=="scissors":
		print("Its a tie")
	else:
		print("Not a valid input player 2")
		
		



else:
	print("None of the entries player 1 entered were rock,paper or scissor...step it up player 1")

		






