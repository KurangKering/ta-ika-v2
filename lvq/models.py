from django.db import models
from django_pandas.managers import DataFrameManager
# Create your models here.
import json

class Dataset(models.Model):
	clump_thickness = models.IntegerField(null=True, blank=True)
	uniformity_of_cell_size = models.FloatField(null=True, blank=True)
	uniformity_of_cell_shape = models.FloatField(null=True, blank=True)
	marginal_adhesion = models.FloatField(null=True, blank=True)
	single_epithelial_cell_size = models.FloatField(null=True, blank=True)
	bare_nuclei = models.FloatField(null=True, blank=True)
	bland_chromatin = models.FloatField(null=True, blank=True)
	normal_nucleoli = models.FloatField(null=True, blank=True)
	mitoses = models.FloatField(null=True, blank=True)
	kelas = models.IntegerField(null=True, blank=True)


class DatasetPreprocessing(models.Model):
	clump_thickness = models.FloatField(null=True, blank=True)
	uniformity_of_cell_size = models.FloatField(null=True, blank=True)
	uniformity_of_cell_shape = models.FloatField(null=True, blank=True)
	marginal_adhesion = models.FloatField(null=True, blank=True)
	single_epithelial_cell_size = models.FloatField(null=True, blank=True)
	bare_nuclei = models.FloatField(null=True, blank=True)
	bland_chromatin = models.FloatField(null=True, blank=True)
	normal_nucleoli = models.FloatField(null=True, blank=True)
	mitoses = models.FloatField(null=True, blank=True)
	kelas = models.FloatField(null=True, blank=True)


class Inisialisasi(models.Model):
	epochs = models.IntegerField(null=True, blank=True)
	persen_uji = models.FloatField(null=True, blank=True)
	lr = models.FloatField(null=True, blank=True)
	pengurangan_lr = models.FloatField(null=True, blank=True)
	minimum_lr = models.FloatField(null=True, blank=True)
	window = models.FloatField(null=True, blank=True)


class BobotAwal(models.Model):
	dataset_id = models.IntegerField(null=True, blank=True)
	x1 = models.FloatField(null=True, blank=True)
	x2 = models.FloatField(null=True, blank=True)
	x3 = models.FloatField(null=True, blank=True)
	x4 = models.FloatField(null=True, blank=True)
	x5 = models.FloatField(null=True, blank=True)
	x6 = models.FloatField(null=True, blank=True)
	x7 = models.FloatField(null=True, blank=True)
	x8 = models.FloatField(null=True, blank=True)
	x9 = models.FloatField(null=True, blank=True)
	kelas = models.IntegerField(null=True, blank=True) 

class BobotAkhir(models.Model):
	x1 = models.FloatField(null=True, blank=True)
	x2 = models.FloatField(null=True, blank=True)
	x3 = models.FloatField(null=True, blank=True)
	x4 = models.FloatField(null=True, blank=True)
	x5 = models.FloatField(null=True, blank=True)
	x6 = models.FloatField(null=True, blank=True)
	x7 = models.FloatField(null=True, blank=True)
	x8 = models.FloatField(null=True, blank=True)
	x9 = models.FloatField(null=True, blank=True)
	kelas = models.IntegerField(null=True, blank=True)
	metode = models.CharField(max_length=20)