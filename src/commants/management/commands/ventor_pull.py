from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings
import helper

STATICFILES_VENTOR_DIR = getattr(settings, 'STATICFILES_VENTOR_DIR', None)

VENDOR_STATICFILES = {

    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('download')

        completed_url = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENTOR_DIR/name
            dl_seccess = helper.download_to_local(url, out_path)

            if dl_seccess:
                completed_url.append(url)
            else:
                self.stdout.write(self.style.ERROR(
                    f'failed to download {url}'
                ))

        if set(completed_url) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated all vendor static files.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Some files were not updated.')
            )        
