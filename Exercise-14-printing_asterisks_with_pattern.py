# Pseudocode
# 1. Print a downward half-pyramid pattern of asterisks
# PATTERN:
# * * * * *
# * * * *
# * * *
# * *
# *

for asterisk_across in range(6, 0, -1):
    for asterisk_down in range(0, asterisk_across -1):
        print("*", end=' ')
    print(" ")