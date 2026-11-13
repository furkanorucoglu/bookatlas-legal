# Türkçe hukuki metinler. build.py tarafından sayfaya dönüştürülür.
#
# {{CONTROLLER}}, {{ADDRESS}}, {{EMAIL}} gibi alanlar build.py içindeki CONFIG
# sözlüğünden doldurulur. Metinler TASLAKTIR; yayımlanmadan önce bir hukukçu
# tarafından gözden geçirilmelidir.

RECIPIENTS_TABLE = """
<div class="table-scroll">
<table>
  <thead>
    <tr><th>Alıcı</th><th>Ülke</th><th>Aktarılan veri</th><th>Amaç</th></tr>
  </thead>
  <tbody>
    <tr><td>Supabase Inc.</td><td>{{SUPABASE_REGION}}</td><td>Hesap, profil, kitap kayıtları, okuma listesi, hedefler, öneri geçmişi, profil fotoğrafı, oturum ve erişim kayıtları</td><td>Veritabanı, kimlik doğrulama, dosya saklama ve sunucu işlevleri</td></tr>
    <tr><td>Anthropic PBC</td><td>ABD</td><td>Okuduğunuz kitapların adı, yazarı ve ülkesi; daha önce önerilen eserler; asistana yazdığınız istek. Adınız, e-posta adresiniz ve kullanıcı kimliğiniz gönderilmez.</td><td>Yapay zekâ destekli kitap ve film önerilerinin üretilmesi</td></tr>
    <tr><td>Google LLC (Google Books)</td><td>ABD</td><td>Kitap arama sorgunuz veya ISBN numarası (sunucumuz üzerinden iletilir); kapak görseli yüklenirken IP adresiniz</td><td>Kitap bilgisi ve kapak görseli</td></tr>
    <tr><td>Internet Archive (Open Library)</td><td>ABD</td><td>Kitap arama sorgunuz veya ISBN numarası (sunucumuz üzerinden iletilir); kapak görseli yüklenirken IP adresiniz</td><td>Kitap bilgisi ve kapak görseli</td></tr>
    <tr><td>OpenStreetMap Foundation (Nominatim)</td><td>Birleşik Krallık</td><td>Kitap kaydına girdiğiniz şehir ve ülke adı (sunucumuz üzerinden iletilir)</td><td>Şehrin haritada konumlandırılması</td></tr>
    <tr><td>OMDb API</td><td>ABD</td><td>Önerilen filmin adı ve yılı (sunucumuz üzerinden iletilir)</td><td>Film afişi görseli</td></tr>
    <tr><td>RevenueCat, Inc.</td><td>ABD</td><td>Kullanıcı kimlik numaranız, satın aldığınız ürün, abonelik durumu ve süresi</td><td>Premium aboneliğin yönetilmesi</td></tr>
    <tr><td>Apple Inc. / Google LLC (uygulama mağazaları)</td><td>ABD</td><td>Satın alma ve abonelik işlemleri. Ödeme kartı bilgileriniz yalnızca mağaza tarafından işlenir, bize iletilmez.</td><td>Ödemenin alınması</td></tr>
  </tbody>
</table>
</div>
"""

RIGHTS_LIST = """
<ul>
  <li>Kişisel verilerinizin işlenip işlenmediğini öğrenme,</li>
  <li>Kişisel verileriniz işlenmişse buna ilişkin bilgi talep etme,</li>
  <li>Kişisel verilerinizin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme,</li>
  <li>Yurt içinde veya yurt dışında kişisel verilerinizin aktarıldığı üçüncü kişileri bilme,</li>
  <li>Kişisel verilerinizin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme ve bu kapsamda yapılan işlemin verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme,</li>
  <li>İşlenmesini gerektiren sebeplerin ortadan kalkması hâlinde kişisel verilerinizin silinmesini, yok edilmesini veya anonim hâle getirilmesini isteme ve bu kapsamda yapılan işlemin verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme,</li>
  <li>İşlenen verilerinizin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle aleyhinize bir sonucun ortaya çıkmasına itiraz etme,</li>
  <li>Kişisel verilerinizin kanuna aykırı olarak işlenmesi sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme.</li>
</ul>
"""

APPLICATION = """
<p>Taleplerinizi, Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ’e uygun olarak {{WRITTEN_ROUTE}}{{EMAIL}} adresine “KVKK Başvuru” konulu e-posta göndererek veya Tebliğ’de belirtilen diğer yöntemlerle iletebilirsiniz. Başvurunuzda kimliğinizi tespit etmemizi sağlayacak bilgilere ve talebinizin konusuna yer vermeniz gerekir.</p>
<p>Başvurunuz, talebin niteliğine göre en kısa sürede ve en geç 30 (otuz) gün içinde ücretsiz olarak sonuçlandırılır. İşlemin ayrıca bir maliyet gerektirmesi hâlinde Kişisel Verileri Koruma Kurulu tarafından belirlenen tarifedeki ücret alınabilir. Talebinizin reddedilmesi hâlinde gerekçesi size yazılı olarak veya elektronik ortamda bildirilir.</p>
"""

