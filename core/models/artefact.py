from django.db import models

from .localization import Localization
from .collection import Collection
from .raw_material import RawMaterial
from .sub_type import SubType
from .archaelogical_site import ArchaeologicalSite

class Artefact(models.Model):
    class ConservationStatus(models.IntegerChoices):
        PERFECT = 1, "Perfeito",
        GOOD = 2, "Bom",
        REGULAR = 3, "Regular"
        BAD = 4, "Ruim"
        CRITICAL = 5, "Critical"
        IRRETRIEVABLE = 6, "Irreversível"
    class Completeness(models.IntegerChoices):
        WHOLE = 1, "Inteiro"
        FRAGMENTED = 2, "Fragmentado"
        FRACTURE = 3, "Fraturado"
    class DetailConservationStatus(models.IntegerChoices):
        FRIABLE = 1, "Friável"
        ERODED = 2, "Erodido"
        CHIPPED = 3, "Lascado"
        INCOMPLETE = 4, "Incompleto"
        CHEMICHAL_CHANGE = 5, "Alterado quimicamente"
        DEFORMED = 6, "Deformado"
        STABLE = 7, "Estável"
    class CollectionCategory(models.IntegerChoices):
        ARCHAEOLOGICAL = 1, "Arqueológico"
        ETHNOGRAPHIC = 2, "Etnográfico"
        PALEONTOLOGICAL = 3, "Paleontológico"
        HISTORIC = 4, "Histórico"
        BIBLIOGRAPHIC = 5, "Bibliográfico"
        DOCUMENTAL = 6, "Documental"
        INDETERMINATE = 7, "Indeterminado"
    class EthnicGroup(models.IntegerChoices):
        SAMBAQUI = 1, "Sambaqui"
        GUARANI = 2, "Guarani"
        ITARARE_TAQUARA = 3, "Itararé/Taquara"
        INDETERMINATE = 4, "Indeterminado"
    class Technique(models.IntegerChoices):
        PERCUSSION = 1, "Percussão"
        PRESSURE_FLAKING = 2, "Lasqueamento por pressão"
        GRINDING = 3, "Abrasão / Polimento"
        DRILLING = 4, "Perfuramento"
        CARVING = 5, "Entalhe"
        SCRAPING = 6, "Raspagem"
        RETOUCH = 7, "Retoque"
        BURNISHING = 8, "Friccionamento"
        NONE_IDENTIFIED = 9, "Não identificada"
    name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, null=True, blank=True)
    dimension_length = models.PositiveSmallIntegerField()
    dimension_width = models.PositiveSmallIntegerField()
    weigth = models.PositiveIntegerField()
    dating = models.PositiveSmallIntegerField(null=True, blank=True)
    conservation_status = models.IntegerField(choices=ConservationStatus.choices, default=1)
    completeness = models.IntegerField(choices=Completeness.choices, default=1)
    detail_conservation_status = models.IntegerField(choices=DetailConservationStatus.choices, default=1)
    collection_category = models.IntegerField(choices=CollectionCategory.choices, default=1)
    ethnic_group = models.IntegerField(choices=EthnicGroup.choices, default=1)
    technique = models.IntegerField(choices=Technique.choices, default=1)
    description = models.TextField()
    observation = models.TextField()
    register_date = models.DateField(auto_now_add=True)
    bibliographic_reference = models.TextField()
    reserved = models.BooleanField(default=False)
    localization = models.ForeignKey(Localization, on_delete=models.PROTECT, related_name="artefacts_localization")
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name="artefacts")
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.PROTECT, related_name="artefacts_rm")
    sub_type = models.ForeignKey(SubType, on_delete=models.PROTECT, related_name="artefacts_st")
    archaeological_site = models.ForeignKey(ArchaeologicalSite, on_delete=models.PROTECT, related_name="artefacts_as")

    def __str__(self):
        return f"#{self.id} {self.name}"