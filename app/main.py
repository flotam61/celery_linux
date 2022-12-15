
import datetime
from tasks import cpu_bound

def main():

    task_result_1 = cpu_bound.delay(1, 3)
    task_result_2 = cpu_bound.delay(1, 2)
    task_result_3 = cpu_bound.delay(1, 4)
    task_result_4 = cpu_bound.delay(1, 5)

    print(task_result_1.get(), task_result_2.get(), task_result_3.get(), task_result_4.get())

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)