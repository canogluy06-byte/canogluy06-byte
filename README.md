<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Yunus Emre Canoğlu — Backend &amp; Desktop Systems Developer"/>
</p>

<p align="center">
  <a href="#öne-çıkan-sistemler"><img src="https://img.shields.io/badge/SİSTEMLER-0D1117?style=for-the-badge&labelColor=0D1117&color=512BD4"/></a>
  <a href="#mimari-yaklaşım"><img src="https://img.shields.io/badge/MİMARİ-0D1117?style=for-the-badge&labelColor=0D1117&color=7C5CFF"/></a>
  <a href="#teknoloji-yetkinliği"><img src="https://img.shields.io/badge/TEKNOLOJİ-0D1117?style=for-the-badge&labelColor=0D1117&color=F59E0B"/></a>
  <a href="#i̇letişim"><img src="https://img.shields.io/badge/İLETİŞİM-0D1117?style=for-the-badge&labelColor=0D1117&color=22C55E"/></a>
</p>

---

## Profil

Kurumsal iş yazılımı geliştiriyorum. Odağım demo veya prototip değil, **üretimde çalışan, bakımı yapılan ve gerçek kullanıcısı olan** sistemler.

Geliştirdiğim ERP bir mühendislik firmasında yaklaşık **10 istemciyle her gün** kullanılıyor; uygulamanın yanı sıra merkez sunucu kurulumunu, ağ yapılandırmasını, yedekleme stratejisini ve saha dağıtımını da ben yürüttüm. Yazılımın yalnızca kodlanan değil, **işletilen** bir şey olduğunu bu süreçte öğrendim.

<table>
<tr>
<td align="center" width="25%"><b>8</b><br/><sub>yayınlanan sistem</sub></td>
<td align="center" width="25%"><b>~10</b><br/><sub>günlük aktif istemci</sub></td>
<td align="center" width="25%"><b>3</b><br/><sub>istemci tipi, tek API</sub></td>
<td align="center" width="25%"><b>30</b><br/><sub>iş günü kurumsal staj</sub></td>
</tr>
</table>

---

## Mimari yaklaşım

Bağımlılıklar içeri doğru akar. İş kuralları veritabanını, web çatısını veya arayüzü tanımaz; bu sayede aynı domain üç farklı istemciyi besleyebiliyor.

```mermaid
flowchart TD
    subgraph Clients["İstemci Katmanı"]
        A["WinForms<br/>Masaüstü"]
        B["PWA<br/>Mobil"]
        C["Tarayıcı"]
    end

    A --> API
    B --> API
    C --> API

    subgraph Backend["Sunucu"]
        API["ASP.NET Core API<br/><i>20 REST controller</i>"]
        APP["Application<br/><i>DTO · use-case sözleşmeleri</i>"]
        INF["Infrastructure<br/><i>EF Core · JWT · BCrypt</i>"]
        DOM["Domain<br/><i>20 entity · sıfır bağımlılık</i>"]
    end

    API --> APP
    APP --> DOM
    INF --> DOM
    API -.->|DI| INF
    INF --> DB[("PostgreSQL")]

    classDef core fill:#512BD4,stroke:#7C5CFF,color:#fff,stroke-width:2px
    classDef infra fill:#0D1424,stroke:#43506B,color:#B9C4D6
    classDef client fill:#F59E0B,stroke:#F59E0B,color:#1a1a1a
    class DOM,APP core
    class API,INF,DB infra
    class A,B,C client
```

**Bu yapının pratik kazancı:** iş kuralı tek yerde durur. Puantaj hesabı değiştiğinde masaüstü, mobil ve tarayıcı aynı anda doğru davranır — üç ayrı yerde düzeltme yapılmaz.

---

## Öne çıkan sistemler

<table>
<tr>
<td width="50%" valign="top">

### [ERP Suite](https://github.com/canogluy06-byte/dotnet-erp-clean-architecture)
`.NET 10` `Clean Architecture` `PostgreSQL` `JWT`

Şantiye yönetimi için uçtan uca kurumsal sistem. Tek API üç istemciyi besler: REST servis, WinForms masaüstü ve kurulabilir PWA.

**20** entity · **20** controller · **24** masaüstü ekranı

Puantaj ve hakediş, malzeme talep onay akışı, fiyat listesi, depo, rol bazlı yetkilendirme, anlık mesajlaşma.

</td>
<td width="50%" valign="top">

### [Nearby — Venue Discovery](https://github.com/canogluy06-byte/php-venue-discovery-pwa)
`PHP 8` `MySQL` `Leaflet` `Capacitor`

Konum tabanlı mekân keşif platformu. Viewport bazlı yükleme yapan harita; veri OpenStreetMap/Overpass'tan otomatik besleniyor.