CONTACT = """
<div class="box">
  <p><strong>Veri sorumlusu:</strong> {{CONTROLLER}}<br>
  {{ADDRESS_LINE}}
  <strong>E-posta:</strong> {{EMAIL}}</p>
</div>
"""

PAGES = {}

# ─────────────────────────────────────────────────────────────────────────────
PAGES["aydinlatma-metni-uyeler"] = {
    "title": "Üyelere İlişkin Aydınlatma Metni",
    "h1": "Üyelere İlişkin Kişisel Verilerin Korunması Hakkında Aydınlatma Metni",
    "description": "BookAtlas üyelerinin kişisel verilerinin 6698 sayılı Kanun kapsamında nasıl işlendiğine ilişkin aydınlatma metni.",
    "body": """
<p>6698 sayılı Kişisel Verilerin Korunması Kanunu (“Kanun”) kapsamında kişisel verilerinizin güvenliğine önem veriyoruz. Bu metin, BookAtlas mobil uygulamasına (“BookAtlas” veya “Uygulama”) üye olan kullanıcılarımızın kişisel verilerinin, veri sorumlusu sıfatıyla {{CONTROLLER}} tarafından nasıl işlendiğini açıklamak ve aydınlatma yükümlülüğünü yerine getirmek amacıyla hazırlanmıştır.</p>
""" + CONTACT + """
<h2>1. İşlenen kişisel veri kategorileri</h2>
<ul>
  <li><strong>Kimlik bilgileri:</strong> ad ve soyad, kullanıcı adı, doğum tarihi.</li>
  <li><strong>İletişim bilgileri:</strong> e-posta adresi.</li>
  <li><strong>Görsel kayıtlar:</strong> yüklemeniz hâlinde profil fotoğrafı.</li>
  <li><strong>Kullanıcı içeriği ve işlem bilgileri:</strong> okuduğunuz kitaplara ilişkin kayıtlar (kitap adı, yazar, ISBN, ülke, şehir, okuyan kişinin adı, bitirme tarihi ve notlarınız), okuma listeniz, okuma hedefleriniz, okuma istatistikleriniz, profilinize yazdığınız kısa tanıtım, harita kartı paylaşım kayıtlarınız, yapay zekâ asistanına yazdığınız istekler ile size sunulan kitap ve film önerilerinin geçmişi.</li>
  <li><strong>Abonelik bilgileri:</strong> premium üyelik durumu, plan türü, satın alınan ürün, satın almanın yapıldığı mağaza, başlangıç ve bitiş tarihleri. Ödeme kartı bilgileriniz tarafımızca işlenmez; ödemeler App Store veya Google Play üzerinden alınır.</li>
  <li><strong>İşlem güvenliği bilgileri:</strong> IP adresi, oturum ve erişim kayıtları, yapay zekâ ve arama özelliklerinin günlük kullanım sayıları.</li>
  <li><strong>Tercih bilgileri:</strong> dil tercihiniz ve uygulama ayarlarınız. Bu bilgiler oturum bilginizle birlikte cihazınızda yerel olarak saklanır.</li>
</ul>
<div class="box">
  <p>Uygulama konum izni istemez; ülke ve şehir bilgisi kitap kaydı sırasında sizin tarafınızdan elle girilir. Kamera yalnızca kitap barkodunu okumak ve dilerseniz profil fotoğrafı çekmek için, fotoğraf galerisi yalnızca profil fotoğrafı seçmek için kullanılır. Uygulamada reklam ve üçüncü taraf analiz aracı bulunmaz.</p>
  <p>Kitap notları serbest metin alanıdır. Bu alana sağlığınız, inancınız, siyasi görüşünüz gibi özel nitelikli kişisel verilerinizi veya başka kişilere ait kişisel verileri yazmamanızı rica ederiz.</p>
</div>

<h2>2. Kişisel verilerin işlenme amaçları</h2>
<ul>
  <li>Üyelik kaydının oluşturulması, kimliğinizin doğrulanması ve hesabınızın yönetilmesi,</li>
  <li>Kitap kayıtlarınızın saklanması, dünya haritanızın, okuma listenizin, hedeflerinizin ve istatistiklerinizin oluşturulması,</li>
  <li>Kitap arama, ISBN ile kitap bulma ve kapak görseli gösterme hizmetlerinin sunulması,</li>
  <li>Okuma geçmişinize ve isteğinize göre yapay zekâ destekli kitap ve film önerilerinin hazırlanması,</li>
  <li>Premium abonelik ve ücretsiz deneme süreçlerinin yürütülmesi,</li>
  <li>Hizmetin kötüye kullanımının önlenmesi, günlük kullanım sınırlarının uygulanması ve bilgi güvenliğinin sağlanması,</li>
  <li>Talep, öneri ve şikâyetlerinizin yanıtlanması,</li>
  <li>Hataların giderilmesi ve hizmetin geliştirilmesi,</li>
  <li>Mevzuattan doğan yükümlülüklerin yerine getirilmesi ve yetkili kurumlara bilgi verilmesi.</li>
</ul>
<p>Kişisel verileriniz reklam hedeflemesi veya üçüncü taraflara pazarlama amacıyla kullanılmaz ve satılmaz.</p>

<h2>3. Toplama yöntemi ve hukuki sebepler</h2>
<p>Kişisel verileriniz; Uygulama’ya kayıt olurken ve Uygulama’yı kullanırken girdiğiniz bilgiler, Uygulama’daki oturum ve işlem kayıtlarınız ile bize gönderdiğiniz e-postalar aracılığıyla elektronik ortamda toplanır.</p>
<div class="table-scroll">
<table>
  <thead><tr><th>Amaç</th><th>Hukuki sebep</th></tr></thead>
  <tbody>
    <tr><td>Üyelik, kitap kayıtları, harita, okuma listesi, hedefler, istatistikler, kitap arama, yapay zekâ önerileri, premium abonelik</td><td>Bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması (Kanun m. 5/2-c)</td></tr>
    <tr><td>Kötüye kullanımın önlenmesi, bilgi güvenliği, hataların giderilmesi, hizmetin geliştirilmesi</td><td>İlgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla veri sorumlusunun meşru menfaati (Kanun m. 5/2-f)</td></tr>
    <tr><td>Yetkili kurumlara bilgi verilmesi, yasal saklama yükümlülükleri</td><td>Kanunlarda açıkça öngörülmesi ve hukuki yükümlülüğün yerine getirilmesi (Kanun m. 5/2-a ve 5/2-ç)</td></tr>
    <tr><td>Talep ve şikâyetlerin yanıtlanması, hakların korunması</td><td>Bir hakkın tesisi, kullanılması veya korunması (Kanun m. 5/2-e)</td></tr>
    <tr><td>Kişisel verilerin yurt dışındaki hizmet sağlayıcılara aktarılması</td><td>Kanun m. 9 kapsamında açık rızanız (bkz. <a href="acik-riza-beyani.html">Açık Rıza Beyanı</a>)</td></tr>
  </tbody>
</table>
</div>

<h2>4. Kişisel verilerin aktarılması</h2>
<p>Kişisel verileriniz, Kanun’un 8. ve 9. maddelerine uygun olarak ve yalnızca hizmetin sunulması için gerekli olduğu ölçüde aşağıdaki hizmet sağlayıcılara aktarılır. Bu sağlayıcıların sunucuları yurt dışında bulunmaktadır.</p>
""" + RECIPIENTS_TABLE + """
<p>Kişisel verileriniz ayrıca, hukuken yetkili kamu kurum ve kuruluşlarının usulüne uygun talepleri hâlinde bu kurumlarla paylaşılabilir.</p>

<h2>5. Saklama süresi</h2>
<p>Kişisel verileriniz üyeliğiniz devam ettiği sürece veya silme talebinize kadar saklanır. Erişim ve işlem kayıtları (loglar) en fazla 12 ay saklanır. Hesabınızı sildiğinizde hesap bilgileriniz, kitap kayıtlarınız, okuma listeniz, hedefleriniz, öneri geçmişiniz ve profil fotoğrafınız silinir. Mevzuat gereği saklanması zorunlu olan veya bir uyuşmazlık hâlinde ispat için gerekli olan kayıtlar, ilgili yasal süre boyunca saklanır ve sürenin sonunda silinir, yok edilir veya anonim hâle getirilir.</p>
<p>Hesabınızı nasıl sileceğiniz <a href="hesap-silme.html">Hesap Silme</a> sayfasında açıklanmıştır.</p>

<h2>6. Veri güvenliği tedbirleri</h2>
<ul>
  <li>Verilerin TLS/SSL şifrelemesiyle iletilmesi,</li>
  <li>Supabase Row Level Security (RLS) ile veri erişim denetimi,</li>
  <li>Şifrelerin özetlenerek (hash) saklanması,</li>
  <li>Üçüncü taraf hizmetlere ait anahtarların uygulamada değil sunucuda tutulması,</li>
  <li>Düzenli güvenlik güncellemeleri.</li>
</ul>

<h2>7. Yapay zekâ destekli öneriler</h2>
<p>Kitap ve film önerileri bir yapay zekâ modeli tarafından üretilir ve hata içerebilir. Bu öneriler hakkınızda hukuki sonuç doğuran veya sizi benzer biçimde önemli ölçüde etkileyen bir karar niteliği taşımaz. Önerilere ilişkin itiraz ve geri bildirimlerinizi {{EMAIL}} adresine iletebilirsiniz.</p>

<h2>8. Kanun’un 11. maddesi kapsamındaki haklarınız</h2>
<p>Veri sorumlusuna başvurarak:</p>
""" + RIGHTS_LIST + """
<p>haklarına sahipsiniz.</p>
""" + APPLICATION + """
<h2>9. Değişiklikler</h2>
<p>Bu metin, işleme faaliyetlerindeki veya mevzuattaki değişikliklere göre güncellenebilir. Güncel metin bu sayfada yayımlanır; önemli değişiklikler Uygulama üzerinden ayrıca duyurulur.</p>
""",
}

