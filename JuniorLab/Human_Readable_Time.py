'''
Write a function, which takes an int number of sec and returns time in HH:MM:SS
HH - hours, max - 99
MM - minutes, max - 59
SS - seconds, max - 59
Max return time 99:59:59 for 359999 sec
'''

seconds = 359999
def humanreadable(seconds):
    hours = seconds // 3600
    if len(str(hours)) == 1:
        hours = '0' + str(hours)
    minutes = seconds % 3600 // 60
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    sec = (seconds % 3600) % 60
    if len(str(sec)) == 1:
        sec = '0' + str(sec)
    return str(hours) + ':' + str(minutes) + ':' + str(sec)

print(humanreadable(seconds))
