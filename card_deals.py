import random
from cards import card_deck
from scoring_game import does_it_bust, sum_cards


def deal_random_card():
    card = random.choice(list(card_deck.keys()))
    return card


def add_to_hand(card_receiver, added_card):
    card_receiver.append(added_card)


def initial_card_deal(card_receiver):
    first_card = deal_random_card()
    second_card = deal_random_card()
    add_to_hand(card_receiver, first_card)
    add_to_hand(card_receiver, second_card)
    # card_receiver[first_card] = card_deck[first_card]
    # card_receiver[second_card] = card_deck[second_card]
    #print(card_receiver)


def dealer_hit_me(card_receiver):
    hit_me = True
    dealer_sum = sum_cards(card_receiver)
    while hit_me == True:
        if dealer_sum < 17:
            new_card = deal_random_card()
            add_to_hand(card_receiver, new_card)
            dealer_sum = sum_cards(card_receiver)
            print("The dealer is drawing a card...")
        else:
            hit_me = False
    bust = does_it_bust(card_receiver)
    print(card_receiver)
    sum_player_cards = sum_cards(card_receiver)
    print(f"The sum of the dealer's cards is {sum_player_cards}")
    if bust == True:
        print("It's a bust! You win!.")
    return bust


def player_hit_me(card_receiver):
    another_card = True
    while another_card == True:
        hit_me = input("Type 'y' to get another card, type 'n' to pass.\n")
        if hit_me == "y":
            new_card = deal_random_card()
            add_to_hand(card_receiver, new_card)
            print(card_receiver)
            bust = does_it_bust(card_receiver)
            if bust:
                another_card = False

        elif hit_me == "n":
            another_card = False
        else:
            print("That is not a valid input")
            player_hit_me(card_receiver)
    bust = does_it_bust(card_receiver)
    sum_player_cards = sum_cards(card_receiver)
    print(f"The sum of your cards is {sum_player_cards}")
    if bust == True:
        print("It's a bust! The dealer wins.")
    else:
        print("Now it's the dealer's turn")
    return bust

    #sum_player_cards = sum_cards(card_receiver)
    # if sum_player_cards > 21:
    #   print(f"The sum of your cards is {sum_player_cards}")
    #   print("It's a bust! The dealer wins.")
