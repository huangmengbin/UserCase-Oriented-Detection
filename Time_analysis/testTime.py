from func_timeout import func_set_timeout
import time
import datetime
import func_timeout.exceptions


@func_set_timeout(5)
def test():
    while True:
        print(111)
        time.sleep(1)


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    try:
        test()
    except func_timeout.exceptions.FunctionTimedOut:
        print(222)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)