# ─────────────────────────────────────────────────────────────────────────────
PAGES["aydinlatma-metni-misafirler"] = {
    "title": "Misafirlere İlişkin Aydınlatma Metni",
    "h1": "Misafir Kullanıcılara ve Ziyaretçilere İlişkin Kişisel Verilerin Korunması Hakkında Aydınlatma Metni",
    "description": "BookAtlas internet sitesini ziyaret eden ve üye olmadan bizimle iletişime geçen kişilerin kişisel verilerine ilişkin aydınlatma metni.",
    "body": """
<p>6698 sayılı Kişisel Verilerin Korunması Kanunu (“Kanun”) kapsamında bu metin; BookAtlas internet sitesini ziyaret eden, Uygulama’yı indirip henüz üye olmayan veya üye olmadan bizimle iletişime geçen kişilerin (“misafir”) kişisel verilerinin, veri sorumlusu sıfatıyla {{CONTROLLER}} tarafından nasıl işlendiğini açıklamak amacıyla hazırlanmıştır.</p>
""" + CONTACT + """
<div class="box">
  <p>BookAtlas’ın kitap kaydı, harita, okuma listesi ve öneri özellikleri yalnızca üyelikle kullanılabilir. Üye olduğunuzda kişisel verileriniz <a href="aydinlatma-metni-uyeler.html">Üyelere İlişkin Aydınlatma Metni</a> kapsamında işlenir.</p>
</div>

<h2>1. İşlenen kişisel veri kategorileri</h2>
<ul>
  <li><strong>İşlem güvenliği bilgileri:</strong> internet sitesini ziyaret ettiğinizde barındırma hizmeti sağlayıcısının sunucularında tutulan IP adresi, ziyaret zamanı ve tarayıcı bilgisi gibi erişim kayıtları.</li>
  <li><strong>İletişim bilgileri ve talep içeriği:</strong> bize e-posta göndermeniz hâlinde e-posta adresiniz, belirtmişseniz adınız ve mesajınızın içeriği.</li>
</ul>
<p>İnternet sitemizde çerez, reklam veya analiz aracı kullanılmaz; ziyaretiniz sırasında cihazınıza herhangi bir veri kaydedilmez. Üye olmayan kişilerden Uygulama aracılığıyla kimlik, konum veya kullanım verisi toplanmaz.</p>

<h2>2. Kişisel verilerin işlenme amaçları</h2>
<ul>
  <li>İnternet sitesinin yayımlanması ve güvenliğinin sağlanması,</li>
  <li>Talep, öneri ve şikâyetlerinizin yanıtlanması,</li>
  <li>Hukuki yükümlülüklerin yerine getirilmesi ve haklarımızın korunması.</li>
</ul>

<h2>3. Toplama yöntemi ve hukuki sebepler</h2>
<p>Kişisel verileriniz, internet sitesini ziyaret etmeniz sırasında otomatik olarak ve bize gönderdiğiniz e-postalar aracılığıyla elektronik ortamda toplanır. Bu veriler; veri sorumlusunun meşru menfaati (Kanun m. 5/2-f), bir hakkın tesisi, kullanılması veya korunması (Kanun m. 5/2-e) ve hukuki yükümlülüğün yerine getirilmesi (Kanun m. 5/2-ç) hukuki sebeplerine dayanılarak işlenir.</p>

<h2>4. Kişisel verilerin aktarılması</h2>
<p>İnternet sitemiz {{HOSTING}} altyapısında barındırılmaktadır; siteyi ziyaret ettiğinizde erişim kayıtlarınız bu hizmet sağlayıcının yurt dışındaki sunucularında işlenir. E-posta yazışmaları, e-posta hizmeti sağlayıcımızın sunucularında saklanır. Kişisel verileriniz ayrıca, hukuken yetkili kamu kurum ve kuruluşlarının usulüne uygun talepleri hâlinde bu kurumlarla paylaşılabilir.</p>

<h2>5. Saklama süresi</h2>
<p>E-posta yazışmaları, talebinizin sonuçlandırılması ve olası bir uyuşmazlıkta ispat için gereken süre boyunca saklanır; ardından silinir. Erişim kayıtları barındırma hizmeti sağlayıcısının kendi saklama süresine tabidir.</p>

<h2>6. Kanun’un 11. maddesi kapsamındaki haklarınız</h2>
<p>Veri sorumlusuna başvurarak:</p>
""" + RIGHTS_LIST + """
<p>haklarına sahipsiniz.</p>
""" + APPLICATION,
}

