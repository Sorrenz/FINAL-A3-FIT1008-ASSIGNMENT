from landsites import Land
from data_structures.bst import BinarySearchTree
from algorithms.mergesort import mergesort
from algorithms.binary_search import binary_search,_binary_search_aux

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        gold_adventureres_ratio = mergesort(sites, key = lambda land: -(land.get_gold()/ land.get_guardians()))
        binary_tree = BinarySearchTree()
        self.split(gold_adventureres_ratio, binary_tree)
        self.sites = binary_tree
        self.sites.draw()
        self.adventurers = adventurers
        
    def split(self,lst,binary_tree):
        return self.auxilary_split(lst,binary_tree)
    
    def auxilary_split(self,lst,binary_tree):
        if len(lst) == 2:
            binary_tree[-(lst[1].get_gold()/lst[1].get_guardians())] = lst[1]
            binary_tree[-(lst[0].get_gold()/lst[0].get_guardians())] = lst[0]
        elif len(lst) == 1:
            binary_tree[-(lst[0].get_gold()/lst[0].get_guardians())] = lst[0]
        else:
            middle_index = len(lst)//2
            middle_value = lst[middle_index].get_gold()/lst[middle_index].get_guardians()
            binary_tree[-middle_value] = lst[middle_index]
            self.auxilary_split(lst[:middle_index], binary_tree)
            self.auxilary_split(lst[middle_index+1:], binary_tree)
            
        
    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        temp = self.adventurers
        iterator = iter(self.sites)
        island_list = []
        while temp > 0:
            try:
                island = iterator.__next__()
            except StopIteration:
                return island_list
            else:
                if temp >= island.item.get_guardians():
                    island_list.append((island.item,island.item.get_guardians()))
                    temp -= island.item.get_guardians()
                else:
                    island_list.append((island.item, temp))
                    break
        return island_list
            
    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        gold_lst = []
        for adventurers in adventure_numbers:
            temp = adventurers
            gold_discovered = 0
            iterator = iter(self.sites)
            for _ in range(len(self.sites)):
                if temp > 0:
                    island = iterator.__next__()
                    gold_retrieved = min((temp*island.item.get_gold())/island.item.get_guardians(), island.item.get_gold())
                    gold_discovered += gold_retrieved
                    temp -= island.item.get_guardians()
                else:
                    break
            gold_lst.append(gold_discovered)
        return gold_lst

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        """if not self.sites[-(land.get_gold()/land.get_guardians())] in self.sites:
            raise Exception("THE LAND IS NOT IN THE ISLAND LIST")"""
        
        del (self.sites[-(land.get_gold()/land.get_guardians())])
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
        self.sites[-(land.get_gold()/land.get_guardians())] = land
    
if __name__ == "__main__":
    a = Land("A", 400, 100)
    b = Land("B", 300, 150)
    c = Land("C", 100, 5)
    d = Land("D", 350, 90)
    e = Land("E", 300, 100)
    f = Land("F", 400, 140)
    # Create deepcopies of the sites
    sites = [
        Land(a.get_name(), a.get_gold(), a.get_guardians()),
        Land(b.get_name(), b.get_gold(), b.get_guardians()),
        Land(c.get_name(), c.get_gold(), c.get_guardians()),
        Land(d.get_name(), d.get_gold(), d.get_guardians()),
        Land(e.get_name(), e.get_gold(), e.get_guardians()),
    ]
    
    nav = Mode1Navigator(sites, 200)
    results = nav.select_sites_from_adventure_numbers([0, 200, 500, 300, 40])
    nav.update_site(sites[1], 400, 400)