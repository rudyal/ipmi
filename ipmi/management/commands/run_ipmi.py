from django.core.management.base import NoArgsCommand, CommandError
#import our database model
from ipmi.models import ipmi
from django.utils import translation
import subprocess
#import paramiko

# 0. Find hosting for django project
# 1. add ipmi script
    #a. ipmi may not(will not) run due to windows OS
# 2. alter ipmi script to save to DB
    # first we need to create, then update ???
# 3. Setup cron to run this command "manage.py run_ipmi" every 15 seconds

class Command(NoArgsCommand):
    help = 'Closes the specified ipm for voting'

    def handle_noargs(self, **options):
        self.stdout.write(' ')
        self.stdout.write('IPMI commands executed')
        p = subprocess.Popen(["C:"], stdout = subprocess.PIPE)
        self.stdout.write(p)
        #Put Script Here

        #While inside server loop

        #Parse output into variables

        #Try to save variables in DB (sqlite)
        try:
            #Example values for server, delete later
            serv_name1 = "R1A1"
            power = "OFF"
            cpu_temp = "96"

            #Put variables into array
            updated_values = {'serv_name': serv_name1, 'power': power, 'cpu_temp': cpu_temp}

            #Get server (serv_name1), if it doesnt exsist, create it
            ipm, created = ipmi.objects.get_or_create(
                serv_name=serv_name1, defaults=updated_values)
            if created:
                #serv_name1(R1A1) created, default variables were already added
                self.stdout.write('Created "%s"' % serv_name1)
            else:
                #Update serv_name1(R1A1) with our new updated_values
                try:
                    ipmi.objects.filter(serv_name=serv_name1).update(power=power,cpu_temp=cpu_temp)
                except:
                    raise CommandError('update failed error')
                self.stdout.write('Updated "%s"' % serv_name1)
            self.stdout.write('Successfully "%s"' % serv_name1)
        except:
            raise CommandError('ipmi error, creation failed')