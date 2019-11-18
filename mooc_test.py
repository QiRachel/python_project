"""
“数字猜猜猜”小游戏
"""
import sys
import random
from datetime import datetime

input_list = []  # 存放用户开始输入2个数字，用做区间


def guide_page(guide_word):
    """
     提示玩家进入游戏，并输出如效果图标题的所示信息
    :param guide_word:
    :return:
    """
    print("{0}{1}{0}".format("*" * 12, guide_word))


def all_num(n):
    """
    判断指定的值是否为数字
    :param n:
    :return:
    """

    return n.isdigit()  # 检测字符串是否只由数字组成


def num_legal(ls):
    """
    判定指定序列中的数值是否相等以及记录数字区间起始位置的值是否大于记录数字区间终止位置的值
    :param ls:
    :return:
    """
    if ls[0] == ls[1]:
        print("您输入的区间数字相同！！！请重新启动程序。")
        sys.exit()
    elif ls[0] > ls[1]:
        print("您输入的区间大小有误！！！请重新启动程序。")
        sys.exit()
    else:
        return 1


def set_final_num(num1, num2):
    """
    根据用户输入的2个数字，检验判断后在该区间生成一个随机数字
    :param num1: 用户输入的第一个
    :param num2:用户输入的第二个
    :return:区间内的一个随机数字
    """
    input_list[:] = [num1, num2]
    # 去除列表中不为数字的元素
    ret_list = list(filter(all_num, input_list))

    # 判断2个数是否都合要求
    if len(ret_list) != 2:
        print("您所输入的为非数字字符，请重新启动！")
        sys.exit()

    input_list[:] = list(map(lambda n: int(n), input_list))

    # print(input_list)
    # 判断区间合法性
    num_legal(input_list)

    print("所产生的随机数字区间为：{}".format(str(ret_list)))

    return random.randint(int(num1), int(num2))  # 左闭右闭


def check_num_legal(num):
    """
    判断用户输入的数字是否在区间内
    :param num: 用户猜测的数字
    :return:
    """
    # print(input_list)
    if input_list[0] <= num <= input_list[1]:
        return True
    else:
        print("对不起，您输入的数字未在指定区间！！！")
        return False


def write_record(times, value):
    """
    将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件
    :param times:
    :param value:
    :return:
    """
    now_time = datetime.now()

    txt = "{0}:第{1}次您的猜测数字为:{2}\r\n".format(now_time, times, value)

    with open("record.txt", mode="a+", encoding='utf-8') as f:
        f.write(txt)


guest_count = 0  # 猜测次数为0


def main(rand1):
    """
    输入猜测数字，判断是否正确，并记录
    :param rand1:
    :return:
    """
    temp = rand1
    guess_count = 0

    while 1:
        guess_num = input("请继续输入您猜测的数字：")

        if not all_num(guess_num):
            print("您所输入的为非数字字符，请重新输入！")
            # main(temp)
            continue
        else:
            guess_num = int(guess_num)
            # 校验猜测的数字是否在区间内
            if not check_num_legal(guess_num):
                # 若是不在之前的区间内，递归执行main函数
                # main(temp)
                continue
            else:
                # 进入猜测流程
                guess_count = guess_count + 1
                # print(guess_count)
                write_record(guess_count, guess_num)
                # 校验猜测的数字是否正确
                if guess_num == temp:
                    print("恭喜您，只用了{}次就赢得了比赛".format(guess_count))
                    return
                elif guess_num < temp:
                    print("Lower than the answer")
                else:
                    print("Higher than the answer")


if __name__ == "__main__":
    guide_page("欢迎进入数字猜猜猜小游戏")

    i = input("数字区间起始值：")
    j = input("数字区间终止值：")

    r = set_final_num(i, j)
    if r:
        main(r)
