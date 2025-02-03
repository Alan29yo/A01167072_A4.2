import sys
import time as t

if __name__ == "__main__":
    filename = sys.argv[1]
    rel_path = "../data/p3/"

    with open(rel_path + filename, encoding="utf-8") as f:
        start = t.time()
        read_data = f.read().splitlines()
        word_list = read_data
        unique_words = set(word_list)
        count_dict = dict.fromkeys(unique_words, 0)

        print("Row Labels\t\t" + "Count")
        for word in word_list:
            count_dict[word] += 1

        sorted_count_dict = sorted(count_dict, key=count_dict.get, reverse=True)
        for word in sorted_count_dict:
            print(word + "\t\t" + str(count_dict[word]))

    end = t.time()
    exec_time = (end-start) * 1000
    print("\n\nThe elapsed execution time is :", exec_time, "ms")

with open(rel_path + "WordCountResults.txt", "w", encoding="utf-8") as f:
    f.write("Row Labels\t\t" + "Count\n")
    for word in sorted_count_dict:
        f.write(word + "\t\t" + str(count_dict[word]) + "\n")
    f.write("\n\nThe elapsed execution time is :" + str(exec_time) + " ms")
