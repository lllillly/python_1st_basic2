from db import Person
from util import Util
from program import Program

bhj = Person()
bhj.data_setter("방효진", 19, "여성")

# sts = Person()
# sts.data_setter("신태섭", 19, "남성")

# oeh = Person()
# oeh.data_setter("오은하", 15, "여성")

# People = []

# People.append(bhj)
# People.append(sts)
# People.append(oeh)

# print(People)

# for p in People:
#     p.add_age()
#     print(p)

DB_PEOPLE = []
DB_PEOPLE.append(bhj)


def startApp():
    print("🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    print("1. View People")
    print("2. Add People")
    print("3. Delete People")
    print("4. Exit Program")
    print("🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀")

    an = Util.custom_input()

    if an is False:
        print("[SYSTEM] 잘못된 입력 입니다.")
        startApp()
    else:
        if an == 1:
            Program.view_people(DB_PEOPLE)
            startApp()
        elif an == 2:
            result = Program.create_people(DB_PEOPLE)

            if result is True:
                print("[SYSTEM] 새로운 사람이 추가되었습니다.")
                startApp()
            else:
                print("[SYSTEM] 사람 추가에 실패하였습니다. 다시 시도해 주세요.")
                startApp()
        elif an == 3:
            result = Program.delete_people(DB_PEOPLE)

            if result is True:
                print("[SYSTEM] 사람이 삭제되었습니다.")
                startApp()
            else:
                print("[SYSTEM] 사람 삭제에 실패하였습니다. 다시 시도해 주세요.")
                startApp()
        elif an == 4:
            print("프로그램 종료")
        else:
            print("[SYSTEM] 잘못된 입력 입니다.")
            startApp()


startApp()
