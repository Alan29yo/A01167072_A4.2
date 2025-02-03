import sys
import re
import time as t

if __name__ == "__main__":
    filename = sys.argv[1]
    rel_path = "../data/p1/"

    with open(rel_path + filename, encoding="utf-8") as f:
        start = t.time()
        read_data = f.read().splitlines()
        num_list = []
        invalid_list = []
        has_invalid_data = False

        for item in read_data:
            if re.search("^-?[0-9]+[.]?[0-9]*$", item):
                num_list.append(float(item))
            else:
                invalid_list.append(item)
                has_invalid_data = True

        if has_invalid_data:
            print("WARNING: INVALID DATA FOUND.")
            print("The program will discard the invalid items and continue.")
            print("Invalid items: ", invalid_list)
            print("\n")

        # count
        count = len(read_data)
        print("count: ", count)

        # mean
        n = len(num_list)
        mean = sum(num_list) / n
        print("mean: ", mean)

        # median
        sorted_num_list = sorted(num_list)
        sorted_n = len(sorted_num_list)
        med_index = sorted_n // 2

        is_odd = sorted_n % 2 != 0
        median = sorted_num_list[med_index] if is_odd \
            else (sorted_num_list[med_index-1] + sorted_num_list[med_index]) / 2
        print("median: ", median)

        # mode
        num_set = set(num_list)
        if len(num_set) != len(num_list):
            mode = max(num_list, key=num_list.count)
        else:
            mode = "N/A"

        print("mode: ", mode)

        # variance
        var = sum(pow(x - mean, 2) for x in num_list) / (n - 1)

        # standard deviation
        sd = pow(var, 0.5)

        print("std deviation: ", sd)
        print("variance: ", var)

    end = t.time()
    exec_time = (end-start) * 1000
    print("\n\nThe elapsed execution time is :", exec_time, "ms")

    with open(rel_path + "StatisticsResults.txt", "w", encoding="utf-8") as f:
        f.write("COUNT: " + str(count) + "\n")
        f.write("MEAN: " + str(mean) + "\n")
        f.write("MEDIAN: " + str(median) + "\n")
        f.write("MODE: " + str(mode) + "\n")
        f.write("SD: " + str(sd) + "\n")
        f.write("VAR: " + str(var) + "\n\n")
        f.write("\nThe elapsed execution time is :" + str(exec_time) + " ms")
