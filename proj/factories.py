
from factory.django import DjangoModelFactory

from proj import models


class PetFactory(DjangoModelFactory):

    class Meta:
        model = models.Pet
