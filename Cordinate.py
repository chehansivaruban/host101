import utm

coordinate_1 = (6.799876461577403, 79.92079429796134)

coordinate_2 = (6.79987785154483, 79.9208432496612)
coordinate_3 = (6.799818120361846, 79.92085590900636)
coordinate_4 = (6.799802845588296, 79.92080696323306)

utm_conversion = utm.from_latlon(coordinate_1[0],coordinate_1[1])

utm_conversion2 = utm.from_latlon(coordinate_2[0],coordinate_2[1])
utm_conversion3 = utm.from_latlon(coordinate_3[0],coordinate_3[1])
utm_conversion4 = utm.from_latlon(coordinate_4[0],coordinate_4[1])
print(utm_conversion)

print(utm_conversion2)
print(utm_conversion3)
print(utm_conversion4)

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

# examples
corners = [(utm_conversion[0], utm_conversion[1]), (utm_conversion2[0],utm_conversion2[1]), (utm_conversion3[0], utm_conversion3[1]),(utm_conversion4[0], utm_conversion4[1])]
print(PolygonArea(corners))