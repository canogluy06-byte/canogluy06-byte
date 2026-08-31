<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero-dark.svg" alt="Yunus Emre Canoğlu — Kurumsal iş yazılımı · Backend, masaüstü ve saha sistemleri" width="100%">
</picture>

<p align="center">
  <a href="#öne-çıkan-sistemler"><img src="https://img.shields.io/badge/Sistemler-0D1117?style=flat-square&labelColor=0D1117&color=7C5CFF"/></a>&nbsp;
  <a href="#yetkinlik--sistem"><img src="https://img.shields.io/badge/Yetkinlik-0D1117?style=flat-square&labelColor=0D1117&color=8B6BFF"/></a>&nbsp;
  <a href="#mimari"><img src="https://img.shields.io/badge/Mimari-0D1117?style=flat-square&labelColor=0D1117&color=A886FF"/></a>&nbsp;
  <a href="#mühendislik-prensipleri"><img src="https://img.shields.io/badge/Prensipler-0D1117?style=flat-square&labelColor=0D1117&color=F5A524"/></a>&nbsp;
  <a href="#i̇letişim"><img src="https://img.shields.io/badge/İletişim-0D1117?style=flat-square&labelColor=0D1117&color=2FD97B"/></a>
</p>

<br/>

Kurumsal iş yazılımı geliştiriyorum. Odağım demo veya prototip değil, **üretimde çalışan, bakımı yapılan ve gerçek kullanıcısı olan** sistemler.

Yazdığım ERP bir mühendislik firmasında yaklaşık on istemciyle her gün kullanılıyor. Uygulamanın yanı sıra merkez sunucu kurulumunu, ağ yapılandırmasını, yedekleme stratejisini ve saha dağıtımını da ben yürüttüm — yazılımın yalnızca *kodlanan* değil **işletilen** bir şey olduğunu orada öğrendim. Konum tabanlı keşif platformum Civari ise tasarımından sunucu yönetimine kadar tek başıma geliştirilip yayına alındı ve şu an canlıda.

<br/>

## Öne çıkan sistemler

<table>
<tr>
<td width="50%" valign="top">

### ERP Suite
**`.NET 10`** · Clean Architecture · PostgreSQL · JWT

Şantiye yönetimi için uçtan uca kurumsal sistem. **Tek API üç istemciyi besler:** REST servis, WinForms masaüstü ve kurulabilir PWA.

Puantaj ve hakediş, malzeme talep onay akışı, ~3.000 kalemlik fiyat listesi, depo, rol bazlı yetkilendirme, anlık mesajlaşma.

`20 entity` `20 controller` `24 masaüstü ekranı`

