class VcFirm:
    def __init__(self, limit_revenue, limit_funds):
        self.limit_revenue = limit_revenue
        self.limit_funds = limit_funds
        
    def CheckInvestor(self, funds):
        if funds >= self.limit_funds:
            return True
        return False
    
    def CheckCompanies(self, revenue):
        if revenue >= self.limit_revenue:
            return True
        return False