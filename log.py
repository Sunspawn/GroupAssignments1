from datetime import datetime


def log(mission, success):
    """Logs a mission.
:param mission: Mission description
:param success: Did the mission succeed? True or False
"""
    status = {True: "Succeeded", False: "Failed"}
    cur_time = datetime.now().strftime("%H:%M:%S")
    with open("logfile.txt", 'a') as log_file:
        log_file.write("Time - " + cur_time + ": Attempting: " + mission + "\nStatus: " + status[success] + "\n")
