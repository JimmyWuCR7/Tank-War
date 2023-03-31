## @file decTime.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief declining time Module
#  @date 03/23/2020


## @brief declining time in the game.
#  @details This class sets up the time duration of the game, it initialize the
#   total time of the game, make it decline and return zero when the remaning
#   time is zero.
class decTime():
    ## @brief Constructor for decTime.
    #  @details Constructor initialize the decTime and turns the total seconds
    #  into the hours:minutes:seconds.
    #  @param totalTime represents the total time of the game in seconds.
    def __init__(self, total):
        self.second = total
        self.hour = int(self.second / 3600)
        self.second = self.second % 3600
        self.minute = int(self.second / 60)
        self.second = self.second % 60

    ## @brief Make the time decline during the game.
    #  @return 0 means end the game when time is over.
    def subTime(self):
        if self.second > 0:
            self.second -= 1
        elif self.minute > 0:
            self.minute -= 1
            self.second = 59
        elif self.hour > 0:
            self.hour -= 1
            self.minute = 59
            self.second = 59
        else:
            return 0
