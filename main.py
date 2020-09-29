from enum import Enum

class TennisGame:    
    def __init__(self, server_score, receiver_score):
        self.game_over = False
        self.winner = ''
        self.score = TennisScore(server_score,receiver_score)

    def point_is_scored(self, player):
       if self.game_over == False:
            self.score.increment_score(player)
            if (self.score.scores[player] == Scores.WIN):
                self.game_over = True
                self.winner = player
    
    def get_score_string(self):
        if self.game_over == True:
            score_string = '{} Wins'.format(self.winner)
        elif self.score.scores['server'] == self.score.scores['receiver'] == Scores.FORTY:
            score_string = 'DEUCE'
        else:
            score_string_dict = {'LOVE':'0','FIFTEEN':'15','THIRTY':'30','FORTY':'40','ADVANTAGE':'A'}
            score_string = '{}:{}'.format(score_string_dict[self.score.scores['server'].name],score_string_dict[self.score.scores['receiver'].name])
        return score_string
        
class TennisScore:
    def __init__(self, server_score, receiver_score):
        self.scores = {'server':server_score, 'receiver':receiver_score}

    def increment_score(self, player):
        self.scores[player] = Scores(self.scores[player].value + 1)
        self.validate_scores(player)

    def validate_scores(self, player):
        other_player = self.get_other_player(player)
        if ((self.scores[player] == Scores.ADVANTAGE) and (self.scores[other_player].value < Scores.FORTY.value)):
            self.scores[player] = Scores.WIN
        elif (self.scores[player] == self.scores[other_player] == Scores.ADVANTAGE):
            self.scores[player] = self.scores[other_player] = Scores.FORTY

    def get_other_player(self, player):
        both = ['server','receiver']
        both.remove(player)
        return both[0]

class Scores(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE = 4
    WIN = 5
