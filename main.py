from enum import Enum

class TennisGame:    
    def __init__(self, server_score, receiver_score):
        self.game_over = False
        self.score = TennisScore(server_score,receiver_score)

    def server_wins_point(self):
        self.score.increment_server_score()
        if (self.score.server.score.WIN):
            self.game_over = True
            self.winner = 'server'
        
    def reciever_wins_point(self):
        self.score.increment_receiver_score()
        if (self.score.receiver.score.WIN):
            self.game_over = True
            self.winner = 'receiver'
    
        
class TennisScore:
    def __init__(self, server_score, receiver_score):
        self.server = TennisPlayer('server', server_score)
        self.receiver = TennisPlayer('receiver', receiver_score)

    def increment_score(self, score, player):
        if player.score == Scores.ADVANTAGE:
            player.score = Scores.WIN
        
        else: 
            score = Scores(score.value + 1)
        if score == [Scores.FORTY,Scores.FORTY]:
            score = player.score = DEUCE
        return score

    def increment_server_score(self):
        self.server.score = self.increment_score(self.receiver.score)

    def increment_receiver_score(self):
        self.receiver.score = self.increment_score(self.server.score)

class TennisPlayer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Scores(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE = 4
    ADVANTAGE = 5 
    WIN = 6
