# BookAtlas web sitesi ve hukuki metinler

Açılış sayfası (İngilizce ve Türkçe) ile uygulamanın bağlantı verdiği hukuki metinler.

## Güncelleme

Sayfalar `build.py` ile üretilir; HTML dosyalarını elle düzenleme.

```bash
python3 build.py
```

- Ad, adres, e-posta, mağaza ve Instagram bağlantıları: `build.py` içindeki `CONFIG`.
- Türkçe hukuki metinler: `legal_tr.py`. İngilizce metinler: `legal_en.py`.
- Açılış sayfası metinleri: `build.py` içindeki `LANDING`.
- Görünüm: `assets/site.css`.

`CONFIG` içinde değeri `None` olan alanlar sayfada sarı işaretli yer tutucu olarak görünür. Bunlar doldurulmadan ve hukuki metinler bir hukukçu tarafından onaylanmadan site yayımlanmamalıdır. Onaydan sonra `CONFIG["draft"]` değerini `False` yap.

## Adresler

Uygulama `privacy_policy.html` ve `terms_of_use.html` adreslerini açar; bu dosya adları değiştirilmemelidir. Türkçe cihazlar bu sayfalardan Türkçe metinlere (`tr/`) yönlendirilir. Eski `kvkk.html` adresi yeni aydınlatma metnine yönlenir.

Site çerez, analiz aracı veya dış kaynak (font, betik) kullanmaz.
