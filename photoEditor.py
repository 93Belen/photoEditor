from PIL import Image, ImageEnhance, ImageOps, ImageDraw
import os
import random

path = '../../imgs_to_edit'
pathOut = '../../edited_imgs'

##img = Image.open(f"./imgs/flower.jpg")

## Vibrance, Contast, Brightness, Sharpness
def modify_values(image, level_vibrance, level_contrast, level_brightness, level_sharpness):
    vibrance = ImageEnhance.Color(img)
    enhanced = vibrance.enhance(level_vibrance)

    contrast = ImageEnhance.Contrast(enhanced)
    enhanced = contrast.enhance(level_contrast)

    brightness = ImageEnhance.Brightness(enhanced)
    enhanced = brightness.enhance(level_brightness)

    sharpness = ImageEnhance.Sharpness(enhanced)
    enhanced = sharpness.enhance(level_sharpness)

    ##enhanced.show()
    return enhanced


## Change colors of picture to only two colors
def change_colors(image, color_one, color_two):
    black_white_img = image.convert("L")
    colorized = ImageOps.colorize(image = black_white_img, black = color_one, white = color_two)
    #colorized.show()
    return colorized



## Draw shapes
# One triangle
def add_triangle1(image, color):
    w = image.size[0]
    h = image.size[1]
    draw = ImageDraw.Draw(image)
    draw.polygon(((w // 2, 0), (w, h), (0, h)), width = 5, outline = color)
    #image.show()
    return image

# Two triangles
def add_triangle2(image, color):
    w = image.size[0]
    h = image.size[1]
    draw = ImageDraw.Draw(image)
    draw.polygon(((w // 2, 0), (w, h), (0, h)), width = 5, outline = color)
    draw.polygon(((0, 0), (w, 0), (w // 2, h)), width = 5, outline = color)
    #image.show()
    return image

# Two triangles B

def add_triangle2_b(image, color):
    w = image.size[0]
    h = image.size[1]
    draw = ImageDraw.Draw(image)
    draw.polygon(((0, 0), (w, 0), (0, h)), width = 5, outline = color)
    draw.polygon(((w, 0), (w, h), (0, h)), width = 5, outline = color)
    #image.show()
    return image

# Three triangles
def add_triangle3(image, color):
    w = image.size[0]
    h = image.size[1]
    draw = ImageDraw.Draw(image)
    draw.polygon(((w // 2, 0), (w, h), (0, h)), width = 5, outline = color)
    draw.polygon(((w // 2, h // 5), (w, h), (0, h)), width = 5, outline = color)
    draw.polygon(((w // 2, h // 3), (w, h), (0, h)), width = 5, outline = color)
    #image.show()
    return image

# Four triangles
def add_triangle4(image, color):
    w = image.size[0]
    h = image.size[1]
    draw = ImageDraw.Draw(image)
    draw.polygon(((0, 0), (w, 0), (w // 2, h // 2)), width = 5, outline = color)
    draw.polygon(((0, 0), (w // 2, h // 2), (0, h)), width = 5, outline = color)
    draw.polygon(((0, h), (w // 2, h // 2), (w, h)), width = 5, outline = color)
    draw.polygon(((w // 2, h // 2), (w, h), (0, h)), width = 5, outline = color)

    #image.show()
    return image

# Two squares
def add_squares2(image, color):
    w = image.size[0]
    h = image.size[1]

    draw = ImageDraw.Draw(image)
    draw.rectangle((w // 10, h // 10, w // 1.5, h // 1.2), width = 5, outline = color)
    draw.rectangle((w // 5, h // 5, w // 1.2, h // 1.1), width = 5, outline = color)
    #image.show()
    return image

# Four circles
def add_circles4(image, color):
    w = image.size[0]
    h = image.size[1]

    draw = ImageDraw.Draw(image)
    draw.ellipse((w // 12, h // 12, w // 2, h // 1.7), width = 5, outline = color)
    draw.ellipse((w // 10, h // 10, w // 1.7, h // 1.5), width = 5, outline = color)
    draw.ellipse((w // 5, h // 5, w // 1.5, h // 1.2), width = 5, outline = color)
    draw.ellipse((w // 2, h // 2, w // 1.2, h // 1.03), width = 5, outline = color)
    #image.show()
    return image

def all_shapes(image, color):
    w = image.size[0]
    h = image.size[1]

    draw = ImageDraw.Draw(image)
    draw.rectangle((w // 10, h // 10, w // 1.1, h // 1.1), width = 5, outline = color)
    draw.polygon(((w // 2, 0), (w, h), (0, h)), width = 5, outline = color)
    draw.polygon(((0, 0), (w, 0), (w // 2, h)), width = 5, outline = color)

    #image.show()
    return image

## border
def add_border(image, color):
    with_border = ImageOps.expand(image = image, border = 200, fill = color)
    ##with_border.show()
    return with_border

## Vibrance, Contast, Brightness, Sharpness
## modify_values()

## Change colors to only 2 colors
##change_colors()

## Add shapes

## CUSTOM FILTERS
def edit(image):
    random_vibrance = random.randint(1, 5)
    random_contrast = random.randint(1, 5)
    random_brightness = random.randint(1, 5)
    random_sharpness = random.randint(1, 5)

    image_edited = modify_values(image, random_vibrance, random_contrast, random_brightness, random_sharpness)
    
    ## Choose filter randomly
    yes_no = random.randint(0,1)
    list_of_colors = ['pink', 'purple', 'blue', 'red', 'yellow', 'green']

    if(yes_no == 0):
        color_one = list_of_colors[random.randint(0,5)]
        color_two = list_of_colors[random.randint(0,5)]
        image_edited = change_colors(image_edited, color_one, color_two)
    
    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_border(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_triangle1(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_triangle2(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_triangle2_b(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_triangle3(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_triangle4(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_squares2(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = add_circles4(image_edited, color)

    yes_no = random.randint(0,1)
    if(yes_no == 0):
        color = list_of_colors[random.randint(0,5)]
        image_edited = all_shapes(image_edited, color)


    image_edited = ImageOps.contain(image = image_edited, size = (600,600))
    ##image_edited.show()

    return image_edited


for filename in os.listdir(path):
    if filename == '.DS_Store':
        continue
    img = Image.open(f"{path}/{filename}")
    edited = edit(img)
    clean_name = os.path.splitext(filename)[0]
    edited_rgb = edited.convert('RGB')
    edited_rgb.show()
    edited_rgb.save(f"{pathOut}/{clean_name}_edited.jpg")


