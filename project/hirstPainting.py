# Part 1
import colorgram

rgb_colors = []
colors = colorgram.extract('project/hirstImage.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(169, 8, 49), (151, 88, 31), (68, 14, 37), (180, 158, 33), (51, 122, 84), (45, 100, 146), (214, 238, 223), (18, 40, 74), (105, 193, 142), (228, 219, 58), (66, 165, 112), (166, 51, 110), (111, 160, 211), (75, 29, 15), (152, 17, 10), (205, 75, 147), (208, 127, 182), (201, 164, 73), (25, 56, 41), (238, 217, 232), (217, 226, 234), (85, 82, 21), (74, 117, 206), (31, 45, 131), (27, 88, 63), (139, 221, 171), (217, 80, 55), (16, 84, 98), (69, 153, 166), (166, 147, 132), (128, 111, 104), (154, 161, 179), (217, 204, 135), (186, 101, 86), (226, 175, 168), (151, 162, 154),(183, 185, 211), (218, 177, 185), (185, 196, 186)]
print(rgb_colors)