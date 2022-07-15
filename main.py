from vcfirmclass import VcFirm
from investorclass import Investor
from companyclass import Company

def main():
    
    vc = VcFirm(1000000, 5000000)
    invest = Investor()
    company = Company()
    
    while True:
        
        print("Welcome to our VC Firm... \nChoose the preferred Option: \n 1. are you interested in Investing ? \n 2. Do you required funding ? \n 3. Exit")
        
        choose = input("Enter you Valuable option : ")
        
        try:
            choose = int(choose)
        except ValueError:
            print("Enter the Valid value")
            continue
        
        if choose == 1:
            print("You are an Investor... \nChoose further options: \n 1. Check your Elgibilty \n 2. New to our platform, Want to register? \n 3. Want to See Companies who need funding. \n 4. Back to previous menu \n 5. Exit")
            
            temp = input("Enter you Valuable option : ")
        
            try:
                temp = int(temp)
            except ValueError:
                print("Enter the Valid value")
                continue
            
            if temp == 1:
                funds = input("Enter your fund you want to invest: ")
                try:
                   funds = float(funds)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                
                if vc.CheckInvestor(funds):
                    print("You are eligible for investment")
                    continue
                else:
                    print("You are not eligible for investment \n Please increase your investment fund")
                    continue
                   
               
            elif temp == 2:
                name = input("Enter the name: ")
                equity = input("Enter the equity you want : ")
                try:
                    equity = float(equity)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                funds = input("Enter the funds you provide(min. is 5000000) : ")
                try:
                    funds = float(funds)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                
                if vc.CheckInvestor(funds):
                    invest.add_investor(name, equity, funds)
                else:
                    print("You are not eligible, Please increase your fund.")
                
            elif temp == 3:
                company.get_details()
                
            elif temp == 4:
                print("Redirected to Main Menu")
                continue
            
            elif temp == 5:
                print("Thank you for visiting us")
                break
            else:
                print("Wrong Input, Redirected to Main Menu")
                continue
            
        elif choose == 2:
            print("You are a Company... \nChoose further options: \n 1. Check your Eligibilty \n 2. New to our platform, Want to register? \n 3. Want to See Investors who is interested in investing. \n 4. Back to previous menu \n 5. Exit")
            
            temp = input("Enter you Valuable option : ")
        
            try:
                temp = int(temp)
            except ValueError:
                print("Enter the Valid value")
                continue
            
            if temp == 1:
                revenue = input("Enter your revenue: ")
                try:
                   revenue = float(revenue)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                
                if vc.CheckCompanies(revenue):
                    print("You are eligible for funding")
                    continue
                else:
                    print("You are not eligible for funding \n Please increase your revenue")
                    continue
            elif temp == 2:
                name = input("Enter the name: ")
                equity = input("Enter the equity you want to sell : ")
                try:
                    equity = float(equity)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                funds = input("Enter the funds you want: ")
                try:
                    funds = float(funds)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                
                revenue = input("Enter your revenue(min. 1000000): ")
                try:
                    revenue = float(revenue)
                except ValueError:
                    print("Enter the Valid value")
                    continue
                
                if vc.CheckCompanies(funds):
                    company.add_companies(name, equity, funds, revenue)
                else:
                    print("You are not eligible, Please increase your revenue.")
            
            elif temp == 3:
                invest.get_details()
                
            elif temp == 4:
                print("Redirected to Main Menu")
                continue
            
            elif temp == 5:
                print("Thank you for visiting us")
                break
            
            else:
                print("Wrong Input, Redirected to Main Menu")
                continue
            
        elif choose == 3:
            print("Thank you for visiting us")
            break
        
        else:
            print("Wrong Input, Choose the option from 1,2 and 3")
            continue
        
if __name__ == "__main__":
    main()