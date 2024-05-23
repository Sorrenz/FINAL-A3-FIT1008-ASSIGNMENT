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
            
        self.value_lst = self.sites.values()
          
    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        self.construct_score_data_structure(adventurer_size) 
        lst = []
        for _ in range(self.teams): #O(K)
            island_score = self.heap.get_max() #O(logn)
            data = self.compute_score(island_score, adventurer_size)   #O(1)
            if data[0] == 0:
                lst.append((None, data[1]))
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
        if original_adventurer >= land.get_guardians():
            remaining_score = (2.5 * original_adventurer)
            if land.get_gold() == 0:
                gold_stolen = 0
                adventurer_sent = 0
            else:
                gold_stolen = land.get_gold()
                adventurer_sent =  land.get_guardians()
                land.set_gold(0)
                land.set_guardians(0)
        else: 
            gold_stolen = min((original_adventurer * land.get_gold()) / land.get_guardians(), land.get_gold())
            if (2.5 * original_adventurer) > gold_stolen:
                #remaining_score = (2.5 * original_adventurer)
                remaining_score = land[0]
                adventurer_sent = 0
            else: 
                remaining_score = land.get_gold() - gold_stolen #careful of this
                land.set_guardians(land.get_guardians() - original_adventurer)
                land.set_gold(land.get_gold() - gold_stolen)
                adventurer_sent = original_adventurer
        self.heap.add((remaining_score, max_land[1]))
        return (gold_stolen, adventurer_sent)
    
    def construct_score_data_structure(self, adventurer_number):
        """_summary_

        Args:
            lst (_type_): _description_
        """
        lst = []
        for land in self.value_lst:
            difference = adventurer_number - land.get_guardians()
            if difference >= 0:
                calculation = (2.5 * (difference)) + land.get_gold()
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
    #print(lol)
    