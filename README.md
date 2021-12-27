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
<br>-----PostgreSql'de ToplantiDb adında veritabanı oluşturulur.</br>
<br>-----Terminalden python manage.py migrate            komutu ile migration işlemi kpntrol edilir.</br>
<br>-----python manage.py makemigrations katilimci       komutu ile katilimci dosyasına migration oluşturulur.(zaten var)</br>
<br>-----python manage.py sqlmigrate katilimci 0001      komutu ile model oluşturulur.</br>
<br>-----python manage.py migrate                        komutu çalıştırılır</br>
<br>-----python manage.py runserver                      komutu ile proje çalıştırılır</br>


<br>Path bilgileri

<br>http://127.0.0.1:8000/toplanti/  yolundan ulaşılabilir.


*Tarih doğru format girildiği sürece çalışıyor.
