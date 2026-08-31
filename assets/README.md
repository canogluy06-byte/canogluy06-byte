# Profil tasarım varlıkları

Bu klasördeki altı SVG **elle yazılmış ve üretilmiştir** — hiçbir üçüncü parti
görsel servisine bağımlı değildir.

```bash
python assets/generate.py
```

`generate.py` tek bir jeton kümesinden (renk, tipografi, ızgara) hem koyu hem
açık tema varyantını üretir. README bunları `<picture>` ile ziyaretçinin
sistem temasına göre servis eder.

| Dosya | İçerik |
|---|---|
| `profile-hero-*.svg` | Başlık — isim, ünvan, teknoloji satırı, ölçüm paneli |
| `profile-matrix-*.svg` | Yetkinlik × sistem kanıt matrisi |
| `profile-systems-*.svg` | Tek API / üç istemci mimari şeması |

## Tasarım kuralları

Bunlar keyfi tercih değil, bu varlıklar geliştirilirken **canlıda karşılaşılıp
teşhis edilen** üç kısıttır.

**Görünürlük animasyona bağlanmaz.** CSS `animation-fill-mode: forwards`
kullanır, `both` değil. `both`, gecikme süresince ögeyi `from` durumunda
(`opacity: 0`) tutar; animasyon hiç ilerlemezse — indirgenmiş hareket tercihi,
statik önizleme, eski render — içerik **kalıcı olarak görünmez** kalır.
`forwards` ile gecikme boyunca ögenin normal, görünür stili geçerlidir.
`prefers-reduced-motion` ayrıca onurlandırılır.

**Aynı ögede CSS `transform` ile SVG `transform` özniteliği kullanılmaz.**
CSS özelliği sunum özniteliğini ezer: `transform: none` ile biten bir animasyon,
`transform="translate(...)"` taşıyan bir `<g>`'yi orijine düşürür. Bu yüzden
konumlandırma dış `<g>`'de, animasyon iç `<g>`'de durur.

**Dosya adı sabit kalıp içerik değişirse GitHub'ın `/raw/` uç noktası eski
sürümü servis etmeye devam edebilir.** `?v=` sorgu parametresi bu önbelleği
kırmaz — `raw.githubusercontent.com` güncel içeriği verirken profil sayfası
eskisini göstermeye devam eder. Böyle bir durumda dosya adını değiştirin.
