files = ["img_01.png", "data_log.txt", "img_02.png", "readme.md", "img_03.png"]
for file in files:
    print(file)
    
for file in files:
    print(file)
    
clean_img=[file.replace(".png","") for file in files if file.endswith(".png")]
print(clean_img)