
from django.test import TestCase

from proj.factories import PetFactory


class PetTestCase(TestCase):
    
    def test_factory(self):
        test_pet = PetFactory(name='Doggy')

        self.assertEqual(test_pet.name, 'Doggy')
