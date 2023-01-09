with open("day.txt", "r",encoding="utf8") as f:
    lines=f.readlines()

for line in range(len(lines)):
    lines[line]=lines[line].strip()
file="\n".join(lines)


file=file.replace("me \"","\"Семён: ")
file=file.replace("th \"","\"Мысли: ")

file=file.replace("slp \"","\"Пионерка: ")
file=file.replace("unp \"","\"Пионерка: ")
file=file.replace("dvp \"","\"Пионерка: ")
file=file.replace("uvp \"","\"Девочка-Кошка: ")
file=file.replace("elp \"","\"Пионер: ")
file=file.replace("shp \"","\"Пионер: ")

file=file.replace("el \"","\"Электроник: ")
file=file.replace("sh \"","\"Шурик: ")

file=file.replace("mi \"","\"Мику: ")
file=file.replace("uv \"","\"Юля: ")
file=file.replace("sl \"","\"Славя: ")
file=file.replace("us \"","\"Ульяна: ")
file=file.replace("dv \"","\"Алиса: ")
file=file.replace("un \"","\"Лена: ")

file=file.replace("mz \"","\"Женя: ")
file=file.replace("cs \"","\"Виола: ")
file=file.replace("pi \"","\"Пионер: ")
file=file.replace("mt \"","\"Ольга Дмитриевна: ")

file=file.replace("all \"","\"Пионеры: ")
file=file.replace("voice \"","\"Голос: ")
file=file.replace("voices \"","\"Голоса: ")
file=file.replace("dreamgirl \"","\"... : ")
file=file.replace("message \"","\"Сообщение: ")

items=file.split("\n\"")
for i in range(len(items)):
    items[i]=items[i].split("\"",1)[0]

file="\n".join(items)
file=file.replace("{/i}","_")
file=file.replace("{i}","_")
file=file.replace("{w}","")
with open("dayconv.txt", "w",encoding="utf8") as f:
    f.write(file)
