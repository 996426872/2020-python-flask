# 关于异常及捕获处理  关键字断言assert
import sys

print(sys.platform)
assert ('win' in sys.platform)

# 代码只允许在linux平台运行
if not ('win' in sys.platform):
    raise AssertionError

# 异常处理
while True:
    try:
        x = int(input("请输入整数"))
    except ValueError:
        print("异常：您输入的不是数字，请重新输入")
    else:
        print("没有异常时执行的代码")
        print(x)
        break
    finally:
        print("无论异常与否，都会执行的最终code")



