FILE_NAME = "data.txt"

def pievienot(rindina):
    f = open(FILE_NAME, 'a', encoding="utf-8")
    f.write(rindina + '\n')
    f.close()