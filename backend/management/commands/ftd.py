from django.core.management.base import BaseCommand
from django.utils import timezone
import logging
import time
from backend.models import FTD,Profile
class Command(BaseCommand):
    help = 'Starting update.'

    def handle(self, *args, **kwargs):
        logger = logging.getLogger(__name__)
        while True:
            try:
                today = timezone.now()
                if today.date().day == 28:
                    last_month = today.month - 1

                    profiles = Profile.objects.all()
                    for profile in profiles:
                        ftd = FTD.objects.filter(recommended_by=profile,
                                                 created_at__month=last_month).count()

                        new_level = profile.level
                        next_level = profile.next_level

                        if ftd > 299:
                            new_level = 5
                            next_level = 300
                        elif ftd > 199:
                            new_level = 4
                            next_level = 300
                        elif ftd > 99:
                            new_level = 3
                            next_level = 200
                        elif ftd > 49:
                            new_level = 2
                            next_level = 100



                        if new_level != profile.level and profile.next_level != next_level:
                            profile.level = new_level
                            profile.next_level = next_level
                            profile.save(update_fields=['level', 'next_level'])

                        elif new_level != profile.level:
                            profile.level = new_level
                            profile.save(update_fields=['level'])

                        elif profile.next_level != next_level:
                            profile.next_level = next_level
                            profile.save(update_fields=['next_level'])


            except Exception as e:
                logger.error(f"Error updating profile {e}")


            time.sleep(86400)