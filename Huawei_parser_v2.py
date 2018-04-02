import os

input_path = "/home/oladotun/Documents/Python/Codes/Trunk_List/N7TG_list.txt"
output_path = "/home/oladotun/Documents/Python/Codes/Trunk_List/huawei_tg_N7TG_list.log"

count = 0

trunk_file = open(input_path, "r")
output_file = open(output_path, "w")

for tg_line in trunk_file.readlines():
    #print(tg_line)
    if tg_line.startswith("(Number of results"):
        count = 0

    if tg_line.startswith(" Trunk group name") or count == 1:
        if not tg_line.startswith(" Trunk group name") and tg_line != "\n":
            while tg_line.find("  ") >= 1:
                tg_line = tg_line.replace("  ", " ")
            tg_line = tg_line.replace(" ", "|")
            output_file.write(tg_line)
            values = tg_line.split("|")
            #print(values[1])
            #output_file.write(values[0]+"|"+values[1]+"|"+values[2]+"|"+values[3]+"|"+values[4]+"|"+values[5])
            #output_file.write(values[1])
        count = 1

trunk_file.close()
output_file.close()
