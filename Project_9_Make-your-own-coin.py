import random    
class Pound:

    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
        
        self.colour="Gold"
        self.num_edges=1
        self.diameter=22.5
        self.thickness=3.15
        self.Head=True
    def __del__ (self):
        int("spent")

    def rust(self):
        self.colour="greenish"
    def clean(self):
        self.colour="gold"

    def flip(self):
        heads_options=[True , False]
        choice =random.choice(heads_options)
        self.Head=choice