# ─────────────────────────────────────────────────────────────────────────────
PAGES["acik-riza-beyani"] = {
    "title": "Açık Rıza Beyanı",
    "h1": "Açık Rıza Beyanı",
    "description": "BookAtlas üyelerinin kişisel verilerinin yurt dışına aktarılmasına ilişkin açık rıza beyanı.",
    "body": """
<p><a href="aydinlatma-metni-uyeler.html">Üyelere İlişkin Aydınlatma Metni</a>’ni okudum ve kişisel verilerimin işlenmesi hakkında bilgilendirildim.</p>

<div class="box">
  <p>6698 sayılı Kişisel Verilerin Korunması Kanunu’nun 9. maddesi kapsamında; BookAtlas’a kaydettiğim hesap ve profil bilgilerimin, kitap kayıtlarımın, okuma listemin, okuma hedeflerimin, öneri geçmişimin ve abonelik bilgilerimin, Aydınlatma Metni’nde belirtilen amaçlarla sınırlı olarak, veri sorumlusu {{CONTROLLER}} tarafından aşağıda sayılan ve sunucuları yurt dışında bulunan hizmet sağlayıcılara aktarılmasına açık rıza veriyorum.</p>
</div>

<h2>Aktarım yapılan hizmet sağlayıcılar</h2>
""" + RECIPIENTS_TABLE + """
<h2>Bilgilendirildiğim hususlar</h2>
<ul>
  <li>Bu rızayı vermek zorunda olmadığımı; ancak BookAtlas’ın altyapısı yurt dışındaki hizmet sağlayıcılar üzerinde çalıştığı için rıza vermemem hâlinde üyelik oluşturulamayacağını,</li>
  <li>Verilerimin aktarıldığı ülkelerde, Türkiye’dekine eşdeğer bir kişisel veri koruması bulunmayabileceğini,</li>
  <li>Açık rızamı dilediğim zaman, herhangi bir gerekçe göstermeksizin {{EMAIL}} adresine yazarak veya hesabımı silerek geri alabileceğimi; geri almanın ileriye yönelik sonuç doğuracağını ve bu durumda üyeliğimin sona ereceğini,</li>
  <li>Kanun’un 11. maddesi kapsamındaki haklarımı Aydınlatma Metni’nde açıklanan şekilde kullanabileceğimi</li>
</ul>
<p>biliyorum.</p>
""",
}

