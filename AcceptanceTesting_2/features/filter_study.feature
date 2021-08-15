# language: en

Feature: Search games by developer

    @gamesByStudy
    Scenario: Filter games that has been developed by Nintendo
        Given a set of games
        | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
        | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
        | Splatoon                   | 2016         | Nintendo             | T      |
        | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
        | The Last of Us             | 2013         | Naughty Dog          | M      |
        Given the user chooses study: Nintendo
        When the user search games by study
        Then 1 games will match
        And the names of these games are
        | NAME                       |
        | Splatoon                   |
        And the following message is displayed: A game developed by Nintendo was found.
    
    @gamesByStudy
    Scenario: Filter games by rating without finding results
        Given a set of games
        | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
        | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
        | Splatoon                   | 2016         | Nintendo             | T      |
        | The Last of Us             | 2013         | Naughty Dog          | M      |
        Given the user chooses study: Bandai Namco Studios
        When the user search games by study
        Then 0 games will match
        And the following message is displayed: No game developed by Bandai Namco Studios found.
