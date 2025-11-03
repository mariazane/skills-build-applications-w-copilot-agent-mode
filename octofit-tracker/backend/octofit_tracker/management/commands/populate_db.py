from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        # Delete in order: Leaderboard, Activity, Workout, User, Team
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        # Only delete users with a PK (avoid unhashable error)
        for user in User.objects.all():
            if user.pk:
                user.delete()
        Team.objects.all().delete()

        # Create Teams

        marvel = Team.objects.create(id=1, name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(id=2, name='DC', description='DC superheroes')

        # Create Users (assigning team as ForeignKey)
        tony = User.objects.create(id=1, email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(id=2, email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(id=3, email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(id=4, email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create Activities
        Activity.objects.create(id=1, user=tony, type='run', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(id=2, user=steve, type='cycle', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(id=3, user=bruce, type='swim', duration=60, date=date(2023, 1, 3))
        Activity.objects.create(id=4, user=clark, type='run', duration=50, date=date(2023, 1, 4))

        # Create Workouts
        Workout.objects.create(id=1, name='Morning Cardio', description='Run and cycle', difficulty='Easy')
        Workout.objects.create(id=2, name='Strength', description='Weights and pushups', difficulty='Medium')

        # Create Leaderboard
        Leaderboard.objects.create(id=1, user=tony, score=300, rank=4)
        Leaderboard.objects.create(id=2, user=steve, score=400, rank=2)
        Leaderboard.objects.create(id=3, user=bruce, score=500, rank=1)
        Leaderboard.objects.create(id=4, user=clark, score=450, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
