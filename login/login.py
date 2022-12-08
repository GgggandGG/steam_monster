def login_main():
    while 1:
        print("-----------------")
        print("请选择您的登录身份：")
        print("1.普通用户")
        print("2.管理员")
        print("-----------------")
        option = input()

        if option == '1':
            print("---------普通用户---------")
            print("请输入邮箱：")
            email = input()
            print("请输入密码：")
            password = input()
            print("密码：", password)
            print("请获得数字令牌！")
            break

        elif option == '2':
            print("---------管理员---------")
            print("请输入邮箱：")
            email = input()
            print("请输入密码：")
            password = input()
            print("密码：", password)
            print("请获得数字令牌")
            break

        else:
            print("请输入正确选项")

    from login.sendway import SendWay
    while 1:
        print("------------------------")
        print("请选择获得数字令牌的方式：")
        print("1.邮箱验证")
        print("2.短信验证")
        print("------------------------")
        options = input()
        SendWay(options)
        break

    print("请输入数字令牌：")
    identifyCode = input()
    print(("验证成功！"))
