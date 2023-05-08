

class Solution:
    def maxRealValue(self , m , sellPrice , realValue ):
        # write code here
        sellPrice_sorted = sorted(sellPrice)
        realValue_sorted = sorted(realValue,reverse=True)
        temp_price = 0
        temp_value = 0
        for i in range(len(sellPrice)):
            temp_price += sellPrice_sorted[i]
            if temp_price <= m:
                temp_value+=realValue_sorted[i]
            else:
                temp_price -= sellPrice_sorted[i]
        return temp_value