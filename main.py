from stegano import lsb, exifHeader


#   Для png
input_png = ""  # Путь до изначального изображения
secret_text = ""    # Текст, который будет использоваться
secret_png = "" # Путь и имя измененного файла

secret = lsb.hide(input_png, secret_text)
secret.save(secret_png)
result = lsb.reveal(secret_png)
print(result)


#   Для jpg
input_jpg = ""  # Путь до изначального изображения
secret_text = ""    # Текст, который будет использоваться
secret_png = "" # Путь и имя измененного файла

secret = exifHeader.hide(input_jpg, secret_png, secret_text)
result = exifHeader.reveal(secret_png)
result = result.decode()
print(result)