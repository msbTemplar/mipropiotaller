# cars_repairs_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LineaFacturaVenta, Articulo

@receiver(post_save, sender=LineaFacturaVenta)
def reducir_stock_por_venta(sender, instance, created, **kwargs):
    if created:
        # Solo si la línea de factura es nueva, reduce el stock.
        articulo = instance.articulo
        cantidad_vendida = instance.cantidad
        
        # Asegúrate de que no reducimos el stock por debajo de cero.
        articulo.stock = articulo.stock - cantidad_vendida
        if articulo.stock < 0:
            articulo.stock = 0
            # Opcional: podrías enviar un aviso si el stock es negativo.
        
        articulo.save()