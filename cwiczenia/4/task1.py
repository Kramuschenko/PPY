def panel_calc(lengthPod, widthPod, lengthPan, widthPan, packCapacity):
    area = lengthPod * widthPod * 1.1
    areaPan = lengthPan * widthPan
    panCount = area // areaPan
    count = panCount / packCapacity
    if count < 1:
        return 1
    else:
        return int(count) + 1

print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))