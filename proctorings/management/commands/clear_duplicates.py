from django.core.management.base import BaseCommand
from proctorings.models import FormResponse

class Command(BaseCommand):
    help = 'Clear duplicate FormResponse entries'

    def handle(self, *args, **kwargs):
        # Get all FormResponse entries and find duplicates
        entries = FormResponse.objects.all()
        seen = {}
        duplicates = []

        for entry in entries:
            key = entry.email  # Or another unique identifier
            if key in seen:
                duplicates.append(entry)
            else:
                seen[key] = entry

        # Delete duplicates
        for duplicate in duplicates:
            duplicate.delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted duplicate entry: {duplicate}'))

        self.stdout.write(self.style.SUCCESS('Finished clearing duplicates.'))
