import poker,random
import pokerkit
import treys

class Game:
    def __init__(self,num_players:int = 2):
        self.num_players = num_players
        self.deck = treys.Deck()
        # random.shuffle(self.deck)
        self.player_hands = []
        for player in range(self.num_players):
            self.player_hands.append(self._create_hand())

    
    def _create_hand(self):
        hand = self.deck.draw(2)
        hand.sort(reverse=True)
        return hand
    
    def reset(self):
        self.deck = treys.Deck()
        # random.shuffle(self.deck)
        self.player_hands = []
        for player in range(self.num_players):
            self.player_hands.append(self._create_hand())
    
    def run_flop(self):
        self.flop = self.deck.draw(3)
        self.table = self.flop.copy()

    def run_turn(self):
        self.turn = self.deck.draw(1)
        self.table = self.flop + self.turn

    def run_river(self):
        self.river = self.deck.draw(1)
        self.table = self.flop + self.turn + self.river

    def run_game(self):
        self.run_flop()
        self.run_turn()
        self.run_river()

    def evaluate(self,hand):
        return treys.Evaluator().evaluate(hand,self.table)
    
    def pretty_eval(self):
        treys.Evaluator().hand_summary(self.table,self.player_hands)
    
    


if __name__=="__main__":
    game = Game(2)
    # print(treys.Card.print_pretty_cards(game.player_hands))
    print(type(game.player_hands[0][0]))
    print(treys.Card.int_to_str(game.player_hands[0][0]))
    print(treys.Card.ints_to_pretty_str(game.player_hands[0]))
    print("Player 1:",end=" ")
    treys.Card.print_pretty_cards(game.player_hands[0])
    print("Player 2:",end=" ")
    treys.Card.print_pretty_cards(game.player_hands[1])
    game.run_flop()
    # treys.Card.print_pretty_cards(game.flop)
    # treys.Card.print_pretty_cards(game.table)
    game.run_turn()
    # treys.Card.print_pretty_cards(game.turn)
    # treys.Card.print_pretty_cards(game.table)
    game.run_river()
    # treys.Card.print_pretty_cards(game.river)
    treys.Card.print_pretty_cards(game.table)

    print(game.evaluate(game.player_hands[0]))
    print(game.evaluate(game.player_hands[1]))

    treys.Evaluator().hand_summary(game.table,game.player_hands)
    