# mech_toplanti

..\mech_toplanti\mech_toplanti\settings.py dizininde parola bilgisi var.

Database bilgileri:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ToplantiDB',
        'USER':'postgres',
        'PASSWORD':'123',
        'HOST':'localhost'
    }
    Yapılması gerekenler
-----Üst koddaki Parola yerel pgadmin şifresi ayarlanır.Benim 123
-----PostgreSql'de ToplantiDb adında veritabanı oluşturulur.
-----Terminalden python manage.py migrate            komutu ile migration işlemi kpntrol edilir.
-----python manage.py makemigrations katilimci       komutu ile katilimci dosyasına migration oluşturulur.(zaten var)
-----python manage.py sqlmigrate katilimci 0001      komutu ile model oluşturulur.
-----python manage.py migrate                        komutu çalıştırılır
-----python manage.py runserver                      komutu ile proje çalıştırılır


Path bilgileri

http://127.0.0.1:8000/toplanti/  yolundan ulaşılabilir.



Tarih doğru format girildiği sürece çalışıyor.
