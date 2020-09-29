from main import TennisGame, Scores

def test_server_wins_first_point():
    game = TennisGame(Scores.LOVE,Scores.LOVE)
    game.point_is_scored("server")
    assert game.get_score_string() == "15:0"

def test_receiver_wins_point_15_15():
    game = TennisGame(Scores.FIFTEEN,Scores.FIFTEEN)
    game.point_is_scored("receiver")
    assert game.get_score_string() == "15:30"
    
def test_server_wins_point_30_30():
    game = TennisGame(Scores.THIRTY,Scores.THIRTY)
    game.point_is_scored("server")
    assert game.get_score_string() == "40:30"

def test_deuce():
    game = TennisGame(Scores.FORTY, Scores.FORTY)
    game.point_is_scored("receiver")
    assert game.get_score_string() == "40:A"

def test_advantage():
    game = TennisGame(Scores.ADVANTAGE, Scores.FORTY)
    game.point_is_scored("receiver")
    assert game.get_score_string() == "DEUCE"

def test_winning_game():
    game = TennisGame(Scores.FORTY, Scores.THIRTY)
    game.point_is_scored("server")
    assert (game.game_over == True and game.winner == 'server')

def test_winning_game_from_advantage():
    game = TennisGame(Scores.FORTY, Scores.ADVANTAGE)
    game.point_is_scored("receiver")
    assert (game.game_over == True and game.winner == 'receiver')
    
def test_full_game_with_deuce():
    game = TennisGame(Scores.LOVE,Scores.LOVE)
    game.point_is_scored("server")
    game.point_is_scored("server")
    game.point_is_scored("receiver")
    game.point_is_scored("server")
    game.point_is_scored("receiver")    
    game.point_is_scored("receiver")    
    game.point_is_scored("receiver")
    game.point_is_scored("server")
    game.point_is_scored("receiver")
    game.point_is_scored("receiver")
    assert (game.game_over == True and game.winner == 'receiver')

     