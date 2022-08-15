from cards import card_deck

def sum_cards(hand):
  sum_player_cards = 0
  num_aces = 0
  for card in hand:
    card_value = card_deck[card]
    if card_value is None:
      num_aces += 1
    else:
      sum_player_cards += card_value
  #print(f"The sum of your cards is {sum_player_cards}")
  for _ in range(num_aces):
    sum_player_cards += 11
  for _ in range(num_aces):
    if sum_player_cards > 21:
      sum_player_cards -= 10
  return sum_player_cards
def score_game(player_sum, dealer_sum):
  if player_sum > 21 or dealer_sum > 21:
    return
  print(f"Your score was {player_sum}. The dealer's score was {dealer_sum}.")
  if player_sum > dealer_sum:
    print("You win!")
  elif player_sum == dealer_sum:
    print("It's a draw!")
  else:
    print("You lose :(")

def does_it_bust(card_receiver):
  bust = False
  sum_player_cards = sum_cards(card_receiver)
  if sum_player_cards > 21:
    bust = True
    return bust
    #print(f"The sum of your cards is {sum_player_cards}")
    #print("It's a bust! The dealer wins.")
  else:
    return bust

