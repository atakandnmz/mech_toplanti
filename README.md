# mech_toplanti

..\mech_toplanti\mech_toplanti\settings.py dizininde parola bilgisi var.

Database bilgileri:
<br>DATABASES = {
 <br>   'default': {
<br>        'ENGINE': 'django.db.backends.postgresql',
 <br>       'NAME': 'ToplantiDB',
<br>        'USER':'postgres',
<br>        'PASSWORD':'123',
<br>        'HOST':'localhost'
    }</br>
    
--Yapılması gerekenler:::

<br>-----Üst koddaki Parola yerel pgadmin şifresi ayarlanır.Benim 123</br>
<br>-----PostgreSql'de <b>ToplantiDb</b> adında veritabanı oluşturulur.</br>
<br>-----Terminalden <b>python manage.py migrate</b>            komutu ile migration işlemi kontrol edilir.</br>
<br>-----<b>python manage.py makemigrations katilimci </b>      komutu ile katilimci dosyasına migration oluşturulur.(zaten var)</br>
<br>-----<b>python manage.py sqlmigrate katilimci 0001  </b>    komutu ile model oluşturulur.</br>
<br>-----<b>python manage.py migrate </b>                     komutu çalıştırılır</br>
<br>-----<b>python manage.py runserver    </b>                  komutu ile proje çalıştırılır</br>


<br>Path bilgileri

<br>http://127.0.0.1:8000/toplanti/  yolundan ulaşılabilir.
 

*Tarih doğru format girildiği sürece çalışıyor.

Django ile yapılmıştır...
