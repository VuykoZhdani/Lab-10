from transistor import Transistor, TransistorType

from transistorlist import TransistorList


def main():

    tr_list = TransistorList()
    tr_list.push_back(Transistor(TransistorType.NPN, "2b2222", 3, 2))
    tr_list.push_back(Transistor(TransistorType.PNP, "2da1201y", 12, 0.4))
    tr_list.push_back(Transistor(TransistorType.NPN, "2DC4617SQ", 5, 0.5))
    tr_list.push_back(Transistor(TransistorType.PNP, "AC857BQ", 5, 0.1))
    tr_list.push_back(Transistor(TransistorType.NPN, "DXT697BK", 8, 0.5))
    tr_list.insert(Transistor(TransistorType.PNP, "DXT751Q", 6, 3), 0)
    print(tr_list)
    tr_list.sort_by_current()
    print(tr_list)

if __name__ == '__main__':
    main()
