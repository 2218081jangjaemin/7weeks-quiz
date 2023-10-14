class Bungeoppang:
    total_sales = 0

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        Bungeoppang.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

cream_bungeoppang = Bungeoppang("슈크림", 2000)
redbean_bungeoppang = Bungeoppang("팥", 1500)

cream_bungeoppang.sell()
redbean_bungeoppang.sell()

cream_bungeoppang.eat()
redbean_bungeoppang.eat()

print(f"총 판매금은 {Bungeoppang.total_sales}원 입니다.")