**[→ Depoyu incele](https://github.com/canogluy06-byte/dotnet-erp-clean-architecture)**

</td>
<td width="50%" valign="top">

### Civari &nbsp;<sub>🟢 canlı</sub>
**`PHP 8`** · MySQL · Leaflet · Capacitor

Ankara merkezli mekân keşif platformu. Harita, mekânları görünen alana göre yükler; veri **OpenStreetMap/Overpass**'tan otomatik çekilip yerel şemaya eşlenir.

Check-in, değerlendirme, favori, liderlik tablosu, işletme sahibi paneli ve moderasyon.

`PWA` `service worker` `OSM ingest`

**[→ Depoyu incele](https://github.com/canogluy06-byte/civari)** · **[civari.com.tr](https://civari.com.tr)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Finans Takip
**`.NET 8`** · WinForms · SQLite

Çek/senet vade takvimi. Takvim hücreleri ve bildirim bileşenleri hazır kontrol değil — kendi `OnPaint` uygulamalarıyla çizildi, böylece DPI değişiminde tutarlı kalır.

Arşiv, vade bildirimleri, zamanlanmış otomatik yedekleme.

**[→ Depoyu incele](https://github.com/canogluy06-byte/winforms-finance-tracker)**

</td>
<td width="50%" valign="top">

### Idle Music Game
**`Unity`** · C#

Idle oyun prototipi. Arayüzün tamamı Inspector'da sürüklenerek değil, **çalışma zamanında C# ile** kuruluyor — layout diff'te okunabilir ve kaynaktan birebir yeniden üretilebilir kalıyor.

**[→ Depoyu incele](https://github.com/canogluy06-byte/unity-idle-music-game)**

</td>
</tr>
</table>

<p align="center">
  <a href="https://github.com/canogluy06-byte/php-blog-cms"><img src="https://img.shields.io/badge/Flat--File_Blog_CMS-777BB4?style=flat-square&logo=php&logoColor=white&labelColor=0D1117"/></a>&nbsp;
  <a href="https://github.com/canogluy06-byte/csharp-stock-inventory"><img src="https://img.shields.io/badge/Stok_%26_Ön_Muhasebe-239120?style=flat-square&logo=csharp&logoColor=white&labelColor=0D1117"/></a>&nbsp;
  <a href="https://github.com/canogluy06-byte/job-application-tracker"><img src="https://img.shields.io/badge/Belge_Üretim_Aracı-339933?style=flat-square&logo=nodedotjs&logoColor=white&labelColor=0D1117"/></a>&nbsp;
  <a href="https://github.com/canogluy06-byte/php-corporate-website"><img src="https://img.shields.io/badge/Kurumsal_Web_Sitesi-E34F26?style=flat-square&logo=html5&logoColor=white&labelColor=0D1117"/></a>
</p>

<br/>

## Yetkinlik × Sistem

Yetkinlik listesi yerine **kanıt tablosu**: her satırın hangi sistemde fiilen uygulandığı.

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/matrix-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/matrix-light.svg">
  <img src="assets/matrix-dark.svg" alt="Yetkinlik ve sistem matrisi" width="100%">
</picture>

<br/>

## Mimari

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/systems-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/systems-light.svg">
  <img src="assets/systems-dark.svg" alt="Sistem mimarisi: tek API, üç istemci" width="100%">
</picture>

Bağımlılıklar içeri doğru akar: `Domain` veritabanını, web çatısını veya arayüzü tanımaz. Pratik kazancı şu — puantaj hesabı değiştiğinde masaüstü, mobil ve tarayıcı **aynı anda** doğru davranır; üç ayrı yerde düzeltme yapılmaz.

<br/>

## Mühendislik prensipleri

| | |
|:--|:--|
| **Gizli bilgi koda girmez** | Kimlik bilgileri ortam değişkenlerinden okunur; depolarda yalnızca `.env.example` bulunur. Bu profildeki dokuz deponun hiçbirinde parola, anahtar veya müşteri verisi yoktur. |
| **Tek kaynak, çok istemci** | İş kuralı bir kez yazılır; masaüstü, mobil ve web aynı sözleşmeyi tüketir. Kural değişirse üç yerde değil, bir yerde değişir. |
| **Veri kaybı varsayılan değildir** | Finansal ve operasyonel kayıtlarda yedekleme bir menü öğesi değil, zamanlanmış bir servistir. |
| **Bağımlılık bilinçli seçilir** | Sekiz yazılık bir blog için veritabanı sunucusu gerekmez; on istemcili bir ERP için tam katmanlı mimari gerekir. Aynı cevabı her soruya vermiyorum. |
| **Görsel de koddur** | Bu sayfadaki üç grafik dış servisten gelmiyor — depoda duran, elle yazılmış, tema duyarlı SVG'ler. Üçüncü parti bir servis düştüğünde profil bozulmaz. |

<br/>

## İletişim

<p align="center">
  <a href="mailto:canogluy06@gmail.com"><img src="https://img.shields.io/badge/E--posta-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117"/></a>
  <a href="https://github.com/canogluy06-byte?tab=repositories"><img src="https://img.shields.io/badge/Tüm_Depolar-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117"/></a>
  <a href="https://civari.com.tr"><img src="https://img.shields.io/badge/civari.com.tr-F5A524?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0D1117"/></a>
</p>

<p align="center">
  <sub>Müşteri işlerinin depoları <b>portfolyo sürümüdür</b>: kimlik bilgileri, personel kayıtları, tedarikçi ve fiyat bilgileri ile marka varlıkları kaldırılmış, yerlerine jenerik demo değerleri konmuştur. Mimari, kod ve arayüz değişmemiştir. Civari kendi ürünüm olduğu için kendi kimliğiyle yayındadır.</sub>
</p>
