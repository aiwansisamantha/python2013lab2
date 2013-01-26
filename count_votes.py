# Filename: count_votes.py
# Author: Samantha Ai
# Description: Count the number and percentage of votes garnered by each party.

# entries
WP = 0
PAP = 0
RP = 0
SDA = 0
spoilt = 0

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

    percent_PAP = percentage(PAP)
    percent_RP = percentage(RP)
    percent_WP = percentage(WP)
    percent_SDA = percentage(SDA)
    percent_spoilt = percentage(spoilt)
    
    # close file
    votes.close()
except IOError:
    print('Error reading from VOTES.DAT.')
