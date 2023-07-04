## Object Tracking

Bu örnekte, OpenCV'nin `TrackerCSRT` sınıfını kullanarak bir video üzerinde nesne izlemeyi gerçekleştiriyoruz.

Nesne izleme, belirli bir nesnenin bir video akışı boyunca konumunu izlemek için kullanılır. Bu, özellikle video izleme, robotik görüş ve otomatik sürüş gibi uygulamalar için yararlıdır.

Bu kod örneği, 'video.mp4' adlı video dosyasındaki bir nesneyi izler. İlk olarak, kullanıcıyı nesnenin başlangıç konumunu belirlemek için bir ROI (Region of Interest) seçme ekranına yönlendirir. Daha sonra, bu ROI'yi izlemek için CSRT izleyiciyi başlatır.

### Kullanım

Aşağıdaki şekilde çalıştırabilirsiniz:

python object_tracking.py


Bu komut, 'video.mp4' isimli video dosyasında bir nesneyi izler ve sonuçları ekranda gösterir.
