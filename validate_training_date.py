import cv2 as cv

with open("annotation.txt", "r") as f:
    annotations = f.readlines()

for annot in annotations:
    path, xmin, ymin, xmax, ymax, _ = annot.split(",")
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)
    img = cv.imread(path)
    print(img)
    cv.rectangle(img, (xmin, ymin), (xmax, ymax),  (0, 255, 0) ,3)
    cv.imshow('img', img)
    cv.waitKey(0)