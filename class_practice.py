class Player:
    def __init__(self, name, team):
        self.name = name
        self.xt = 1500
        self.team = team
    
    def introduce(self):
        print(f"Hello I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.players = []
        self.team_name = team_name
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
    
    def show_players(self):
        for player in self.players:
            player.introduce()

team_x = Team("Team X")
team_blue = Team("Team Blue")

team_x.add_player("Luffy")
team_blue.add_player("Low")

team_x.show_players()
team_blue.show_players()
