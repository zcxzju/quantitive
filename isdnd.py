class Solution:
    def maxRealValue(self , m , sellPrice , realValue ):
        sellPrice.sort()
        realValue.sort(reverse = True)
        i = 0
        while i < len(sellPrice) and sum(sellPrice[:i+1]) <= m:
            i += 1
        return sum(realValue[:i])


m = 800
# 定义并初始化两个列表，存储n双鞋子的售价和实用价值
sellPrice = [100, 200, 300, 400, 500]
realValue = [50, 60, 80, 90, 100]

# 创建一个解决方案对象
solution = Solution()

# 调用对象中的方法，得到实用价值最大的鞋子组合
result = solution.maxRealValue(m, sellPrice, realValue)

# 输出结果
print("The maximum value of shoes that Xiao Zhaomiao can buy is:", result)