Check-in, değerlendirme, favori, liderlik tablosu, işletme sahibi paneli ve moderasyon.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Finans Takip](https://github.com/canogluy06-byte/winforms-finance-tracker)
`.NET 8` `WinForms` `SQLite`

Çek/senet vade takvimi. Takvim hücreleri ve bildirim bileşenleri hazır kontrol değil, kendi `OnPaint` uygulamalarıyla çizildi — DPI değişiminde tutarlı kalır.

Arşiv, vade bildirimleri, zamanlanmış otomatik yedekleme.

</td>
<td width="50%" valign="top">

### [Idle Music Game](https://github.com/canogluy06-byte/unity-idle-music-game)
`Unity` `C#`

Idle oyun prototipi. Arayüzün tamamı Inspector'da sürüklenerek değil, **çalışma zamanında C# ile** kuruluyor; böylece layout diff'te okunabilir ve kaynaktan birebir yeniden üretilebilir kalıyor.

</td>
</tr>
</table>

<p align="center">
  <a href="https://github.com/canogluy06-byte/php-blog-cms"><img src="https://img.shields.io/badge/Flat--File_Blog_CMS-777BB4?style=flat-square&logo=php&logoColor=white"/></a>
  <a href="https://github.com/canogluy06-byte/csharp-stock-inventory"><img src="https://img.shields.io/badge/Stok_%26_Ön_Muhasebe-239120?style=flat-square&logo=csharp&logoColor=white"/></a>
  <a href="https://github.com/canogluy06-byte/job-application-tracker"><img src="https://img.shields.io/badge/Belge_Üretim_Aracı-339933?style=flat-square&logo=node.js&logoColor=white"/></a>
  <a href="https://github.com/canogluy06-byte/php-corporate-website"><img src="https://img.shields.io/badge/Kurumsal_Web_Sitesi-E34F26?style=flat-square&logo=html5&logoColor=white"/></a>
</p>

---

## Teknoloji yetkinliği

<p align="center">
  <img src="https://skillicons.dev/icons?i=cs,dotnet,php,js,nodejs,unity,postgres,mysql,git,github,visualstudio,vscode&perline=12" alt="stack"/>
</p>

| Alan | Teknolojiler | Uygulandığı sistem |
|---|---|---|
| **Backend** | ASP.NET Core · EF Core · REST · OpenAPI | ERP Suite |
| **Mimari** | Clean Architecture · DI · katmanlı tasarım | ERP Suite |
| **Güvenlik** | JWT Bearer · BCrypt · rol bazlı yetkilendirme | ERP Suite |
| **Veritabanı** | PostgreSQL · MySQL · SQLite · şema migrasyonu | Tümü |
| **Masaüstü** | WinForms · custom `OnPaint` kontrolleri · tema katmanı | Finans Takip · ERP istemcisi |
| **Web** | PHP 8 · PDO · vanilla JS · Leaflet | Nearby · Kurumsal site · Blog |
| **Mobil** | PWA · service worker · Capacitor | Nearby |
| **Oyun** | Unity · runtime UI üretimi | Idle Music Game |
| **Operasyon** | Sunucu kurulumu · ağ yapılandırması · yedekleme · dağıtım | ERP Suite |

---

## Çalışma prensipleri

| | |
|---|---|
| **Gizli bilgi koda girmez** | Kimlik bilgileri ortam değişkenlerinden okunur; depolarda yalnızca `.env.example` bulunur. |
| **Tek kaynak, çok istemci** | İş kuralı bir kez yazılır; masaüstü, mobil ve web aynı sözleşmeyi tüketir. |
| **Veri kaybı varsayılan değildir** | Finansal ve operasyonel kayıtlarda yedekleme bir menü öğesi değil, zamanlanmış bir servistir. |
| **Bağımlılık bilinçli seçilir** | Küçük bir blog için veritabanı sunucusu, kurumsal ERP için ise tam katmanlı mimari. |

---

## İletişim

<p align="center">
  <a href="mailto:canogluy06@gmail.com"><img src="https://img.shields.io/badge/E--posta-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117"/></a>
  <a href="https://github.com/canogluy06-byte?tab=repositories"><img src="https://img.shields.io/badge/Tüm_Depolar-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117"/></a>
  <img src="https://img.shields.io/github/followers/canogluy06-byte?style=for-the-badge&logo=github&label=Takip%C3%A7i&color=512BD4&labelColor=0D1117"/>
  <img src="https://komarev.com/ghpvc/?username=canogluy06-byte&label=Görüntülenme&color=F59E0B&style=for-the-badge"/>
</p>

<p align="center">
  <sub><i>Depoların çoğu <b>portfolyo sürümüdür</b>. Gerçek müşteri verisi, kimlik bilgileri, personel kayıtları, tedarikçi ve fiyat bilgileri ile marka varlıkları kaldırılmış; yerlerine jenerik demo değerleri konmuştur. Mimari, kod ve arayüz değişmemiştir.</i></sub>
</p>
