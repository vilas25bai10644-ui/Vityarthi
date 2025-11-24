"""
Sports Tournament Management System - Core Models
This module contains all the core data classes for the tournament system.
"""

import uuid
from datetime import datetime


class Player:
    """Represents a player in a team."""
    
    def __init__(self, name, age, position, jersey_number, contact):
        """
        Initialize a new Player.
        
        Args:
            name (str): Player's full name
            age (int): Player's age
            position (str): Playing position
            jersey_number (int): Unique jersey number
            contact (str): Contact phone number
        """
        self.player_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.position = position
        self.jersey_number = jersey_number
        self.contact = contact
    
    def to_dict(self):
        """Convert player object to dictionary for JSON serialization."""
        return {
            'player_id': self.player_id,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'jersey_number': self.jersey_number,
            'contact': self.contact
        }
    
    @staticmethod
    def from_dict(data):
        """Create Player object from dictionary."""
        player = Player(
            data['name'],
            data['age'],
            data['position'],
            data['jersey_number'],
            data['contact']
        )
        player.player_id = data['player_id']
        return player


class Team:
    """Represents a sports team with players and statistics."""
    
    def __init__(self, name, coach, contact):
        """
        Initialize a new Team.
        
        Args:
            name (str): Team name
            coach (str): Coach's name
            contact (str): Contact phone number
        """
        self.team_id = str(uuid.uuid4())
        self.name = name
        self.coach = coach
        self.contact = contact
        self.players = []
        self.registration_date = datetime.now().strftime("%Y-%m-%d")
        
        # Statistics
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0
    
    def add_player(self, player):
        """Add a player to the team."""
        # Check for duplicate jersey number
        for p in self.players:
            if p.jersey_number == player.jersey_number:
                raise ValueError(f"Jersey number {player.jersey_number} already exists in team")
        self.players.append(player)
    
    def remove_player(self, player_id):
        """Remove a player from the team by player_id."""
        self.players = [p for p in self.players if p.player_id != player_id]
    
    def get_goal_difference(self):
        """Calculate and return goal difference."""
        return self.goals_for - self.goals_against
    
    def update_stats(self, goals_for, goals_against, result):
        """
        Update team statistics after a match.
        
        Args:
            goals_for (int): Goals scored by this team
            goals_against (int): Goals conceded by this team
            result (str): 'win', 'draw', or 'loss'
        """
        self.matches_played += 1
        self.goals_for += goals_for
        self.goals_against += goals_against
        
        if result == 'win':
            self.wins += 1
            self.points += 3
        elif result == 'draw':
            self.draws += 1
            self.points += 1
        elif result == 'loss':
            self.losses += 1
    
    def reset_stats(self):
        """Reset all team statistics to zero."""
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0
    
    def to_dict(self):
        """Convert team object to dictionary for JSON serialization."""
        return {
            'team_id': self.team_id,
            'name': self.name,
            'coach': self.coach,
            'contact': self.contact,
            'players': [p.to_dict() for p in self.players],
            'registration_date': self.registration_date,
            'matches_played': self.matches_played,
            'wins': self.wins,
            'draws': self.draws,
            'losses': self.losses,
            'goals_for': self.goals_for,
            'goals_against': self.goals_against,
            'points': self.points
        }
    
    @staticmethod
    def from_dict(data):
        """Create Team object from dictionary."""
        team = Team(data['name'], data['coach'], data['contact'])
        team.team_id = data['team_id']
        team.players = [Player.from_dict(p) for p in data.get('players', [])]
        team.registration_date = data.get('registration_date', datetime.now().strftime("%Y-%m-%d"))
        team.matches_played = data.get('matches_played', 0)
        team.wins = data.get('wins', 0)
        team.draws = data.get('draws', 0)
        team.losses = data.get('losses', 0)
        team.goals_for = data.get('goals_for', 0)
        team.goals_against = data.get('goals_against', 0)
        team.points = data.get('points', 0)
        return team


class Match:
    """Represents a match between two teams."""
    
    def __init__(self, tournament_id, team1_id, team2_id):
        """
        Initialize a new Match.
        
        Args:
            tournament_id (str): ID of the tournament
            team1_id (str): ID of first team
            team2_id (str): ID of second team
        """
        self.match_id = str(uuid.uuid4())
        self.tournament_id = tournament_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.match_date = None
        self.venue = None
        self.team1_score = None
        self.team2_score = None
        self.status = "scheduled"  # scheduled, completed
        self.winner_id = None
    
    def set_schedule(self, match_date, venue):
        """Set the match date and venue."""
        self.match_date = match_date
        self.venue = venue
    
    def record_result(self, team1_score, team2_score):
        """
        Record the match result.
        
        Args:
            team1_score (int): Score of team 1
            team2_score (int): Score of team 2
        """
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.status = "completed"
        
        # Determine winner
        if team1_score > team2_score:
            self.winner_id = self.team1_id
        elif team2_score > team1_score:
            self.winner_id = self.team2_id
        else:
            self.winner_id = "draw"
    
    def get_result(self):
        """Get the match result as a string."""
        if self.status != "completed":
            return "Match not completed"
        
        if self.winner_id == "draw":
            return f"Draw {self.team1_score}-{self.team2_score}"
        return f"Winner: {self.winner_id}"
    
    def to_dict(self):
        """Convert match object to dictionary for JSON serialization."""
        return {
            'match_id': self.match_id,
            'tournament_id': self.tournament_id,
            'team1_id': self.team1_id,
            'team2_id': self.team2_id,
            'match_date': self.match_date,
            'venue': self.venue,
            'team1_score': self.team1_score,
            'team2_score': self.team2_score,
            'status': self.status,
            'winner_id': self.winner_id
        }
    
    @staticmethod
    def from_dict(data):
        """Create Match object from dictionary."""
        match = Match(data['tournament_id'], data['team1_id'], data['team2_id'])
        match.match_id = data['match_id']
        match.match_date = data.get('match_date')
        match.venue = data.get('venue')
        match.team1_score = data.get('team1_score')
        match.team2_score = data.get('team2_score')
        match.status = data.get('status', 'scheduled')
        match.winner_id = data.get('winner_id')
        return match
