from PIL import Image, ImageFilter, ImageEnhance


# 1. Открытие и сохранение изображений
def open_and_save_image(input_path, output_path):
    img = Image.open(input_path)
    img.save(output_path)


# 2. Изменение размера изображения
def resize_image(input_path, output_path, size):
    img = Image.open(input_path)
    img = img.resize(size)  # изменение размера
    img.save(output_path)


# 3. Применение фильтров
def apply_filter(input_path, output_path):
    img = Image.open(input_path)
    filtered_img = img.filter(ImageFilter.GaussianBlur(5))  # применение размытия
    filtered_img.save(output_path)


def process_image(input_path, output_path):
    # Открытие изображения
    img = Image.open(input_path)

    # Изменение размера изображения
    img = img.resize((200, 200))

    # Применение эффекта увеличения яркости
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)  # Увеличение яркости на 50%

    # Сохранение в новый формат
    img.save(output_path, format='PNG')


input_jpg = 'Букет из полевых цветов № 1.jpg'
output_jpg = 'Букет из полевых цветов № 11.jpg'
resized_jpg = 'Букет из полевых цветов 800x600.jpg'
blurred_jpg = 'Букет из полевых цветов blurred.jpg'
output_png = 'Букет из полевых цветов № 123.png'

# Пример вызова функций
open_and_save_image(input_jpg, output_jpg)
resize_image(input_jpg, resized_jpg, (800, 600))
apply_filter(input_jpg, blurred_jpg)
process_image(input_jpg, output_png)
