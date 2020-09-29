from main import create_game

def test_winning_game():
    game = create_game(40, 30)
    game.server_wins_point()
    assert (game.game_over == True and game.winner == 'server')

def test_winning_game_from_advantage():
    game = create_game(40, "A")
    game.receiver_wins_point()
    assert (game.game_over == True and game.winner == 'receiver')

def test_deuce():
    game = create_game(40, 40)
    game.receiver_wins_point()
    assert game.score == [40,"A"]

def test_advantage():
    game = create_game("A", 40)
    game.receiver_wins_point()
    assert game.score == [40, 40]

def test_server_wins_first_point():
    game = create_game(0,0)
    game.server_wins_point()
    assert game.score == [15,0]

def test_receiver_wins_point_15_15():
    game = create_game(15,15)
    game.receiver_wins_point()
    assert game.score == [15,30] 
    
def test_server_wins_point_30_30():
    game = create_game(30,30)
    game.server_wins_point()
    assert game.score == [40,30] 
    
def test_full_game_with_deuce():
    game = create_game(0,0)
    game.server_wins_point()
    game.server_wins_point()
    game.receiver_wins_point()
    game.server_wins_point()
    game.receiver_wins_point()
    game.receiver_wins_point()
    game.receiver_wins_point()
    game.server_wins_point()
    game.receiver_wins_point()
    game.receiver_wins_point()
    assert (game.game_over == True and game.winner == 'receiver')

     