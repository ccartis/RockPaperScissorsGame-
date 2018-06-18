print("Rock...")
print("Paper...")
print("Scissor...")

player1=input("Player1, make your move:")
player2=input("Player2, make your move:")

if(player1=="rock" and player2=="scissor"):
	print("Player 1 wins")
elif(player1=="scissor" and player2=="rock"):
	print("Player 2 wins")
elif(player1=="paper" and player2=="scissor"):
	print("Player2 wins")
elif(player1=="scissor" and player2=="paper"):
	print("Player 1 wins")
elif(player1=="rock" and player2=="paper"):
	print("Player 2 wins ")
elif(player1=="paper" and player2=="rock"):
	print("player 1 wins")
else:
	print("None of the entries you entered are rock , paper or scissor ....PAY ATTENTION!")







