from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='W', description='d', difficulty='Easy')
        self.assertEqual(str(workout), 'W')

    def test_activity_creation(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@example.com', team=team)
        workout = Workout.objects.create(name='W2', description='d2', difficulty='Medium')
        activity = Activity.objects.create(user=user, workout=workout, date='2025-01-01', duration_minutes=30, calories_burned=100)
        self.assertEqual(str(activity), 'U2 - W2 on 2025-01-01')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='T3', description='d3')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(str(leaderboard), 'T3 - Rank 1')
