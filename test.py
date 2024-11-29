import requests

class CurrencyConverter:
    """기본 화폐 변환기 클래스"""
    def __init__(self, base_currency, target_currency):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = None

    def get_rate(self):
        """환율 API에서 가져오는 메소드"""
        api_key = "b99f132ee63b480f3282143d" #내 키임
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{self.base_currency}"
        response = requests.get(url)
        data = response.json() #json형식으로
        self.rate = data['conversion_rates'][self.target_currency]
        return self.rate

    def convert(self, amount):
        """금액 변환"""
        rate = self.get_rate()
        return amount * rate


class JPYtoKRW(CurrencyConverter):
    """엔화 -> 원화 변환"""
    def __init__(self):
        super().__init__("JPY", "KRW")

class KRWtoJPY(CurrencyConverter):
    """원화 -> 엔화 변환""" 
    def __init__(self):
        super().__init__("KRW", "JPY")
        
class USDtoKRW(CurrencyConverter):
    """달러 -> 원화 변환"""
    def __init__(self):
        super().__init__("USD", "KRW")
        
class KRWtoUSD(CurrencyConverter):
    """원화 -> 달러(미국) 변환"""
    def __init__(self):
        super().__init__("KRW", "USD")
        
class GBPtoKRW(CurrencyConverter):
    """파운드(영국) -> 원화 변환"""
    def __init__(self):
        super().__init__("GBP", "KRW")
        
class KRWtoGBP(CurrencyConverter):
    """원화 -> 파운드 변환"""
    def __init__(self):
        super().__init__("KRW", "GBP")
        
class CADtoKRW(CurrencyConverter):
    """캐나다 달러(캐나다) -> 원화 변환"""
    def __init__(self):
        super().__init__("CAD", "KRW")
        
class KRWtoCAD(CurrencyConverter):
    """원화 -> 캐나다 달러 (캐나다) 변환"""
    def __init__(self):
        super().__init__("KRW", "CAD")
        
class AUDtoKRW(CurrencyConverter):
    """호주 달러(호주) -> 원화 변환"""
    def __init__(self):
        super().__init__("AUD", "KRW")

class KRWtoAUD(CurrencyConverter):
    """원화 -> 호주 달러 (호주) 변환"""
    def __init__(self):
        super().__init__("KRW", "AUD")
        
def main ():
    print("어느 나라로 환전하시나요?")
    print("1. 미국, 2. 영국, 3. 캐나다. 4. 호주, 5. 유럽연합, 6. 중국, 7. 일본, 8. 스위스")
    country_choice = int(input("번호를 선택하세요"))
    
    print("1. 외화 -> 원화로 계산")
    print("2. 원화 -> 외화로 계산")
    currency_direction_choice = int(input("번호를 선택하세요"))
    
    amount = float(input("금액을 입력하세요: "))
    
    if( country_choice == 1 ) :
        if( currency_direction_choice == 1 ) :
            converter = USDtoKRW()
        else:
            converter = KRWtoUSD()
    elif( country_choice == 2 ):
        if( currency_direction_choice == 1 ) :
            converter = GBPtoKRW()
        else:
            converter = KRWtoGBP()
    elif( country_choice == 3 ):
        if( currency_direction_choice == 1 ) :
            converter = CADtoKRW()
        else:
            converter = KRWtoCAD()
    elif( country_choice == 4 ):
        if( currency_direction_choice == 1 ) :
            converter = AUDtoKRW()
        else:
            converter = KRWtoAUD()
            
    elif( country_choice == 5 ):
        if( currency_direction_choice == 1 ) :
            converter = EURtoKRW()
        else:
            converter = KRWtoEUR()
    elif( country_choice == 6 ):
        if( currency_direction_choice == 1 ) :
            converter = CNYtoKRW()
        else:
            converter = KRWtoCNY()
    elif( country_choice == 7 ):
        if( currency_direction_choice == 1 ) :
            converter = JPYtoKRW()
        else:
            converter = KRWtoJPY()
    elif( country_choice == 2 ):
        if( currency_direction_choice == 1 ) :
            converter = CJFtoKRW()
        else:
            converter = KRWtoCJF()

    print(f"{country_choice}를 선택하셨습니다. 현재 환율은 다음과 같습니다:")
    print(f"1 단위 {country_choice} 통화당 {converter.get_rate()} 원입니다.")

    
main()