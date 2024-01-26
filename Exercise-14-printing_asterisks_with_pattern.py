# Pseudocode
# 1. Print a downward half-pyramid pattern of asterisks
# PATTERN:
# * * * * *
# * * * *
# * * *
# * *
# *

# loop for asterisks going across at the top
for asterisk_across in range(6, 0, -1):
# loop for asterisks going down at the side
    for asterisk_down in range(0, asterisk_across -1):
# for printing the asterisks
        print("*", end=' ')
# for adding pattern to the asterisks
    print(" ")