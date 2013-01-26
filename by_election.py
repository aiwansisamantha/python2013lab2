# Filename: by_election.py
# Author: Samantha Ai
# Description: Display the by election results, output to screen and RESULTS.TXT

# need data from previous program

# entries
WP = 0
PAP = 0
RP = 0
SDA = 0
spoilt = 0
total = 0
# check if vote is valid
def validate(vote):
    # valid votes are PAP,1 RP,1 SDA,1 WP,1
    if vote == 'PAP,1' or vote == 'RP,1' or vote == 'SDA,1' or vote == 'WP,1':
        return True
    else:
        return False

# count each vote
def count(vote):
    global WP
    global PAP
    global RP
    global SDA
    if vote[0:-3] == 'WP':
        WP = WP + 1
    if vote[0:-3] == 'PAP':
        PAP = PAP + 1
    if vote[0:-3] == 'RP':
        RP = RP + 1
    if vote[0:-3] == 'SDA':
        SDA = SDA + 1

# calculate percentage
def percentage(a):
    global total
    total = WP + PAP + RP + SDA + spoilt
    return (str("{0:.2f}".format((a/total) * 100)) + '%')

# main
# read from VOTES.DAT
try:
    votes = open('VOTES.DAT', 'r')
    lines = votes.readlines()

    # for each entry
    for line in lines:
        validate(line)
        if True:
            count(line)
        else:
            spoilt = spoilt + 1
   
    # close file
    votes.close()
except IOError:
    print('Error reading from VOTES.DAT.')

percent_PAP = percentage(PAP)
percent_RP = percentage(RP)
percent_WP = percentage(WP)
percent_SDA = percentage(SDA)
percent_spoilt = percentage(spoilt)

# ---------------------------------------------------------

##     DATE: DD/MM/YYYY                 TIME: HH:MM AM/PM
##     RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION
##     WARD                PARTY     #VOTES    %VOTES
##     --------------------------------------------------
##     PUNGGOL EAST SMC    PAP        99999    99.99%
##                         RP         99999    99.99%
##                         SDA        99999    99.99%
##                         WP         99999    99.99%
##     --------------------------------------------------
##     WINNER: <Party with highest percentage of votes>
##     TOTAL VOTES: 
##     #SPOILT VOTES:
##     %SPOILT VOTES:

import datetime
import time

# determine time and date
current_date = datetime.datetime.now()
current_date = current_date.strftime("DATE: %d/%m/%Y                 TIME: %I:%M %p")

# determine winner
if PAP > RP and PAP > SDA and PAP > WP:
    winner = 'PAP'
elif RP > PAP and RP > SDA and RP > WP:
    winner = 'RP'
elif SDA > PAP and SDA > RP and SDA > WP:
    winner = 'SDA'
else:
    winner = 'WP'
    
# write to RESULTS.TXT
try:    
    output = open("RESULTS.TXT", 'w')
    output.write(current_date + '\n')
    output.write("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION" + '\n')
    output.write("WARD                PARTY     #VOTES    %VOTES" + '\n')
    output.write("--------------------------------------------------" + '\n')
    output.write("PUNGGOL EAST SMC    PAP        " + "{0:>5s}".format(str(PAP)) + "    " + "{0:>6s}".format(percent_PAP) + '\n')
    output.write("                    RP         " + "{0:>5s}".format(str(RP)) + "    " + "{0:>6s}".format(percent_RP) + '\n')
    output.write("                    SDA        " + "{0:>5s}".format(str(SDA)) + "    " + "{0:>6s}".format(percent_SDA) + '\n')
    output.write("                    WP         " + "{0:>5s}".format(str(WP)) + "    " + "{0:>6s}".format(percent_WP) + '\n')
    output.write("--------------------------------------------------" + '\n')
    output.write("WINNER: " + winner + '\n')
    output.write("TOTAL VOTES: " + str(total) + '\n')
    output.write("#SPOILT VOTES: " + str(spoilt) + '\n')
    output.write("%SPOILT VOTES: " + percent_spoilt)
    output.close()
except IOError:
    print("Error creating or writing to RESULTS.TXT.")

# read from RESULTS.TXT and output to screen
try:
    read = open("RESULTS.TXT", 'r')
    lines = read.readlines()
    for line in lines:
        print(line)

    read.close()
except IOError:
    print("Error displaying results here. Please refer to RESULTS.TXT.")
