import peewee as p

db = p.SqliteDatabase('nbateams.db')

class Team(p.Model):
    tName = p.CharField()
    tPG = p.CharField()
    tSG = p.CharField()
    tSF = p.CharField()
    tPF = p.CharField()
    tC = p.CharField()
    tOwner = p.CharField()
    tCoach = p.CharField()

    class Meta:
        database = db
        table_name = 'tblTeams'

Team.create_table()
