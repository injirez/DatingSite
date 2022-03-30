import geopy.distance

def count_dist(first_point, second_point):

    return geopy.distance.geodesic(first_point, second_point).km

print(count_dist(first_point=(55.809288094378324, 37.79845131914668), second_point=(-35.03702443432055, -64.2515517703314)))