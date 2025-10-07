from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Test database connection'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                row = cursor.fetchone()
                self.stdout.write(self.style.SUCCESS(f'Successfully connected to database'))
                self.stdout.write(f'PostgreSQL version: {row[0]}')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection failed: {str(e)}'))