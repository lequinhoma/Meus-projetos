import random
def game():

  def get_choices():
      
      player_choice = input ("Pedra, Papel ou Tesoura:\n")

      options = ["Pedra", "Papel", "Tesoura"]
      
      computer_choice = random.choice(options)
      choices = {"player": player_choice, "computer": computer_choice}
      return choices
    
  def check_win(player , computer):
      if player == computer:
      
        return "Empatou, teu otário"
      elif player > computer:
        return "EITA PORRA, VOCÊ GANHOU" or "MEU DEUS DO CÉU, É VITORIA" or "VISH, GANHOOOU!!!"
      else: 
        return "PERDEU, FILHO DA PUTA"

      
  choices = get_choices()
  result = check_win(choices ["player"], choices ["computer"])

  print (result)



  