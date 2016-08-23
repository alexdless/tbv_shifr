from string import ascii_letters, digits, punctuation, ascii_lowercase
from random import choice, shuffle
from pickle import dump, load

main_StrDigUpLowPunc = ascii_letters + digits + punctuation + " "#тут набор всех символов + пробел
main_CipherDic = {} #шифр-алфавит
main_Seq = int(input("Введите срез: "))

def CipherDicGen(): #создает шифр-алфавит и сохраняет его копию в файл cipher.txt
    for k in main_StrDigUpLowPunc:
        tmp_value = ""

        for i in range(main_Seq):
            tmp_value += choice(ascii_letters + digits)

        main_CipherDic[k] = tmp_value
        del(tmp_value)

        tmp_file = open("./cipherDic.txt", "wb")
        dump(main_CipherDic, tmp_file)
        tmp_file.close()

def Encryption():
    try:
        with open('./cipherDic.txt', 'rb') as tmp_file:
            main_CipherDic = load(tmp_file)
    except:
        print("ошибка загрузки шифр-словаря")
    with open("encryption_text.txt", "r") as EncryptFile:
        main_EncryptString = ""
        for i in EncryptFile.readlines():
            main_EncryptString += i.strip()
    with open("encrypted_text.txt", "w") as EncryptedFile:
        for i in list(main_EncryptString):
            EncryptedFile.write(main_CipherDic.get(i) + ";")
    print("succefull encrypted, with encrypted_text.txt")

def Decryption():
    try:
        with open('./cipherDic.txt', 'rb') as tmp_file:
            main_CipherDic = load(tmp_file)
    except:
        print("ошибка загрузки шифр-словаря")

    with open("encrypted_text.txt", "r") as EncryptedText:
        main_DecryptTmpString = EncryptedText.readline().split(";")
        main_DecryptString = ""
        for i in main_DecryptTmpString:
            for key, value in main_CipherDic.items():
                if i == value:
                    main_DecryptString += key



    with open("decrypted_text.txt", "w") as DecryptedFile:
        DecryptedFile.write(main_DecryptString)

ver = input("=====================\n1. Генерация шифр-словаря\n2.Шифрование файла 'encryption_text.txt'\n3. Расшифровка файла 'encrypted_text.txt'\n===> ")
if ver == "1":
    CipherDicGen()
elif ver == "2":
    Encryption()
elif ver == "3":
    Decryption()
else:
    print("неверные параметры")