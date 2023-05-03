import colorgram
# this file is used to extract colors of a image, using module colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    rgb_colors.append(rgb_color)

print(rgb_colors)
