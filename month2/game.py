class Games:
    def __init__(self, sport_name, no_of_teams, players_per_team):
        self.sport_name = sport_name
        self.no_of_teams = no_of_teams
        self.players_per_team = players_per_team

    def display_info(self):
        print(f"Sport: {self.sport_name}")
        print(f"Number of Teams: {self.no_of_teams}")
        print(f"Players per Team: {self.players_per_team}")
        print("-" * 30)


# Creating objects for different games
football = Games("Football", 2, 11)
basketball = Games("Basketball", 2, 5)
rugby = Games("Rugby", 2, 15)
table_tennis = Games("Table Tennis", 2, 1)

# Displaying their information
football.display_info()
basketball.display_info()
rugby.display_info()
table_tennis.display_info()
