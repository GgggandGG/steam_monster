def SendWay(options):
    if options == '1':
        print("---------邮箱---------")
        print("请输入邮箱：")
        Useremail = input()
        print("已发送数字令牌到邮箱！")

    elif options == '2':
        print("---------短信---------")
        print("请输入手机号：")
        phone = input()
        print("已发送数字令牌到手机！")

    else:
        print("请输入正确选项")