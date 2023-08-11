from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio, DirectorGeneral, Producto


# Create your tests here.
class TemplateTest(TestCase):

    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(nombre='lab1', ciudad='stgo', pais='chile')
        self.director = DirectorGeneral.objects.create(nombre='Juan', laboratorio_id=self.laboratorio.id,
                                                       especialidad='xx')
        self.producto = Producto.objects.create(nombre='Producto',
                                                laboratorio_id=self.laboratorio.id,
                                                f_fabricacion= '2020-01-01',
                                                p_costo=1500,
                                                p_venta=2000, )
        print('imprimiento',  self.laboratorio.ciudad)

    def test_lista_laboratorios(self):
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_laboratorios.html')
        self.assertContains(response, '<th scope="col">Nombre</th>')

# Create your tests here.
