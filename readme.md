# Sports Tournament Management System

A comprehensive Python-based application for managing sports tournaments, from team registration to match scheduling, results tracking, and generating tournament standings.

## Overview

The Sports Tournament Management System automates the complete lifecycle of organizing sports tournaments. It provides tools for managing teams, creating tournaments in various formats, automatically generating match fixtures, recording results, and maintaining real-time points tables and rankings.

## Features

### 1. Team Management
- Register new teams with complete details (name, coach, contact)
- Add multiple players to teams with individual player information
- View all registered teams and their rosters
- Update team and player information
- Delete teams (with validation)

### 2. Tournament Creation
- Create tournaments with custom configurations
- Support for multiple tournament formats:
  - **Round-Robin**: Every team plays every other team once
  - **Knockout**: Single-elimination bracket
- Define tournament parameters (name, sport type, dates)
- Register teams to specific tournaments

### 3. Automated Match Scheduling
- Automatic fixture generation based on tournament format
- Intelligent round-robin algorithm ensuring fair matchups
- Knockout bracket generation with proper seeding
- Manual scheduling of match dates, times, and venues
- View complete tournament fixture calendar

### 4. Results Management
- Record match scores for completed games
- Automatic winner calculation
- Real-time team statistics updates:
  - Matches played, won, drawn, lost
  - Goals for, goals against, goal difference
  - Points calculation (Win: 3, Draw: 1, Loss: 0)

### 5. Points Table & Rankings
- Auto-generated points tables for all tournaments
- Intelligent ranking system based on:
  1. Total points (primary criterion)
  2. Goal difference (tiebreaker)
  3. Goals scored (second tiebreaker)
- Real-time standings updates after each match
- Tournament winner identification

### 6. Reports & Analytics
- Tournament summary reports
- Team performance statistics
- Complete match history
- Data export to CSV format
- Printable reports for distribution

### 7. Data Persistence
- Automatic data saving to JSON files
- Load previous tournament data on startup
- Data backup functionality
- Historical record maintenance

## Technologies/Tools Used

- **Python 3.8+**: Core programming language
- **JSON**: Data storage format
- **datetime**: Date and time handling
- **uuid**: Unique identifier generation
- **csv**: Data export functionality
- **os**: File system operations
- **PEP 8**: Python coding standards

### Python Concepts Demonstrated
- Object-Oriented Programming (Classes, Inheritance, Encapsulation)
- Data Structures (Lists, Dictionaries, Sets)
- File I/O Operations
- Exception Handling
- Algorithms (Sorting, Scheduling, Round-Robin)
- Modular Design and Code Organization

## Project Structure

```
sports_tournament_system/
│
├── main.py                      # Application entry point
├── models/
│   ├── __init__.py
│   ├── player.py               # Player class
│   ├── team.py                 # Team class
│   ├── tournament.py           # Tournament class
│   └── match.py                # Match class
│
├── managers/
│   ├── __init__.py
│   ├── team_manager.py         # Team operations
│   ├── tournament_manager.py   # Tournament operations
│   ├── match_scheduler.py      # Match scheduling logic
│   ├── results_manager.py      # Results handling
│   └── points_table.py         # Rankings calculation
│
├── utils/
│   ├── __init__.py
│   ├── data_persistence.py     # File operations
│   ├── validators.py           # Input validation
│   └── display.py              # Display formatting
│
├── data/
│   ├── teams.json              # Teams data
│   ├── tournaments.json        # Tournaments data
│   ├── matches.json            # Matches data
│   └── backups/                # Backup files
│
├── tests/
│   ├── test_team_manager.py
│   ├── test_tournament_manager.py
│   └── test_match_scheduler.py
│
├── docs/
│   ├── statement.md            # Problem statement
│   ├── requirements.md         # Detailed requirements
│   └── diagrams/               # UML diagrams
│
├── requirements.txt            # Python dependencies (if any)
└── README.md                   # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system
- Basic command-line knowledge

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sports-tournament-system.git
   cd sports-tournament-system
   ```

2. **Create data directory** (if not exists)
   ```bash
   mkdir -p data/backups
   ```

3. **Verify Python installation**
   ```bash
   python --version
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## How to Run

1. Navigate to the project directory
2. Run the main application:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu options
4. Data is automatically saved when you exit

## Usage Guide

### 1. Register Teams
- Select option 1 from main menu
- Choose "Add New Team"
- Enter team details (name, coach, contact)
- Add players to the team

### 2. Create Tournament
- Select option 2 from main menu
- Choose "Create Tournament"
- Enter tournament details and select format
- Register teams to the tournament (minimum 2 teams)

### 3. Generate Fixtures
- Select option 3 from main menu
- Choose "Generate Fixtures"
- Select tournament
- Fixtures are automatically created based on format

### 4. Record Results
- Select option 4 from main menu
- Choose "Record Match Result"
- Enter match ID and scores
- Points table updates automatically

### 5. View Reports
- Select option 5 from main menu
- Choose report type (Points Table, Match History, Team Stats)
- Export data to CSV if needed

## Testing

### Manual Testing
1. Create at least 4 teams with players
2. Create a round-robin tournament
3. Register all teams
4. Generate fixtures and verify all teams play each other
5. Record results for multiple matches
6. Verify points table calculations
7. Test data persistence by restarting the application

### Automated Testing
```bash
python -m pytest tests/
```

## Sample Test Data

### Sample Teams
- Team A (Coach: John Doe)
- Team B (Coach: Jane Smith)
- Team C (Coach: Mike Johnson)
- Team D (Coach: Sarah Williams)

### Sample Tournament
- Name: "Summer League 2024"
- Format: Round-Robin
- 4 teams, 6 matches total

## Key Algorithms

### Round-Robin Fixture Generation
```
For n teams:
  - Total matches = n * (n-1) / 2
  - Each team plays (n-1) matches
  - Algorithm ensures no team plays itself
  - No duplicate fixtures
```

### Points Calculation
```
Win: 3 points
Draw: 1 point
Loss: 0 points
Ranking: Points → Goal Difference → Goals Scored
```

## Future Enhancements

- Web-based GUI using Flask/Django
- Multi-sport support with sport-specific rules
- Player statistics tracking (individual scorers)
- Advanced analytics and data visualization
- Email notifications for match schedules
- Mobile application
- Tournament bracket visualization
- Live score updates
- Multi-language support

## Troubleshooting

### Issue: "File not found" error
**Solution**: Ensure the `data/` directory exists in the project root

### Issue: Data not persisting
**Solution**: Check file permissions for the `data/` directory

### Issue: Invalid JSON error
**Solution**: Delete corrupted JSON files, they will be recreated on next run

## Contributing

This is a student project for VITyarthi coursework. Contributions are welcome for educational purposes.

## License

This project is created for educational purposes as part of VITyarthi coursework.

## Author

**Your Name**
- Roll Number: YOUR_ROLL_NUMBER
- Course: Python Essentials
- Institution: VIT

## Acknowledgments

- VITyarthi for the project framework
- Python documentation and community
- Course instructors and mentors

---

**Note**: This project demonstrates understanding of Python fundamentals including OOP, data structures, file I/O, and algorithmic thinking as part of the Python Essentials course curriculum.