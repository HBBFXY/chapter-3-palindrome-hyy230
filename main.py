def main():
    num_str=input("请输入一个五位数的数字:")
    if not num_str.isdigit():
        print("错误：输入必须为纯数字!")
        return
    if len(num_str)!=5:
        print("错误：输入必须为五位数!")
        return
    if num_str==num_str[::-1]:
        print("这是一个回文数")
    else:
        print("这不是一个回文数")
if __name__=="__main__":
    main()
