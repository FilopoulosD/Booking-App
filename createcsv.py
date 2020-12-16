
def create_csv(tuple1,firstrow):
    print("Writing File")
    f = open("file.csv", "w")
    tuple = firstrow + tuple1
    for l in range(0,len(tuple)):
        for i in range(0,len(tuple[l])):
            f.write(str(tuple[l][i]))
            if i != len(tuple[l]) - 1:
                f.write(",")
        if l != len(tuple):
            f.write("\n")
    f.close()







