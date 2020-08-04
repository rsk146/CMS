if __name__ == "__main__":
    allFiles = open("allFiles.txt", "r")
    config = open("NANOAOD_jetToolbox_cff_NANO.py", "r")
    file_part_one = config.read(1634+28)
    file_part_two = config.read(669 + 68 + 5)
    file_part_three = config.read(1708 + 43)


    process = 0
    for i in range(4790):
        newFile = open("nano" + str(process) + ".py", "a+")
        newFile.write(file_part_one)
        readLine = allFiles.readline()
        newFile.write("'file:" + readLine[:-1] + "'")
        newFile.write(file_part_two)
        newFile.write(str(process))
        newFile.write(file_part_three)
        newFile.close()
        process += 1
