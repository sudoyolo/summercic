from poop import Poop

bathroom_1 = Poop("Men","Occupied",3)
bathroom_2 = Poop("Women","Vacant",2)

bathroom_1.vac()
bathroom_1.gen()
bathroom_1.flr()

bathroom_2.vac()
bathroom_2.gen()
bathroom_2.flr()

'''
Output:
This bathroom is Occupied.
This is a Men's bathroom.
This bathroom is on floor 3.
This bathroom is Vacant.
This is a Women's bathroom.
This bathroom is on floor 2.
'''