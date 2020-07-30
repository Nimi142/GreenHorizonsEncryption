import random
import re


def decrypt(string_input1, string_input2):
    letters = "אבגדהוזחטיכלמנסעפצקרשת"
    string_output = ""
    for i in range(0, len(string_input1)):
        if string_input1[i] not in letters:
            string_output += string_input1[i]
            continue
        string_output += letters[(letters.index(string_input2[i]) + letters.index(string_input1[i]) + 1) % len(letters)]
    print(string_output)
    return string_output


def encrypt(string_input):
    letters = "אבגדהוזחטיכלמנסעפצקרשת"
    string_output1 = ""
    string_output2 = ""
    for i in string_input:
        if i not in letters or i == " ":
            string_output2 += i
            string_output1 += i
            continue
        if i == "א":
            string_output1 += "ת"
            string_output2 += "א"
            continue
        wanted_num = letters.index(i)
        k = random.randint(0, len(letters) - 1)
        done = False
        for j in range(0, len(letters)):
            if done:
                break
            for r in range(0, len(letters)):
                if (k + j) % len(letters) == wanted_num - 1:
                    string_output1 += letters[k]
                    string_output2 += letters[j]
                    done = True
                    break
    print(string_output1)
    print(string_output2)
    return string_output1 + "\n\n" + string_output2


if __name__ == "__main__":
    decryption_pattern = r"(.+)\n+(.+)"
    file_name = input("Enter name of text file with text: (Caution! The encryption will overwrite the file!)\n")
    try:
        file = open(file_name, "r", encoding="utf-8")
    except IOError:
        raise Exception("File not found!")
    file_content = file.read()
    file.close()
    mode = "-1"
    while mode != "1" and mode != "2":
        mode = input("1: Encrypt, 2 Decrypt: ")
    if mode == "1":  # Encryption
        regex_content = re.compile(r"((?:[\u05d0-\u05f4]|(?<=[\u05be-\u05f4])[\W0-9])+)").search(file_content)
        if regex_content is None or len(regex_content.groups()) == 0:
            raise Exception("File not formatted right!")
        out_string = encrypt(regex_content.group(1))
    else:  # Decryption
        lines = re.search(decryption_pattern, file_content)
        if lines is None or len(lines.groups()) == 0:
            raise Exception("File not formatted right!")
        out_string = decrypt(lines.group(1), lines.group(2))

    file = open(file_name, "w", encoding="utf-8")

    if mode == "1":  # Encryption
        file.write("Original file:\n" + file_content + "\n\nEncrypted content:\n" + out_string +
                   "\n\nDecryption for proof:\n" +
                   decrypt(re.match(decryption_pattern, out_string).group(1), re.match(decryption_pattern, out_string).group(2)))
    else:  # Decryption
        file.write("Original file:\n" + file_content + "\n\nDecrypted content:\n" + out_string)
    print("Project completed successfuly!")
