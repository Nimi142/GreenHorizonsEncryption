import random

def decrypt(string_input1, string_input2):
    letters = "אבגדהוזחטיכלמנסעפצקרשת"
    string_output = ""
    for i in range(0, len(string_input1)):
        if string_input1[i] not in letters:
            string_output += string_input1[i]
            continue
        string_output += letters[(letters.index(string_input2[i]) + letters.index(string_input1[i]) + 1) % len(letters)]
    print(string_output)

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
    return [string_output1, string_output2]


string_in = input("Enter input:\n")
res = encrypt(string_in)
print("Decryption:\n")
decrypt(res[0], res[1])