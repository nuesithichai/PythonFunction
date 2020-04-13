# สร้างฟังก์ชั่นแบบไม่มี Return
def hello(name):
    print("Hello %s" % name)


# การเรียกใช้งานฟังก์ชั่น
hello("Sithichai")


# สร้างฟังก์ชั่นแบบมี Return Value
def area(width, height):
    total = width * height
    return total


# การเรียกใช้งานฟังก์ชั่น
print(area(10, 30))


# ฟังก์ชั่นแบบมีการกำหนดค่าเริ่มต้นไว้
def show_info(name="", salary=0.00, lang="not define"):
    print("Name: %s" % name)
    print("Salary: %s" % salary)
    print("Language: %s" % lang)


# การเรียกใช้งานฟังก์ชั่น
show_info("Sithichai", 12000)
