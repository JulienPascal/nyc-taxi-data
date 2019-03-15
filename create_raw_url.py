#Python file to create raw_data_urls.txt
#---------------------------------------
from pathlib import Path
import os
import sys
import datetime
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
cwd = os.getcwd()

#-------------------------------------------------------------------------------
# Constant
#-------------------------------------------------------------------------------
# year, month, day
startingDateFHV=datetime(2015, 1, 1)
startingDateGreen=datetime(2013, 8, 1)
startingDateYellow=datetime(2009, 1, 1)
# basic structures
rootFHV="https://s3.amazonaws.com/nyc-tlc/trip+data/fhv_tripdata_"
rootGreen="https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_"
rootYellow="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_"

print("Current directory is "+cwd)
my_file = Path(cwd + "/raw_data_urls.txt")

# source:https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond already with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

if my_file.is_file() == True:
    if query_yes_no(str(my_file) + " already exists. Would you like to overwrite it?") == True:
        print("Replacing file.")
        os.rename(str(my_file), str(Path(cwd + "/raw_data_urls_"))+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt")
    else:
        print("Stopping execution here.")
        exit()


urlsFile = open(str(my_file),'w')
#Write FHV
#Write Green
#Write Yellow
for (startingDate, taxiType) in zip([startingDateFHV, startingDateGreen, startingDateYellow], ['FHV','Green','Yellow']):
    print(taxiType)
    d, end = startingDate, now
    delta = relativedelta(months=+1)
    while d <= now:
        print(d.strftime("%Y-%m"))
        if taxiType == "FHV":
            urlsFile.write(rootFHV + d.strftime("%Y-%m") + ".csv\n")
        elif taxiType == "Green":
            urlsFile.write(rootGreen + d.strftime("%Y-%m") + ".csv\n")
        elif taxiType == "Yellow":
            urlsFile.write(rootYellow + d.strftime("%Y-%m") + ".csv\n")
        d += delta

urlsFile.close()
