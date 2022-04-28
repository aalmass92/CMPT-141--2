# A list of magic items .
loot = [['Sword of Fighting ', 1250, 10],
        ['Scroll of Conjure Milk', 20, 5],
        ['Yellow Wizard Robe ', 100 , 3] ,
         ['Orcish Rhyming Dictionary ', 550, 1] ]
expensive_loot = [ x for x in loot if x [1] > 500 ]

print(expensive_loot)