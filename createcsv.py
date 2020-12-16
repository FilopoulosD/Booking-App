def create_csv(tuple):
    print("Writing File")
    f = open("file.csv", "w")
    for l in range(0,len(tuple)):
        for i in range(0,len(tuple[l])):
            f.write(tuple[l][i])
            f.write(",")
        f.write("\n")
    f.close()




