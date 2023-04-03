# import databaseController
from packages.Database.databaseController import (
    SaveDataInFile,
    getAllDataFromCollection,
)
from packages.Scripts.ParserController import getPayload
from packages.Scripts.toH5AndCsv import toH5AndCsv


def main():
    # SaveDataInFile()
    # getAllDataFromCollection()
    # getPayload()
    toH5AndCsv()


if __name__ == "__main__":
    main()
