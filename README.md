## Object Tracking

Bu örnekte, OpenCV'nin `TrackerCSRT` sınıfını kullanarak bir video üzerinde nesne izlemeyi gerçekleştiriyoruz.

Nesne izleme, belirli bir nesnenin bir video akışı boyunca konumunu izlemek için kullanılır. Bu, özellikle video izleme, robotik görüş ve otomatik sürüş gibi uygulamalar için yararlıdır.

Bu kod örneği, 'video.mp4' adlı video dosyasındaki bir nesneyi izler. İlk olarak, kullanıcıyı nesnenin başlangıç konumunu belirlemek için bir ROI (Region of Interest) seçme ekranına yönlendirir. Daha sonra, bu ROI'yi izlemek için CSRT izleyiciyi başlatır.

### Kullanım

Aşağıdaki şekilde çalıştırabilirsiniz:

python object_tracking.py


Bu komut, 'video.mp4' isimli video dosyasında bir nesneyi izler ve sonuçları ekranda gösterir.

## Hata Çözümleri

Bazı durumlarda, `cv2.TrackerCSRT_create()` çağrısı sırasında `AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'` hatası ile karşılaşabilirsiniz. 

Bu hata, OpenCV'nin `cv2.TrackerCSRT_create()` özelliğini desteklemeyen bir sürümünü kullandığınızı gösterir.

OpenCV'nin nesne takibi özelliği, `opencv-contrib-python` paketi ile birlikte gelir ve bu paketin en son sürümünü yüklemeniz gerekir.

Python'da `opencv-contrib-python` paketini yüklemek için aşağıdaki pip komutunu kullanabilirsiniz:

```bash
pip install opencv-contrib-python
