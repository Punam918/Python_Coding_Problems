'''
Write a Python program to convert a list to a list of dictionaries. 
input = ["Black", "Red", "Maroon", "Yellow"]
input = ["#000000", "#FF0000", "#800000", "#FFFF00"]
[{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_nam
e': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]  
'''

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
colorlist = []
for name,color in zip(color_names,color_codes):
    color_dict = {'colorname':name, 'colorcode':color}
    colorlist.append(color_dict)
print(colorlist)


color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
color_dict_list = [{'color_name': name, 'color_code': code} for name, code in zip(color_names, color_codes)]
print(color_dict_list)
