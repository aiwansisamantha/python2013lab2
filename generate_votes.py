# Filename: generate_votes.py
# Author: Samantha Ai
# Description: Generate a suitable delimited file VOTES.DAT containing a reasonable number of records.

import random

try:
    votes = open("VOTES.DAT", 'w')

    # total number of votes: 33,281
    # randomly generate votes
    # must have some invalid votes as well

    # every vote
    for i in range(0,33281):
        # small occurrence of invalid votes
        valid_or_invalid = random.randint(0, 100)
        if valid_or_invalid == 1 or valid_or_invalid == 2:
            # when votes are spoilt, content does not matter
            # write to file
            votes.write("Spoilt vote." + '\n')
        else:
            # generate valid vote
            # according to http://en.wikipedia.org/wiki/Singaporean_general_election,_2011, PAP - 50%, SDA - 5%, WP - 45%, RP - 5%
            # RP was not included so will give an estimate of 5% -- ASSUMPTION
            which = random.randint(1,11)
            if which < 6:
                party = 'PAP'
            elif which == 6:
                party = 'SDA'
            elif which == 7:
                party = 'RP'
            elif which > 7:
                party = 'WP'
            # complete valid format
            party = party + ',1'
            # write to file
            votes.write(party + '\n')

    # close file
    votes.close()
except IOError:
    print('Error creating or writing to VOTES.DAT.')
