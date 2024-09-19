"""
program which calcluate the total value of books.
Author = sahil
"""


bookprice=24.95
discount= 40/100
copies =60


bookpriceaterdiscount=bookprice-(bookprice*discount)

shippingcost=3+((copies -1)*0.75)
total=(bookpriceaterdiscount*copies)+shippingcost



print(total)


