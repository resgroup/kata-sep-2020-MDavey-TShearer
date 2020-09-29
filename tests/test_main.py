from main import TennisGame, Scores

def test_server_wins_first_point():
    game = TennisGame(Scores.LOVE,Scores.LOVE)
    game.server_wins_point()
    assert game.score == [Scores.FIFTEEN,Scores.LOVE]

def test_receiver_wins_point_15_15():
    game = TennisGame(Scores.FIFTEEN,Scores.FIFTEEN)
    game.receiver_wins_point()
    assert game.score == [Scores.FIFTEEN,Scores.THIRTY] 
    
def test_server_wins_point_30_30():
    game = TennisGame(Scores.THIRTY,Scores.THIRTY)
    game.server_wins_point()
    assert game.score == [Scores.FORTY,Scores.THIRTY]

def test_deuce():
    game = TennisGame(Scores.FORTY, Scores.FORTY)
    game.receiver_wins_point()
    assert game.score == [Scores.FORTY,Scores.ADVANTAGE]

def test_advantage():
    game = TennisGame(Scores.ADVANTAGE, Scores.FORTY)
    game.receiver_wins_point()
    assert game.score == [Scores.FORTY, Scores.FORTY]

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

     