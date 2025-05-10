def generate_usa_bboxes():

    bboxes = []
    for lat in range(25, 50):  # Enlem (Güney-Kuzey)
        for lng in range(-125, -65):  # Boylam (Batı-Doğu)
            bbox = f"{lng},{lat},{lng+1},{lat+1}"
            bboxes.append(bbox)
    return bboxes