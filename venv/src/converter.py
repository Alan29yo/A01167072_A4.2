import sys
import re
import time as t

if __name__ == "__main__":
    filename = sys.argv[1]
    rel_path = "../data/p2/"
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                        4: '4', 5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B',
                        12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    with open(rel_path + filename, encoding="utf-8") as f:
        start = t.time()
        read_data = f.read().splitlines()
        num_list = []
        invalid_list = []
        has_invalid_data = False
        bin_list = []
        hex_list = []

        for item in read_data:
            if re.search("^-?[0-9]+[.]?[0-9]*$", item):
                num_list.append(int(item))
            else:
                invalid_list.append(item)
                has_invalid_data = True

        if has_invalid_data:
            print("WARNING: INVALID DATA FOUND.")
            print("The program will discard the invalid items and continue.")
            print("Invalid items: ", invalid_list)
            print("\n")

        print("ITEM\t" + "DEC\t\t\t" + "BIN\t\t\t\t" + "HEX")
        for index, dec_num in enumerate(num_list):
            is_positive = True
            if dec_num < 0:
                complement_bin = (2**10) - abs(dec_num)
                complement_hex = (16**10) - abs(dec_num)
                is_positive = False

            # binary converter
            number = dec_num if is_positive else complement_bin
            binary_string = '' if number != 0 else '0'
            while number > 0:
                binary_string = str(number % 2) + binary_string
                number //= 2
            bin_list.append(binary_string)

            # hexadecimal converter
            number = dec_num if is_positive else complement_hex
            hex_string = '' if number != 0 else '0'
            while number > 0:
                remainder = number % 16
                hex_string = conversion_table[remainder] + hex_string
                number //= 16
            hex_list.append(hex_string)

            print(str(index+1) + "\t\t" + str(dec_num) + "\t\t"
                  + binary_string + "\t\t" + hex_string)

    end = t.time()
    exec_time = (end-start) * 1000
    print("\n\nThe elapsed execution time is :", exec_time, "ms")

with open(rel_path + "ConvertionResults.txt", "w", encoding="utf-8") as f:
    f.write("ITEM\t" + "DEC\t\t\t" + "BIN\t\t\t\t" + "HEX" + "\n")
    for index, dec_num in enumerate(num_list):
        f.write(str(index+1) + "\t\t" + str(dec_num) + "\t\t" +
                bin_list[index] + "\t\t" + hex_list[index] + "\n")
    f.write("\n\nThe elapsed execution time is :" + str(exec_time) + " ms")