# ─────────────────────────────────────────────────────────────────────────────
PAGES["kullanici-sozlesmesi"] = {
    "title": "Kullanıcı Sözleşmesi",
    "h1": "Kullanıcı Sözleşmesi",
    "description": "BookAtlas mobil uygulamasının kullanım koşullarını düzenleyen kullanıcı sözleşmesi.",
    "body": """
<p>BookAtlas mobil uygulamasına üye olmanız ve uygulamayı kullanmanız, bu Kullanıcı Sözleşmesi’ni (“Sözleşme”) okuduğunuz ve kabul ettiğiniz anlamına gelir. Sözleşme’yi kabul etmiyorsanız lütfen uygulamayı kullanmayın.</p>

<h2>1. Taraflar</h2>
<p>Bu Sözleşme; BookAtlas mobil uygulamasını (“BookAtlas” veya “Uygulama”) işleten {{CONTROLLER}} (“BookAtlas”) ile Uygulama’ya üye olarak sunulan hizmetlerden yararlanan, ticari ve mesleki amaçla hareket etmeyen gerçek kişi (“Kullanıcı”) arasında kurulmuştur.</p>

<h2>2. Sözleşmenin konusu ve hizmetin kapsamı</h2>
<p>BookAtlas; Kullanıcı’nın okuduğu kitapları ülke ve şehir bilgisiyle kaydetmesine, bu kayıtları dünya haritası üzerinde görmesine, okuma listesi ve okuma hedefi oluşturmasına, okuma istatistiklerini izlemesine ve yapay zekâ destekli kitap ve film önerileri almasına imkân veren bir mobil uygulamadır. Bu Sözleşme, Uygulama’dan yararlanma koşullarını ve tarafların hak ve yükümlülüklerini düzenler.</p>

<h2>3. Üyelik ve hesap güvenliği</h2>
<ul>
  <li>Uygulama’yı kullanmak için geçerli bir e-posta adresi ve şifre ile üyelik oluşturulması gerekir.</li>
  <li>Kullanıcı, 13 yaşını doldurmuş olduğunu beyan eder. 18 yaşından küçük Kullanıcılar, Uygulama’yı ancak velilerinin veya yasal temsilcilerinin onayıyla kullanabilir.</li>
  <li>Kullanıcı, kayıt sırasında verdiği bilgilerin doğru ve kendisine ait olduğunu kabul eder.</li>
  <li>Şifrenin belirlenmesi ve gizli tutulması Kullanıcı’nın sorumluluğundadır. Kullanıcı, hesabının izinsiz kullanıldığını fark ettiğinde durumu gecikmeksizin BookAtlas’a bildirir.</li>
  <li>Her Kullanıcı yalnızca bir hesap oluşturabilir ve ücretsiz deneme hakkından bir kez yararlanabilir.</li>
</ul>

<h2>4. Kullanım kuralları</h2>
<p>Kullanıcı, Uygulama’yı kullanırken:</p>
<ul>
  <li>Uygulama’yı yalnızca kişisel amaçla ve hukuka uygun biçimde kullanmayı,</li>
  <li>Hukuka veya genel ahlaka aykırı, hakaret veya tehdit içeren, üçüncü kişilerin kişilik haklarını ya da fikri mülkiyet haklarını ihlal eden kullanıcı adı, profil fotoğrafı veya içerik kullanmamayı,</li>
  <li>Başka kişilere ait kişisel verileri izinsiz olarak kaydetmemeyi ve yaymamayı,</li>
  <li>Uygulama’nın ve altyapısının güvenliğini tehlikeye atacak, işleyişini bozacak veya diğer kullanıcıların yararlanmasını engelleyecek işlemlerde bulunmamayı,</li>
  <li>Uygulama’ya otomatik araçlarla erişmemeyi, günlük kullanım sınırlarını dolanmaya çalışmamayı, Uygulama’yı kaynak koduna dönüştürmemeyi veya kopyalamamayı,</li>
  <li>Uygulama’yı ticari amaçla veya reklam amacıyla kullanmamayı</li>
</ul>
<p>kabul eder.</p>

<h2>5. Kullanıcı içeriği</h2>
<p>Kullanıcı’nın Uygulama’ya girdiği kitap kayıtları, notlar ve diğer içerikler Kullanıcı’ya aittir. Kullanıcı, bu içeriğin yalnızca hizmetin kendisine sunulması amacıyla saklanmasına ve işlenmesine izin verir. Kullanıcı, kayıtlarını Uygulama içinden dışa aktarabilir ve hesabını silerek kaldırabilir.</p>
<p>Harita kartı gibi paylaşım özellikleriyle oluşturulan görseller, Kullanıcı’nın kendi tercihiyle ve kendi seçtiği mecralarda paylaşılır; bu paylaşımların sorumluluğu Kullanıcı’ya aittir.</p>

<h2>6. Veri güvenliği tedbirleri</h2>
<ul>
  <li>Verilerin TLS/SSL şifrelemesiyle iletilmesi,</li>
  <li>Supabase Row Level Security (RLS) ile veri erişim denetimi,</li>
  <li>Şifrelerin özetlenerek (hash) saklanması,</li>
  <li>Üçüncü taraf hizmetlere ait anahtarların uygulamada değil sunucuda tutulması,</li>
  <li>Düzenli güvenlik güncellemeleri.</li>
</ul>

<h2>7. Yapay zekâ destekli öneriler</h2>
<ul>
  <li>Kitap ve film önerileri bir yapay zekâ modeli tarafından üretilir, bilgilendirme amaçlıdır ve hata içerebilir. Önerilen eserin adı, yazarı veya içeriğine ilişkin bilgilerin doğruluğu garanti edilmez.</li>
  <li>Öneri özellikleri günlük kullanım sınırına tabidir. Sınırlar ücretsiz ve premium üyelik için farklıdır ve Uygulama içinde gösterilir.</li>
  <li>BookAtlas, hizmetin sürdürülebilirliği için bu sınırları ileriye dönük olarak değiştirebilir; premium üyeler bakımından aleyhe değişiklikler mevcut abonelik döneminin sonundan itibaren uygulanır.</li>
</ul>

<h2>7. Premium abonelik, ücretsiz deneme ve ödeme</h2>
<ul>
  <li>Uygulama’nın temel özellikleri ücretsizdir. Premium abonelik, Uygulama içinde belirtilen ek özellikleri ve daha yüksek kullanım sınırlarını sağlar.</li>
  <li>Abonelik ücreti ve süresi, satın alma sırasında App Store veya Google Play tarafından gösterilir. Ödemeler bu mağazalar aracılığıyla alınır; BookAtlas ödeme kartı bilgilerine erişmez.</li>
  <li>Abonelikler, mevcut dönemin bitiminden en az 24 saat önce iptal edilmediği sürece aynı süre için otomatik olarak yenilenir. Kullanıcı, aboneliğini mağaza hesap ayarlarından dilediği zaman iptal edebilir; iptal hâlinde erişim, ödenen dönemin sonuna kadar devam eder.</li>
  <li>İade talepleri, satın almanın yapıldığı mağazanın iade kurallarına göre ilgili mağaza tarafından değerlendirilir.</li>
  <li>Ücretsiz deneme ve kampanyalar, Uygulama içinde duyurulan koşullara tabidir. Ücretsiz deneme her Kullanıcı için bir defaya mahsustur; deneme süresi sonunda erişim kendiliğinden sona erer ve herhangi bir ücret tahsil edilmez. BookAtlas, kampanya koşullarını ileriye dönük olarak değiştirebilir veya kampanyayı sona erdirebilir.</li>
  <li>Hesabın silinmesi, mağaza üzerindeki aboneliği kendiliğinden iptal etmez; Kullanıcı’nın aboneliğini mağaza hesap ayarlarından ayrıca iptal etmesi gerekir.</li>
</ul>
<p>Kullanıcı’nın tüketici mevzuatından doğan hakları saklıdır.</p>

<h2>8. Üçüncü taraf içerik ve hizmetler</h2>
<p>Kitap bilgileri ve kapak görselleri Google Books ve Open Library gibi üçüncü taraf kaynaklardan, film afişleri OMDb’den alınır. BookAtlas, bu kaynaklardan gelen bilgilerin eksiksiz veya güncel olduğunu garanti etmez. Uygulama içinden açılan üçüncü taraf internet siteleri kendi koşullarına tabidir.</p>

<h2>9. Fikri mülkiyet</h2>
<p>Uygulama’nın yazılımı, tasarımı, adı, logosu ve Uygulama’ya ait diğer tüm unsurlar üzerindeki fikri mülkiyet hakları BookAtlas’a aittir. Bu unsurlar, BookAtlas’ın yazılı izni olmaksızın kopyalanamaz, çoğaltılamaz, dağıtılamaz ve bunlardan türev çalışmalar yapılamaz. Kitap adları, kapak görselleri ve film afişleri üzerindeki haklar ilgili hak sahiplerine aittir.</p>

<h2>10. Hizmette değişiklik, askıya alma ve sona erdirme</h2>
<ul>
  <li>BookAtlas, Uygulama’ya yeni özellikler ekleyebilir, mevcut özellikleri değiştirebilir veya kaldırabilir; bakım, güncelleme ve güvenlik nedenleriyle hizmeti geçici olarak durdurabilir.</li>
  <li>BookAtlas, bu Sözleşme’ye veya hukuka aykırı kullanımın ya da hesabın yetkisiz kişilerce kullanıldığının tespiti hâlinde ilgili hesabı geçici olarak askıya alabilir veya üyeliği sona erdirebilir.</li>
</ul>

<h2>11. Sorumluluk</h2>
<p>BookAtlas, Uygulama’nın kesintisiz ve hatasız çalışması için makul özeni gösterir; ancak hizmetin her zaman kesintisiz ve hatasız olacağını taahhüt etmez. BookAtlas; Kullanıcı’nın bu Sözleşme’ye aykırı kullanımından, üçüncü taraf hizmet sağlayıcılardan kaynaklanan kesintilerden ve yapay zekâ önerilerine dayanılarak verilen kararlardan doğan zararlardan, kastı veya ağır kusuru bulunmadıkça sorumlu değildir. Bu madde, Kullanıcı’nın emredici hukuk kurallarından doğan haklarını sınırlamaz.</p>

<h2>12. Kişisel verilerin korunması</h2>
<p>Kullanıcı’nın kişisel verileri, <a href="aydinlatma-metni-uyeler.html">Üyelere İlişkin Aydınlatma Metni</a>’nde açıklanan koşullarda işlenir, saklanır ve imha edilir.</p>

<h2>13. Mücbir sebep</h2>
<p>Tarafların öngöremediği ve önleyemediği; doğal afet, salgın hastalık, savaş, grev, yasal düzenlemeler, altyapı ve iletişim kesintileri gibi olaylar nedeniyle yükümlülüklerin yerine getirilememesi hâlinde taraflar sorumlu tutulamaz. Yükümlülükler, mücbir sebep ortadan kalkana kadar askıda kalır.</p>

<h2>14. Sözleşme değişiklikleri</h2>
<p>BookAtlas, teknik zorunluluklar ve mevzuata uyum amacıyla bu Sözleşme’yi güncelleyebilir. Güncel metin bu sayfada yayımlanır; Kullanıcı’nın haklarını etkileyen önemli değişiklikler Uygulama üzerinden önceden duyurulur. Değişikliği kabul etmeyen Kullanıcı, hesabını silerek Sözleşme’yi sona erdirebilir.</p>

<h2>15. Yürürlük ve fesih</h2>
<p>Bu Sözleşme, Kullanıcı’nın üye olmasıyla yürürlüğe girer ve üyelik devam ettiği sürece yürürlükte kalır. Kullanıcı, Uygulama içindeki “Hesabı Sil” seçeneğini kullanarak veya {{EMAIL}} adresine yazarak üyeliğini dilediği zaman sona erdirebilir. Ayrıntılar <a href="hesap-silme.html">Hesap Silme</a> sayfasındadır.</p>

<h2>16. Uygulanacak hukuk ve uyuşmazlıkların çözümü</h2>
<p>Bu Sözleşme Türkiye Cumhuriyeti hukukuna tabidir. Sözleşme’den doğan uyuşmazlıklarda {{COURT}} yetkilidir. Kullanıcı’nın 6502 sayılı Tüketicinin Korunması Hakkında Kanun uyarınca Tüketici Hakem Heyetleri’ne ve Tüketici Mahkemeleri’ne başvurma hakkı ile yerleşik olduğu ülkenin emredici tüketici kurallarından doğan hakları saklıdır.</p>

<h2>17. İletişim</h2>
""" + CONTACT,
}

