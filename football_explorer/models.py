
class Player(object):
    def __init__(self, number, position, name, date_of_birth,
                 caps, club, country, club_country, year):
        self.number = number
        self.position = position
        self.name = name
        self.date_of_birth = date_of_birth
        self.caps = caps
        self.club = club
        self.country = country
        self.club_country = club_country
        self.year = int(year)
        

    def __str__(self):
        return '{} - {} ({})'.format(self.position, self.name, self.country)
