########################################################
#  Incubator Class File
########################################################

class Inc:
    # Some #defines
    IDLE_MODE = 0
    ACQUIRE_MORE = 1
    MAINTAIN_MODE = 2
    
    def __init__(self, num):
        self.inc_number = num
        self.mode = self.IDLE_MODE

    def get_mode(self):
        return self.mode
