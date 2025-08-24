from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(
        max_length=50,
        choices=(
            ('alquiler', 'Alquiler'),
            ('suministros', 'Suministros'),
            ('salarios', 'Salarios'),
            ('herramientas', 'Herramientas'),
            ('otros', 'Otros')
        ),
        default='otros'
    )
    imagen_gasto = models.ImageField(upload_to='imagen_gastos/', max_length=5500, blank=True, null=True)
    fichero_gasto = models.FileField(upload_to='fichero_gastos/', max_length=5500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Gasto de {self.monto}€ en {self.descripcion}"


class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    persona_contacto = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    imagen_proveedor = models.ImageField(upload_to='imagen_proveedors/', max_length=5500, blank=True, null=True)
    fichero_proveedor = models.FileField(upload_to='fichero_proveedors/', max_length=5500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_empresa


class Vehiculo(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='vehiculos')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True, help_text="Ej: 1234 ABC")
    vin = models.CharField(max_length=17, blank=True, null=True, help_text="Número de identificación del vehículo")
    color = models.CharField(max_length=50, blank=True, null=True)
    imagen_vehiculo = models.ImageField(upload_to='imagen_vehiculos/', max_length=5500, blank=True, null=True)
    fichero_vehiculo = models.FileField(upload_to='fichero_vehiculos/', max_length=5500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"
    
    
    

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    imagen_cliente = models.ImageField(upload_to='imagen_clientes/', max_length=5500, blank=True, null=True)
    fichero_cliente = models.FileField(upload_to='fichero_clientes/', max_length=5500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre_completo
    



class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=100, unique=True)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio de compra al proveedor")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio de venta al cliente")
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

class FacturaCompra(models.Model):
    #proveedor = models.CharField(max_length=200)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name='facturas')
    numero_factura = models.CharField(max_length=100, unique=True)
    fecha = models.DateField(default=timezone.now)
    total_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen_factura = models.ImageField(upload_to='imagen_facturas_compra/', max_length=5500, blank=True, null=True)
    fichero_factura = models.FileField(upload_to='fichero_facturas_compra/', max_length=5500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Factura {self.numero_factura} de {self.proveedor}"
        
class FacturaVenta(models.Model):
    #cliente = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clientes')
    fecha = models.DateField(default=timezone.now)
    total_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen_factura = models.ImageField(upload_to='imagen_facturas_venta/', max_length=5500, blank=True, null=True)
    fichero_factura = models.FileField(upload_to='fichero_facturas_venta/', max_length=5500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Factura para {self.cliente} del {self.fecha}"

class LineaFacturaVenta(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='lineas')
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_factura = models.ImageField(upload_to='imagen_facturas_linea_venta/', max_length=5500, blank=True, null=True)
    fichero_factura = models.FileField(upload_to='fichero_facturas_linea_venta/', max_length=5500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def subtotal(self):
        return self.cantidad * self.precio_unitario
        
    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre}"
    
    
       
    

class TeamMember(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_members/' , blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    es_activo = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Message from {self.name} - {self.subject}'


class Service(models.Model):
    # Campos para la barra de navegación lateral (pestañas)
    icono_fa = models.CharField(max_length=50, help_text="Ej: fa-car-side", blank=True, null=True)
    titulo_pestaña = models.CharField(max_length=100, blank=True, null=True)

    # Campos para el contenido de la pestaña
    titulo_contenido = models.CharField(max_length=200, help_text="Ej: 15 Years Of Experience...", blank=True, null=True)
    imagen_contenido = models.ImageField(upload_to='service_images/', blank=True, null=True)
    descripcion_corta = models.TextField( blank=True, null=True)
    
    # Campo para los puntos de la lista (calidad, expertos, etc.)
    puntos_lista = RichTextField(blank=True, null=True, help_text="Use HTML para los puntos, ej: <p><i class='fa fa-check...'></i>Quality Servicing</p>")

    # Campos para el encabezado de la página de servicios
    imagen_encabezado = models.ImageField(upload_to='service_images/headers/', blank=True, null=True, default='cars_repairs_app/img/carousel-bg-2.jpg' )
    
    # Campo para la sección de "Booking"
    titulo_booking = models.CharField(max_length=200, blank=True, null=True)
    descripcion_booking = models.TextField(blank=True, null=True)
    
    # Campos de gestión
    orden = models.IntegerField(default=0, blank=True, null=True)
    es_activo = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo_pestaña

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['orden']


class Booking(models.Model):
    """
    Modelo para almacenar las reservas o citas de los clientes.
    """
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    # Usa una ForeignKey para relacionar la reserva con un servicio existente
    servicio = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='bookings')
    fecha_servicio = models.DateTimeField(default=timezone.now)
    solicitud_especial = models.TextField(blank=True, null=True)
    
    # Campos de gestión
    creado_el = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reserva de {self.nombre} para el servicio {self.servicio.titulo_pestaña if self.servicio else 'N/A'}"
        
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-creado_el']


class Testimonial(models.Model):
    autor = models.CharField(max_length=100, blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)
    texto = models.TextField( blank=True, null=True)
    # Esta es la clave: el ForeignKey que relaciona el testimonio con un servicio.
    servicio = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='testimonials')
    
    def __str__(self):
        return f"Testimonio de {self.autor} para {self.servicio.titulo_pestaña}"
    
    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        
                
        

class CarouselItem(models.Model):
    titlo = models.CharField(max_length=200,blank=True, null=True)
    subtitlo = models.CharField(max_length=200,blank=True, null=True)
    imagen = models.ImageField(upload_to='carousel_images/',blank=True, null=True)
    imagen_principal = models.ImageField(upload_to='carousel_images/',blank=True, null=True)
    saber_mas_link = models.URLField(blank=True, null=True)
    es_activo = models.BooleanField(default=False)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"titulo: {self.titlo} - {self.subtitlo} - {self.saber_mas_link} - {self.creado_el}"
    
    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"
        

class OrdenDeTrabajo(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('entregada', 'Entregada'),
    )
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordenes')
    #vehiculo = models.CharField(max_length=200, help_text="Ej: Marca, modelo y matrícula")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, related_name='ordenes') # Usar el modelo Vehiculo
    
    descripcion_problema = models.TextField()
    servicios_realizados = models.ManyToManyField(Service, blank=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='pendiente')
    fecha_entrada = models.DateField(default=timezone.now)
    fecha_salida_estimada = models.DateField(blank=True, null=True)
    factura = models.OneToOneField(FacturaVenta, on_delete=models.SET_NULL, null=True, blank=True)
    imagen_ot = models.ImageField(upload_to='imagen_ots/', max_length=5500, blank=True, null=True)
    fichero_ot = models.FileField(upload_to='fichero_ots/', max_length=5500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"Orden de Trabajo #{self.id} - {self.cliente.nombre_completo}"