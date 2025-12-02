import sys,os,json
from game import Game
import treys
import tqdm

def main():
    if len(sys.argv) > 2:
        num_players = int(sys.argv[1])
        loop_len = int(sys.argv[2])
    elif len(sys.argv) > 1:
        num_players = int(sys.argv[1])
        loop_len = 50_000
    else:
        num_players = 2
    
    game = Game(num_players)
    result = {}
    for _ in tqdm.tqdm(range(loop_len),colour="red"):
        game.reset()
        game.run_game()

        min_eval = float("inf")
        winner_id = 0
        for i in range(num_players):
            eval = game.evaluate(game.player_hands[i])
            if eval < min_eval:
                min_eval = eval
                winner_id = i
        

        for player in range(num_players):
            key_name = create_dict_key(game.player_hands[player])
            try:
                result[key_name][1] += 1
            except KeyError:
                result[key_name] = [0,1]

            if player == winner_id:
                result[key_name][0] += 1

            
    with open(f"result_{num_players}.json","w",encoding="utf-8") as file:
        json.dump(result,file,ensure_ascii=False,indent=2)

def create_dict_key(hand:list[treys.Card]):
    first_card = treys.Card.int_to_str(hand[0])
    second_card = treys.Card.int_to_str(hand[1])
    if first_card[0] == second_card[0]:
        return f"{first_card[0]}"*2
    if first_card[1] == second_card[1]:
        return f"{first_card[0]}{second_card[0]}s"
    return f"{first_card[0]}{second_card[0]}o"

if __name__=="__main__":
    main()