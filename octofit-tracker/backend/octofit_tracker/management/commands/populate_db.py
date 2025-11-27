from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Heavy lifting', difficulty='Hard')
        workout2 = Workout.objects.create(name='Speed Run', description='Fast running', difficulty='Medium')
        workout3 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', difficulty='Easy')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], workout=workout1, date=timezone.now().date(), duration_minutes=60, calories_burned=500)
        Activity.objects.create(user=users[1], workout=workout2, date=timezone.now().date(), duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workout3, date=timezone.now().date(), duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=users[3], workout=workout1, date=timezone.now().date(), duration_minutes=50, calories_burned=450)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=900, rank=1)
        Leaderboard.objects.create(team=dc, total_points=750, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))