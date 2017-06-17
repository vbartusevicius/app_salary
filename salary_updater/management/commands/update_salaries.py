from datetime import datetime

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Updates Company salaries'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            default=datetime.now().strftime('%Y-%m'),
            dest='period'
        )

    def handle(self, *args, **options):
        period = datetime.strptime(options['period'], '%Y-%m')
        self.stdout.write(self.style.SUCCESS('Given period: "%s"' % period))
