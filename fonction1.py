def volume (a,b,c,masse_volumique):
    import math
    volume_e = (4/3)* math.pi* a *b *c
    masse = masse_volumique * volume_e
    return volume_e, masse


