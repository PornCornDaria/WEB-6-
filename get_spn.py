def get_spn(toponym):
    lower_corner = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    upper_corner = toponym['boundedBy']['Envelope']['upperCorner'].split()
    spn_1 = float(upper_corner[0]) - float(lower_corner[0])
    spn_2 = float(upper_corner[1]) - float(lower_corner[1])
    return spn_1, spn_2
