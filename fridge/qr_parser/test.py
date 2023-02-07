import cv2

import main as parser


filename = '/test_files/photo_2023-02-06_19-03-40.jpg'
image = cv2.imread(filename)

qr = parser.decode(image)[0]
print(qr)
