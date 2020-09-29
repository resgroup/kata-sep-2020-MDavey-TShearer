from main import TennisGame, Scores

def test_server_wins_first_point():
    game = TennisGame(Scores.LOVE,Scores.LOVE)
    game.server_wins_point()
    assert game.get_score_string() == "15:0"

def test_receiver_wins_point_15_15():
    game = TennisGame(Scores.FIFTEEN,Scores.FIFTEEN)
    game.receiver_wins_point()
    assert game.get_score_string() == "15:30"
    
def test_server_wins_point_30_30():
    game = TennisGame(Scores.THIRTY,Scores.THIRTY)
    game.server_wins_point()
    assert game.get_score_string() == "40:30"

def test_deuce():
    game = TennisGame(Scores.FORTY, Scores.FORTY)
    game.receiver_wins_point()
    assert game.get_score_string() == "40:A"

def test_advantage():
    game = TennisGame(Scores.ADVANTAGE, Scores.FORTY)
    game.receiver_wins_point()
    assert game.get_score_string() == "DEUCE"

def test_winning_game():
    game = TennisGame(Scores.FORTY, Scores.THIRTY)
    game.server_wins_point()
    assert (game.game_over == True and game.winner == 'server')

def test_winning_game_from_advantage():
    game = TennisGame(Scores.FORTY, Scores.ADVANTAGE)
    game.receiver_wins_point()
    assert (game.game_over == True and game.winner == 'receiver')
    
def test_full_game_with_deuce():
    game = TennisGame(Scores.LOVE,Scores.LOVE)
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

     