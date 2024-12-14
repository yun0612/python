class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
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

    # players에서 특정 player를 제거하는 메소드
    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
    
    def show_players(self):
        for player in self.players:
            player.introduce()
    
    # 팀의 xp 총합을 출력하는 메소드
    def show_total_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"{self.team_name} has {total_xp} points")

team_x = Team("Team X")
team_blue = Team("Team Blue")

team_x.add_player("Luffy")
team_blue.add_player("Low")
team_blue.add_player("Penguin")

team_blue.show_total_xp()
team_x.show_total_xp()

team_blue.remove_player("Low")

team_x.show_players()
team_blue.show_players()
