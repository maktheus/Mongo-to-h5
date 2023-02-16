# import databaseController
from packages.Database.databaseController import SaveDataInFile, getAllDataFromCollection
from packages.Scripts.ParserController import getPayload

def main():
    SaveDataInFile()
    print(getAllDataFromCollection())


if __name__ == "__main__":
    main()


