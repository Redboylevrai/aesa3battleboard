import unittest

from combattant import Combattant


class PropTestCase(unittest.TestCase):
    def test_attributs_calcules(self):
        c = Combattant("Ninja")

        self.assertEqual(c.points_action, 6, "valeur calculée à 6 par défaut")

        self.assertEqual( c.PV, 45, '45 points de vie au départ' )

        # label du champ PV: Points de vie
        self.assertEqual( c.labels.PV, 'Points de vie' )



        with self.assertRaises(AttributeError):
            '''
            on teste ici que points_action est une property calculée qu'on ne peut pas
            fixer arbitrairement. le test est OK si une exception est lancée
            '''
            c.points_action = 10 # interdit !!!


if __name__ == '__main__':
    unittest.main()

