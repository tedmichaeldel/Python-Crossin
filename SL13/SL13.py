class OlympicGames:
    def __init__(self, country_name, GM, SM, BM):
        self.country_name = country_name
        self.GM = GM
        self.SM = SM
        self.BM = BM

    def Increased_medals(self, increased_medals):
        print increased_medals

    def sum_medals_print(self):
        sum_medals = self.GM + self.SM + self.BM
        print sum_medals

    def sum_medals(self):
        sum_medals = self.GM + self.SM + self.BM
        return sum_medals

    def medals_list(self):
        print ('Gold Medals:', self.GM, 'Silver Medals:', self.SM, 'Bronze Medals:', self.BM,
               'Sum Medals:',self.sum_medals())


China = OlympicGames('China',40,30,20)
America = OlympicGames('America',30,41,20)
Russia = OlympicGames('Russia',20,30,42)

China.Increased_medals(20)
China.sum_medals_print()
China.medals_list()

Gold_Medals_list_rank_dict = {'China':China.GM,'America':America.GM,'Russia':Russia.GM}
Gold_Medals_list_rank = sorted(Gold_Medals_list_rank_dict.iteritems(),key = lambda d:d[1],reverse= True)
print Gold_Medals_list_rank
Sum_Medals_list_rank_dict = {'China':China.sum_medals(),'America':America.sum_medals(),'Russia':Russia.sum_medals()}
Sum_Medals_list_rank = sorted(Sum_Medals_list_rank_dict.iteritems(),key = lambda d:d[1],reverse= True)
print Sum_Medals_list_rank