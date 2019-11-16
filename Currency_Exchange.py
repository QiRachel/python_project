# 货币转换系统

# 货币转换的四种服务
service_menu = {
    1: "人民币转换美元",
    2: "美元转换人民币",
    3: "人民币转换欧元",
    0: "结束程序"
}
# print(service_menu)

is_to_choice = True
while is_to_choice:
    print("**********欢迎使用货币转换系统**********")
    for k, v in service_menu.items():
        print("{}.{}".format(k, v))

    Your_Choice = input("请您选择需要的服务：")

    # 用户输入错误数据，小数，负数，所以用list校验
    # 选择服务,0-3进入正常程序，选择错误则提示重新输入
    if Your_Choice not in ['1', '2', '3', '0']:
        # 选择错误，重新选择
        print("您输入的选择有误,请重新输入")
    else:
        # 选择正确
        Your_Choice = int(Your_Choice)

        if Your_Choice in [1, 2, 3]:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            chose_item = service_menu[Your_Choice].split('转换')
            print("欢迎使用{}服务".format(service_menu[Your_Choice]))
            your_money = input("请输入您要转换的{}金额：".format(chose_item[0]))
            # print("您需要转换的{0}为：{1}{0}".format(chose_item[0], your_money))

            your_money = int(your_money)

            # 1人民币=0.13欧元
            # 1美元= 6.72人民币
            if Your_Choice == 1:
                # 转换美元
                RMB_to_US = your_money / 6.72
                print("您需要转换的人民币为：{:0,.2f}元".format(your_money))
                print("兑换成美元为：{:0,.2f}$".format(RMB_to_US))
                # print("兑换成美元为：{:0,.0f}$".format(RMB_to_US))
                # print("兑换成美元为：{}$".format(format(RMB_to_US, '.2f')))
            elif Your_Choice == 2:
                # 美元转换人民币
                US_to_RMB = your_money * 6.72
                print("您需要转换的美元为：{} $".format(your_money))
                print("兑换成人民币为：{:0,.2f}元".format(US_to_RMB))
                # print("兑换成人民币为：{}元".format(format(US_to_RMB, '.2f')))
            else:
                # 人民币转换欧元
                RMB_to_EUR = your_money * 0.13
                print("您需要转换的人民币为：{:0,.2f}元".format(your_money))
                print("兑换成欧元为：{:0,.2f}欧元".format(RMB_to_EUR))
                # print("兑换成欧元为：{}欧元".format(format(RMB_to_EUR, '.2f')))

            print("========================================")
        else:
            is_to_choice = False
            print('感谢您的使用，祝您生活愉快，再见！')
