import os

def soldier(Path, file, format):
    os.chdir(Path)
    i = 1
    Pfiles = os.listdir(Path)
    with open(file) as f:
        files = f.read().split('\n')
    for file in Pfiles:
        if file not in files:
            os.rename(file, file.capitalize())

        # if os.path.splitext(file)[1] == format:
        #     os.rename(file, f"{i}.jpg")
        #     i += 1
        # or
        if file.endswith(f"{format}"):
            os.rename(file, f"{i}.jpg")
            i += 1

if __name__ == '__main__':
    soldier("D:\\testing", "D:\\testing\\Capital.txt", '.jpg')
    # or
    # soldier(r"D:\testing", r"D:\testing\Capital.txt", '.jpg')
    print("Done")
