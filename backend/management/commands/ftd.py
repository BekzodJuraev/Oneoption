from django.core.management.base import BaseCommand
from django.utils import timezone
import logging
from django.db.models import F
import time
from decimal import Decimal
from django.db import transaction
from backend.models import FTD,Profile
class Command(BaseCommand):
    help = 'Starting update.'

    def handle(self, *args, **kwargs):
        logger = logging.getLogger(__name__)
        while True:
            try:
                today = timezone.now()
                if today.date().weekday() == 0:

                    profiles = Profile.objects.select_related('recommended_by_partner').all()
                    updates=[]
                    partners=[]

                    for profile in profiles:
                        total=profile.income_oborot + profile.income_doxod
                        profile.total_income=F('total_income') + total
                        profile.income_oborot=0
                        profile.income_doxod=0

                        if profile.recommended_by_partner:
                            partner = profile.recommended_by_partner
                            partner.total_income = F('total_income') + total * Decimal('0.1')
                            partners.append(partner)


                        updates.append(profile)

                    with transaction.atomic():
                        if updates:
                            Profile.objects.bulk_update(updates, ['total_income', 'income_oborot', 'income_doxod'])

                        if partners:
                            Profile.objects.bulk_update(partners, ['total_income'])






                    # profiles.update(
                    #     total_income=F('total_income') + F('income_oborot') + F('income_doxod'),
                    #     income_oborot=0,
                    #     income_doxod=0
                    #
                    # )



                    # profiles = Profile.objects.select_related('recommended_by_partner').annotate(
                    #     partner_income=F('total_income') * Decimal('0.1')
                    # )
                    # updates=[]
                    #
                    # for profile in profiles:
                    #     if profile.recommended_by_partner:
                    #         partner = profile.recommended_by_partner
                    #         partner.total_income = F('total_income') + profile.partner_income
                    #         updates.append(partner)
                    #
                    # print(updates)
                    #
                    #
                    # if updates:
                    #     with transaction.atomic():
                    #         Profile.objects.bulk_update(updates, ['total_income'])




                if today.date().day == 1:
                    last_month = today.month - 1 if today.month > 1 else 12

                    profiles = Profile.objects.all()
                    updates = []





                    ftd_counts = {
                        profile.id: FTD.objects.filter(recommended_by=profile, created_at__month=last_month).count()
                        for profile in profiles
                    }

                    for profile in profiles:
                        ftd = ftd_counts[profile.id]
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
                        else:
                            new_level = 1
                            next_level = 50


                        if new_level != profile.level and next_level != profile.next_level:
                            profile.level = new_level
                            profile.next_level=next_level

                        elif new_level != profile.level:
                            profile.level = new_level

                        elif next_level != profile.next_level:
                            profile.next_level = next_level

                        updates.append(profile)












                    if updates:
                        with transaction.atomic():
                            Profile.objects.bulk_update(updates,
                                                        ['level','next_level'])


            except Exception as e:
                print(e)
                logger.error(f"Error updating profile {e}")




            time.sleep(86400)