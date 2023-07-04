import cv2

# Nesne izleyicisini oluştur
tracker = cv2.TrackerCSRT_create()

# Video dosyasını oku
cap = cv2.VideoCapture('video.mp4')

# İlk frame'i oku
ret, frame = cap.read()

# İzlemek istediğimiz nesnenin ilk konumunu seç
bbox = cv2.selectROI('Tracking', frame, False)

# İzleyiciyi başlat
tracker.init(frame, bbox)

while True:
    # Video akışından bir frame al
    ret, frame = cap.read()

    # İzleyiciyi güncelle
    success, bbox = tracker.update(frame)

    # İzleyici başarılıysa, izlenen nesnenin konumunu çiz
    if success:
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255,125,25), 3, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Sonuç frame'ini göster
    cv2.imshow('Tracking', frame)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
