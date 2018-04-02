import os

input_path = "/home/oladotun/Documents/Python/Codes/Trunk_List/Route Dump_Ericsson.log"
output_path = "/home/oladotun/Documents/Python/Codes/Trunk_List/ericsson_tg.log"

count = 0

trunk_file = open(input_path, "r")
output_file = open(output_path, "w")

#write header to file
#output_file.write("R|NDV|NOCC|NIDL|NBLO|RSTAT")

#qbfile = open("qbdata.txt","r")

for tg_line in trunk_file.readlines():
    if tg_line.endswith("END\n"):
        count = 0

    if tg_line.endswith("RSTAT\n") or count == 1:
        while tg_line.find("  ") >= 1:
            tg_line = tg_line.replace("  ", " ")
        tg_line = tg_line.replace(" ", "|")
        values = tg_line.split("|")
        output_file.write(values[0]+"|"+values[1]+"|"+values[2]+"|"+values[3]+"|"+values[4]+"|"+values[5])
        count = 1

trunk_file.close()
output_file.close()
