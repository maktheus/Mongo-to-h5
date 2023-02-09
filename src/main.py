# import databaseController
from Database.databaseController import SaveDataInFile, getAllDataFromCollection

def main():
    SaveDataInFile()
    print(getAllDataFromCollection())


if __name__ == "__main__":
    main()


