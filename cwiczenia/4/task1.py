def countPack(lengthPod, widthPod, lengthPan, widthPan, packCapacity):
    area = lengthPod * widthPod * 1.1
    areaPan = lengthPan * widthPan
    panCount = area // areaPan
    count = panCount / packCapacity
    if count < 1:
        return 1
    else:
        return int(count) + 1

print("Ilosc opakowan: ", countPack(10,20, 1, 2, 10))