from enum import Enum

class TennisGame:    
    def __init__(self, server_score, receiver_score):
        self.game_over = False
        self.winner = ''
        self.score = TennisScore(server_score,receiver_score)

    def server_wins_point(self):
        if self.game_over == False:
            self.score.increment_server_score()
            if (self.score.server_score == Scores.WIN):
                self.game_over = True
                self.winner = 'server'
        
    def receiver_wins_point(self):
        if self.game_over == False:
            self.score.increment_receiver_score()
            if (self.score.receiver_score == Scores.WIN):
                self.game_over = True
                self.winner = 'receiver'
    
    def get_score_string(self):
        if self.game_over == True:
            score_string = '{} Wins'.format(self.winner)
        elif self.score.server_score == self.score.receiver_score == Scores.FORTY:
            score_string = 'DEUCE'
        else:
            score_string_dict = {'LOVE':'0','FIFTEEN':'15','THIRTY':'30','FORTY':'40','ADVANTAGE':'A'}
            score_string = f'{score_string_dict[self.score.server_score.name]}:{score_string_dict[self.score.receiver_score.name]}'
        return score_string
    
        
class TennisScore:
    def __init__(self, server_score, receiver_score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def increment_server_score(self):
        self.server_score = Scores(self.server_score.value + 1)
        self.validate_scores()
    
    def increment_receiver_score(self):
        self.receiver_score = Scores(self.receiver_score.value + 1)
        self.validate_scores()

    def validate_scores(self):
        if (self.server_score == Scores.ADVANTAGE and self.receiver_score.value < Scores.FORTY.value):
            self.server_score = Scores.WIN
        if (self.receiver_score == Scores.ADVANTAGE and self.receiver_score.value < Scores.FORTY.value):
            self.receiver_score = Scores.WIN
        elif (self.server_score == self.receiver_score == Scores.ADVANTAGE):
            self.server_score = Scores.FORTY
            self.receiver_score = Scores.FORTY

class Scores(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE = 4
    WIN = 5