# ─────────────────────────────────────────────────────────────────────────────
PAGES["hesap-silme"] = {
    "title": "Hesap Silme",
    "h1": "Hesap Silme",
    "description": "BookAtlas hesabınızı ve verilerinizi nasıl sileceğiniz.",
    "body": """
<p>BookAtlas hesabınızı ve hesabınıza bağlı verileri kalıcı olarak silmek için aşağıdaki yöntemlerden birini kullanabilirsiniz.</p>

<h2>Yöntem 1: Uygulama içinden</h2>
<ol>
  <li>BookAtlas uygulamasını açın.</li>
  <li>Profil sayfasına gidin.</li>
  <li>“Hesabı Sil” seçeneğine dokunun.</li>
  <li>Şifrenizi girerek silme işlemini onaylayın.</li>
</ol>

<h2>Yöntem 2: E-posta ile</h2>
<p>Uygulamaya erişemiyorsanız {{EMAIL}} adresine, hesabınıza kayıtlı e-posta adresinden “BookAtlas Hesap Silme Talebi” konulu bir e-posta gönderin; kayıtlı e-posta adresinizi ve adınızı soyadınızı belirtin. Talepler, kimlik doğrulamasının ardından en geç 7 (yedi) iş günü içinde işleme alınır.</p>

<h2>Silinen veriler</h2>
<p>Hesabınız silindiğinde aşağıdaki veriler kalıcı olarak kaldırılır ve geri getirilemez:</p>
<ul>
  <li>Hesap ve profil bilgileriniz (e-posta, ad, kullanıcı adı, doğum tarihi, profil fotoğrafı),</li>
  <li>Tüm kitap kayıtlarınız ve dünya haritanız,</li>
  <li>Okuma listeniz ve okuma hedefleriniz,</li>
  <li>Yapay zekâ kitap ve film öneri geçmişiniz,</li>
  <li>İstatistik ve paylaşım kayıtlarınız,</li>
  <li>Premium üyelik kaydınız.</li>
</ul>
<p>Silme işlemi geri alınamaz. Verilerin yedekleme sistemlerinden tamamen kaldırılması en fazla 30 gün sürebilir. Mevzuat gereği saklanması zorunlu olan kayıtlar, ilgili yasal süre boyunca saklanmaya devam edebilir. Aynı e-posta adresiyle yeniden hesap oluşturabilirsiniz; ancak eski verilerinize erişemezsiniz.</p>

<div class="box">
  <p><strong>Aktif aboneliğiniz varsa:</strong> Hesabınızı silmek mağaza üzerindeki aboneliğinizi iptal etmez. Ücretlendirilmeye devam etmemek için hesabınızı silmeden önce aboneliğinizi App Store veya Google Play hesap ayarlarınızdan iptal edin.</p>
  <p><strong>Kayıtlarınızı saklamak isterseniz:</strong> Silmeden önce İstatistik sayfasındaki dışa aktarma düğmesiyle kitap kayıtlarınızı CSV dosyası olarak indirebilirsiniz.</p>
</div>
""",
}

# Sayfaların menüdeki sırası ve kısa adları.
NAV = [
    ("kullanici-sozlesmesi", "Kullanıcı Sözleşmesi"),
    ("aydinlatma-metni-uyeler", "Aydınlatma Metni (Üyeler)"),
    ("aydinlatma-metni-misafirler", "Aydınlatma Metni (Misafirler)"),
    ("acik-riza-beyani", "Açık Rıza Beyanı"),
    ("hesap-silme", "Hesap Silme"),
]
