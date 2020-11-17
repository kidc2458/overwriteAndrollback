import Overwrite
import RollBack


if __name__ == "__main__":
    Overwrite.overwrite("D:/Develop/Git","D:/Develop/Git2","D:/Develop")
    RollBack.rollback("D:/Develop/Git2","D:/Develop/overwiteLog.log")