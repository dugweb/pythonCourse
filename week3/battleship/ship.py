class Ship(object):
	'''
	Battle Ship class. Stores the ship's position on the board, direction,
	and whether or not a node on the ship has been shot.
	'''
	
	def __init__(self, position = (0,0), vertical = False, name = "Default Ship", length = 2):
		
		self.position = position
		self.length = length
		self.vertical = False
		self.hitBox = self.__generateHitBox()
		self.name = name


	def defend(self, shot = (0,0)):
		''' Compares a shot coordinate with the coordinates in the hitbox.
			***Note***, this returns whether it successfully defended or not
			(so if all shots miss True will be returned)'''

		hb = self.hitBox
		defend = True
		summary = ""

		for shipNode in hb:
			if shipNode['point'] == shot:
				shipNode['hit'] = True
				defend = False

		### Uncomment if you want the Ship class to give some feedback,
		### but that would probably be better left to the Player class

		# if not defend:
		# 	summary += "Hit! "
		# 	if self.sunk():
		# 		summary += "And you sunk my {}".format(self.name)
		# else:
		# 	summary += "Miss!"

		# print summary
		
		return defend

	def sunk(self):
		''' Checks whether this ship has any nodes not hit, otherwise it is sunk'''

		hb = self.hitBox
		
		return all([node['hit'] for node in hb])

	def __generateHitBox(self):
		''' Generates the all the points possible to be hit
			and flags them as not hit. Private Method'''

		output = []

		xIncrement = 0
		yIncrement = 0

		for i in range(self.length):

			output.append({	'point': (self.position[0] + xIncrement,
									  self.position[1] + yIncrement),
							'hit': False })

			xIncrement += 1 if not  self.vertical else 0
			yIncrement += 1 if 		self.vertical else 0

		return output


class AircraftCarrier(Ship):
	def __init__(self, position = (0,0), vertical = False):
		super(AircraftCarrier, self).__init__(position, vertical, "Aircraft Carrier", 5)

class Battleship(Ship):
	def __init__(self, position = (0,0), vertical = False):
		super(Battleship, self).__init__(position, vertical, "Battleship", 4)

class Cruiser(Ship):
	def __init__(self, position = (0,0), vertical = False):
		super(Cruiser, self).__init__(position, vertical, "Cruiser", 3)

class Submarine(Ship):
	def __init__(self, position = (0,0), vertical = False):
		super(Submarine, self).__init__(position, vertical, "Submarine", 3)

class Destroyer(Ship):
	def __init__(self, position = (0,0), vertical = False):
		super(Destroyer, self).__init__(position, vertical, "Destroyer", 2)
			



import unittest

class ShipTestCase(unittest.TestCase):

	def test_ship_creation(self):
		s = Ship()

		self.assertTrue(s != None)
		self.assertEqual(s.length, 2)

	def test_ship_hitbox_generation(self):

		s = Ship((4,6), vertical = True, length = 10)
		self.assertEqual(len(s.hitBox), 10)

	def test_ship_defend(self):

		s = Ship()
		self.assertFalse(s.defend((1,0))) # Calls to Defend return True if there are no hits, and False if there is a hit



if __name__ == '__main__':
    unittest.main()



