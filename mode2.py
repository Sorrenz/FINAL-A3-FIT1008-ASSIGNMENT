from landsites import Land
from data_structures.hash_table import LinearProbeTable
from data_structures.heap import MaxHeap
class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = LinearProbeTable()
        self.heap = None
        self.name_lst = None
        self.value_lst = None
        self.teams = n_teams
        
    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        for index in range(len(sites)):
            self.sites[sites[index].get_name()] = sites[index]
            
        self.name_lst = self.sites.keys()
        self.value_lst = self.sites.values()
          
    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        self.construct_score_data_structure(adventurer_size) #O(K)
        lst = []
        for _ in range(self.teams):
            island_score = self.heap.get_max()
            data = self.compute_score(island_score, adventurer_size)   
            if data[0] == 0:
                lst.append(None, data[1])
            else:
                lst.append((self.sites[island_score[1]], data[1]))
        return lst
    def compute_score(self, max_land, original_adventurer: int): #(x,y)
        """_summary_

        Args:
            adventurer_size (int): _description_
            land (Land): _description_
        """
        land = self.sites[max_land[1]]
        remaining_adventurer = original_adventurer - land.get_guardians()
        if remaining_adventurer >= 0:
            adventurer_sent = land.get_guardians()
            gold_stolen = min((adventurer_sent*land.get_gold())/land.get_guardians(), land.get_gold())
            score = (2.5 * (remaining_adventurer)) + gold_stolen
        else:
            adventurer_sent = original_adventurer
            score = (2.5 * (0)) + min((adventurer_sent*land.get_gold())/land.get_guardians(), land.get_gold()) 
            if score < (2.5 * original_adventurer):
                score = 2.5 * original_adventurer
            else:
                gold_stolen = min((adventurer_sent*land.get_gold())/land.get_guardians(), land.get_gold())
                remaining_adventurer = 0
        self.heap.add((score, max_land[1]))
        return (gold_stolen, remaining_adventurer)
    
    def construct_score_data_structure(self, adventurer_number):
        """_summary_

        Args:
            lst (_type_): _description_
        """
        lst = []
        for land in self.value_lst:
            difference = adventurer_number - land.get_guardians()
            if difference >= 0:
                calculation = (2.5 * (difference)) + min((land.get_guardians()*land.get_gold())/land.get_guardians(), land.get_gold())
            else:
                calculation = (2.5 * (0)) + min((adventurer_number*land.get_gold())/land.get_guardians(), land.get_gold())
                if calculation < (2.5 * adventurer_number):
                    calculation = (2.5 * adventurer_number)
            lst.append((calculation, land.get_name()))   
        self.heap = MaxHeap.heapify(lst)
        
if __name__ == "__main__":
    a = Land("A", 400, 100)
    b = Land("B", 300, 150)
    c = Land("C", 100, 5)
    d = Land("D", 350, 90)
    e = Land("E", 300, 100)
    #f = Land("F", 400, 140)
    #g = Land("G", 400, 20)
    #h = Land('H', 200, 5)
    #i = Land("F", 400, 100)
    # Create deepcopies of the sites
    sites = [
        Land(a.get_name(), a.get_gold(), a.get_guardians()),
        Land(b.get_name(), b.get_gold(), b.get_guardians()),
        Land(c.get_name(), c.get_gold(), c.get_guardians()),
        Land(d.get_name(), d.get_gold(), d.get_guardians()),
        Land(e.get_name(), e.get_gold(), e.get_guardians())
    ]
    
    """sites2 = [
        Land(f.get_name(), f.get_gold(), f.get_guardians()),
        Land(g.get_name(), g.get_gold(), g.get_guardians()),
        Land(h.get_name(), h.get_gold(), h.get_guardians())
    ]"""
    
    nav = Mode2Navigator(8)
    nav.add_sites(sites)
    #print(nav.sites)
    #print("__________________________")
    #nav.add_sites(sites2)
    lol = nav.simulate_day(100)
    print(lol)
    #nav.construct_score_data_structure(lol)
    #nav.simulate_day(100)
    #print(nav.sites)