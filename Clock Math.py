"""
1 circle =360deg
clock gap = 12
12 hour hand covers 360 deg
1 hour hand covers 360/12 deg = 30deg
that means for min hand, 5min = 30deg (12 to 1 gap = 5min)
                         1min = 30/5deg =6deg
for hour hand,60 min = 30 deg (12 to 1 gap =1hr = 60min)
               1 min = 60/30deg = 0.5deg
"""


def hand_angle(H,M):

    #Equation for the angle of the hour hand
    hr = 0.5 * (60 * H + M)
    #Equation for the angle of the minute hand
    min = 6 * M
    #Equation for the angle between the hands
    angle = abs (hr - min)
    ## consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle
    return angle


if __name__ == '__main__':
    H, M = [int(H) for H in input().split()]

    print("{:.7f}".format(hand_angle(H,M)));
