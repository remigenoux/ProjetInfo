import unittest
from Billard import Billard
from Billes import Bleue, Rouge, Blanche

# Tests pour la méthode fin_partie
class TestBillard(unittest.TestCase):

    def setUp(self):
        self.billard = Billard(100, 200, 2, 1/60)

    def test_fin_partie_same_color(self):
        self.billard.append(Bleue(10, 10))
        self.billard.append(Bleue(20, 20))
        self.assertTrue(self.billard.fin_partie())

    def test_fin_partie_immobile_billes(self):
        # Toutes les billes sont immobiles mais de couleurs différentes
        bille1 = Bleue(10, 10)
        bille2 = Rouge(20, 20)
        bille1.v = 0
        bille2.v = 0
        self.billard.append(bille1)
        self.billard.append(bille2)
        self.assertFalse(self.billard.fin_partie())

# Tests pour la méthode collisions
class TestCollisions(unittest.TestCase):

    def setUp(self):
        self.billard = Billard(100, 200, 2, 1/60)

    def test_bille_bille_collision(self):
        # Deux billes se touchent
        bille1 = Bleue(50, 50)
        bille2 = Rouge(51, 50)
        bille1.v = 1
        bille1.direction = (1, 0)
        bille2.v = 0
        clone = [(bille1.x, bille1.y, bille1.v, bille1.direction, bille1._taille, 0, bille1.coul),
                 (bille2.x, bille2.y, bille2.v, bille2.direction, bille2._taille, 1, bille2.coul)]
        self.assertNotEqual(len(self.billard.collisions(clone, 1/60)), 0)

    def test_wall_collision(self):
        bille = Bleue(95, 50)
        bille.v = 10
        bille.direction = (1, 0)
        clone = [(bille.x, bille.y, bille.v, bille.direction, bille._taille, 0, bille.coul)]
        self.assertNotEqual(len(self.billard.collisions(clone, 1/60)), 0)

# Tests pour la méthode contact_mur
class TestContactMur(unittest.TestCase):

    def test_contact_mur_vertical(self):
        bille = Bleue(95, 50)
        bille.direction = (1, 0)
        bille.contact_mur((100, 200))
        self.assertEqual(bille.direction[0], -1)

    def test_contact_mur_horizontal(self):
        bille = Bleue(50, 195)
        bille.direction = (0, 1)
        bille.contact_mur((100, 200))
        self.assertEqual(bille.direction[1], -1)

# Tests pour la méthode contact_boule
class TestContactBoule(unittest.TestCase):

    def test_contact_boule_movement(self):
        bille1 = Bleue(50, 50)
        bille2 = Rouge(50, 51)
        bille1.direction = (0, 1)
        bille2.direction = (0, -1)
        bille1.contact_boule(bille2)
        self.assertEqual(bille1.direction, (0, -1))
        self.assertEqual(bille2.direction, (0, 1))

    def test_contact_boule_stationary(self):
        bille1 = Bleue(50, 50)
        bille2 = Rouge(50, 51)
        bille1.direction = (0, 1)
        bille2.direction = (0, 0)
        bille1.contact_boule(bille2)
        self.assertEqual(bille1.direction, (0, 0))
        self.assertEqual(bille2.direction, (0, 1))

if __name__ == '__main__':
    unittest.main()
