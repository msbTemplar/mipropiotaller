from django.contrib import admin
from .models import CarouselItem,Service, Testimonial, Booking, ContactMessage, TeamMember, Articulo, FacturaCompra, FacturaVenta, LineaFacturaVenta, Cliente, OrdenDeTrabajo, Vehiculo, Proveedor, Gasto
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.db.models import Q








class GastoResource(resources.ModelResource):
    class Meta:
        model = Gasto
        #fields = ('descripcion', 'monto', 'fecha', 'categoria', 'created_at')
        
        
@admin.register(Gasto)
class GastoAdmin(ImportExportModelAdmin): # Usa ImportExportModelAdmin
    resource_class = GastoResource
    list_display = ('descripcion', 'monto', 'fecha', 'categoria', 'is_active')
    list_filter = ('categoria', 'fecha')
    search_fields = ('descripcion',)
    readonly_fields = ('created_at', 'updated_at')

# @admin.register(Gasto)
# class GastoAdmin(admin.ModelAdmin):
#     list_display = ('descripcion', 'monto', 'fecha', 'categoria', 'is_active')
#     list_filter = ('categoria', 'fecha')
#     search_fields = ('descripcion',)
#     readonly_fields = ('created_at', 'updated_at')

# Recurso para el modelo Proveedor
class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        # Deja esta línea vacía para exportar todos los campos del modelo
        #fields = ()

# Administración del Proveedor con exportación
@admin.register(Proveedor)
class ProveedorAdmin(ImportExportModelAdmin): # Usa ImportExportModelAdmin
    resource_class = ProveedorResource
    list_display = ('nombre_empresa', 'persona_contacto', 'telefono', 'email', 'is_active')
    search_fields = ('nombre_empresa', 'persona_contacto', 'email')
    readonly_fields = ('created_at', 'updated_at')


# @admin.register(Proveedor)
# class ProveedorAdmin(admin.ModelAdmin):
#     list_display = ('nombre_empresa', 'persona_contacto', 'telefono', 'email', 'is_active')
#     search_fields = ('nombre_empresa', 'persona_contacto', 'email')
#     readonly_fields = ('created_at', 'updated_at')
    


# Recurso para el modelo Vehiculo
class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo
        # Deja esta línea vacía para exportar todos los campos del modelo
        #fields = ()

# Administración del Vehiculo con exportación
@admin.register(Vehiculo)
class VehiculoAdmin(ImportExportModelAdmin): # Usa ImportExportModelAdmin
    resource_class = VehiculoResource
    list_display = ('cliente', 'marca', 'modelo', 'matricula', 'is_active')
    search_fields = ('matricula', 'vin', 'marca', 'modelo')
    list_filter = ('marca', 'modelo')
    readonly_fields = ('created_at', 'updated_at')


# @admin.register(Vehiculo)
# class VehiculoAdmin(admin.ModelAdmin):
#     list_display = ('cliente', 'marca', 'modelo', 'matricula', 'is_active')
#     search_fields = ('matricula', 'vin', 'marca', 'modelo')
#     list_filter = ('marca', 'modelo')
#     readonly_fields = ('created_at', 'updated_at')


# Filtro personalizado para Órdenes de Trabajo activas
class ActiveOrderFilter(admin.SimpleListFilter):
    title = 'Estado de Orden'
    parameter_name = 'estado_activo'

    def lookups(self, request, model_admin):
        return [
            ('completada', 'Completada'),
            ('pendiente', 'Pendiente'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'completada':
            return queryset.filter(estado='completada')
        if self.value() == 'pendiente':
            return queryset.exclude(estado='completada')


# Recurso para la Orden de Trabajo
class OrdenDeTrabajoResource(resources.ModelResource):
    cliente_nombre = fields.Field(
        column_name='cliente',
        attribute='cliente',
        widget=ForeignKeyWidget(Cliente, 'nombre_completo'))
    
    # Campo para listar los servicios realizados.
    # El método 'dehydrate_servicios_realizados' manejará la lógica de exportación.
    servicios_realizados = fields.Field(column_name='servicios_realizados')
    
    def dehydrate_servicios_realizados(self, obj):
        # Esta función convierte la lista de servicios en una cadena de texto.
        return ', '.join([s.titulo_pestaña for s in obj.servicios_realizados.all()])
        
    class Meta:
        model = OrdenDeTrabajo
        # Exportar todos los campos excepto 'imagen_ot' y 'fichero_ot'.
        exclude = ('imagen_ot', 'fichero_ot')
        # También puedes usar 'fields' para una lista explícita.
        # fields = ('id', 'cliente', 'vehiculo', 'descripcion_problema', 'estado', 'fecha_entrada', 'fecha_salida_estimada', 'factura', 'created_at', 'updated_at', 'is_active')

# Administración de la Orden de Trabajo con exportación
@admin.register(OrdenDeTrabajo)
class OrdenDeTrabajoAdmin(ImportExportModelAdmin):
    resource_class = OrdenDeTrabajoResource
    list_display = ('id', 'cliente', 'vehiculo', 'estado', 'fecha_entrada', 'is_active')
    #list_filter = ('estado', 'fecha_entrada', 'is_active')
    list_filter = (ActiveOrderFilter, 'fecha_entrada')
    search_fields = ('cliente__nombre_completo', 'vehiculo', 'descripcion_problema')
    readonly_fields = ('created_at', 'updated_at')
    
    # Aquí es donde van los fieldsets, dentro de la clase
    fieldsets = (
        (None, {
            'fields': ('cliente', 'vehiculo', 'descripcion_problema')
        }),
        ('Detalles del servicio', {
            'fields': ('servicios_realizados', 'estado', 'fecha_entrada', 'fecha_salida_estimada')
        }),
        ('Facturación', {
            'fields': ('factura',)
        }),
    )


# @admin.register(OrdenDeTrabajo)
# class OrdenDeTrabajoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cliente', 'vehiculo', 'estado', 'fecha_entrada', 'factura')
#     list_filter = ('estado', 'fecha_entrada')
#     search_fields = ('cliente__nombre_completo', 'vehiculo')
#     readonly_fields = ('created_at', 'updated_at')
    
#     fieldsets = (
#         (None, {
#             'fields': ('cliente', 'vehiculo', 'descripcion_problema')
#         }),
#         ('Detalles del servicio', {
#             'fields': ('servicios_realizados', 'estado', 'fecha_entrada', 'fecha_salida_estimada')
#         }),
#         ('Facturación', {
#             'fields': ('factura',)
#         }),
#     )


# Recurso para el Cliente
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        # Exporta todos los campos del modelo por defecto.
        exclude = ('imagen_cliente', 'fichero_cliente') # Excluye los campos de archivo

# Administración del Cliente con exportación
@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClienteResource
    list_display = ('nombre_completo', 'email', 'telefono', 'is_active', 'created_at')
    search_fields = ('nombre_completo', 'email', 'telefono')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')



# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ('nombre_completo', 'email', 'telefono', 'created_at', 'is_active')
#     search_fields = ('nombre_completo', 'email', 'telefono')
#     list_filter = ('created_at',)
#     readonly_fields = ('created_at', 'updated_at')


# Acción para reponer stock
@admin.action(description='Reponer stock a 10 unidades')
def reponer_stock(modeladmin, request, queryset):
    for articulo in queryset:
        articulo.stock = 10
        articulo.save()



class FacturaCompraResource(resources.ModelResource):
    class Meta:
        model = FacturaCompra

# 1. Crea una clase Resource para el modelo Articulo
class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo
        #fields = ('id', 'nombre', 'referencia', 'precio_costo', 'precio_venta', 'stock') # Omitir campos que no quieres

# 2. Modifica la clase Admin para usar ImportExportModelAdmin
@admin.register(Articulo)
class ArticuloAdmin(ImportExportModelAdmin): # ¡Cambia de admin.ModelAdmin!
    resource_class = ArticuloResource
    list_display = ('nombre', 'referencia', 'precio_costo', 'precio_venta', 'stock')
    search_fields = ('nombre', 'referencia')
    list_filter = ('stock',)
    readonly_fields = ('created_at', 'updated_at')
    actions = [reponer_stock]

# 1. Configuración de la gestión de Artículos (Inventario)
# @admin.register(Articulo)
# class ArticuloAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'referencia', 'precio_costo', 'precio_venta', 'stock')
#     search_fields = ('nombre', 'referencia')
#     list_filter = ('stock',)
#     readonly_fields = ('created_at', 'updated_at')

@admin.register(FacturaCompra)
class FacturaCompraAdmin(ImportExportModelAdmin): # Hereda de ImportExportModelAdmin
    resource_class = FacturaCompraResource # Asigna el recurso
    list_display = ('numero_factura', 'proveedor', 'fecha', 'total_monto')
    search_fields = ('numero_factura', 'proveedor')
    list_filter = ('fecha',)
    readonly_fields = ('created_at', 'updated_at')




# 2. Configuración de la gestión de Facturas de Compra
# @admin.register(FacturaCompra)
# class FacturaCompraAdmin(admin.ModelAdmin):
#     list_display = ('numero_factura', 'proveedor', 'fecha', 'total_monto')
#     search_fields = ('numero_factura', 'proveedor')
#     list_filter = ('fecha',)
#     readonly_fields = ('created_at', 'updated_at')

# 3. Configuración de la gestión de Facturas de Venta
# Usamos un 'inline' para las líneas de factura
class LineaFacturaVentaInline(admin.TabularInline):
    model = LineaFacturaVenta
    extra = 1 # Muestra un campo vacío para añadir una nueva línea
    readonly_fields = ('created_at', 'updated_at')
    

# 1. Recurso para las Líneas de Factura (la clave para conectar todo)
class LineaFacturaVentaResource(resources.ModelResource):
    # articulo_nombre = fields.Field(
    #     column_name='articulo',
    #     attribute='articulo',
    #     widget=ForeignKeyWidget(Articulo, 'nombre'))
    
    class Meta:
        model = LineaFacturaVenta
        #fields = ('id', 'factura', 'articulo_nombre', 'cantidad', 'precio_unitario')
        
# 2. Recurso para la Factura de Venta (para una exportación básica de la factura)
class FacturaVentaResource(resources.ModelResource):
    class Meta:
        model = FacturaVenta
        #fields = ('id', 'cliente', 'fecha', 'total_monto')
        
# 3. Modifica la clase Admin de FacturaVenta
@admin.register(FacturaVenta)
class FacturaVentaAdmin(ImportExportModelAdmin):
    resource_class = FacturaVentaResource
    list_display = ('id', 'cliente', 'fecha', 'total_monto')
    list_filter = ('fecha',)
    search_fields = ('cliente',)
    readonly_fields = ('total_monto','created_at', 'updated_at')
    # Opcionalmente, aún puedes mantener el inline para la edición
    inlines = [LineaFacturaVentaInline] 
    

# @admin.register(FacturaVenta)
# class FacturaVentaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cliente', 'fecha', 'total_monto')
#     list_filter = ('fecha',)
#     search_fields = ('cliente',)
#     readonly_fields = ('created_at', 'updated_at')
#     inlines = [LineaFacturaVentaInline]


class TeamMemberResource(resources.ModelResource):
    class Meta:
        model = TeamMember
        # Excluye los campos que no necesitas exportar a Excel
        exclude = ('photo', 'facebook_url', 'twitter_url', 'instagram_url')
        # También puedes usar 'fields' para una lista explícita
        # fields = ('id', 'full_name', 'email', 'phone', 'address', 'designation', 'is_active')


@admin.register(TeamMember)
class TeamMemberAdmin(ImportExportModelAdmin): # ¡Importante! Usa ImportExportModelAdmin
    resource_class = TeamMemberResource # Asigna el recurso aquí
    
    # El resto de tu configuración puede permanecer igual
    list_display = ('full_name', 'designation', 'is_active', 'created_at')
    list_filter = ('is_active', 'designation')
    search_fields = ('full_name', 'designation', 'email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'designation', 'photo', 'is_active')
        }),
        ('Información de Contacto', {
            'fields': ('email', 'phone', 'address'),
            'classes': ('collapse',),
        }),
        ('Redes Sociales', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url'),
            'classes': ('collapse',),
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


# @admin.register(TeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     # Campos que se mostrarán en la lista de miembros del equipo
#     list_display = ('full_name', 'designation', 'is_active', 'created_at')
    
#     # Añade filtros para buscar por estado (activo/inactivo)
#     list_filter = ('is_active', 'designation')
    
#     # Agrega una barra de búsqueda que busca en estos campos
#     search_fields = ('full_name', 'designation', 'email')
    
#     # Campos que no se podrán editar
#     readonly_fields = ('created_at', 'updated_at')
    
#     # Agrupa los campos en el formulario de edición
#     fieldsets = (
#         (None, {
#             'fields': ('full_name', 'designation', 'photo', 'is_active')
#         }),
#         ('Información de Contacto', {
#             'fields': ('email', 'phone', 'address'),
#             'classes': ('collapse',), # Esto colapsará la sección por defecto
#         }),
#         ('Redes Sociales', {
#             'fields': ('facebook_url', 'twitter_url', 'instagram_url'),
#             'classes': ('collapse',), # Esto colapsará la sección por defecto
#         }),
#         ('Fechas del Sistema', {
#             'fields': ('created_at', 'updated_at'),
#             'classes': ('collapse',), # Esto colapsará la sección por defecto
#         }),
#     )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista de mensajes
    list_display = ('name', 'email', 'subject', 'creado_el', 'es_activo')
    
    # Añade un campo de búsqueda por nombre y email
    search_fields = ('name', 'email', 'subject')
    
    # Agrega filtros para un fácil acceso
    list_filter = ('creado_el', 'es_activo')
    
    # Ordena los mensajes por fecha de creación de forma descendente
    ordering = ('-creado_el',)
    
    # Campos que no se pueden editar en la vista de detalle
    readonly_fields = ('creado_el', 'modificado_el')
    
    # Personaliza el formulario de detalle
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'subject', 'message')
        }),
        ('Detalles del sistema', {
            'fields': ('es_activo', 'creado_el', 'modificado_el'),
            'classes': ('collapse',),  # Opcional: para que esta sección esté colapsada
        }),
    )

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'email',
        'phone',
        'servicio',
        'fecha_servicio',
        'solicitud_especial',
        'creado_el',
    )
    search_fields = ('nombre', 'email', 'phone', 'servicio__titulo_pestaña')
    list_filter = ('servicio', 'fecha_servicio')
    ordering = ('-creado_el',)
    
    
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'titulo_pestaña',
        'es_activo',
        'imagen_contenido',
        'imagen_encabezado',
        'orden',
        'creado_el',
        'modificado_el'
    )
    list_editable = ('orden', 'es_activo')
    search_fields = ('titulo_pestaña', 'descripcion_corta')
    list_filter = ('es_activo',)
    readonly_fields = ('creado_el', 'modificado_el')
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('autor', 'profesion', 'servicio')
    search_fields = ('autor', 'texto')
    list_filter = ('servicio', 'profesion')
    
    

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('titlo', 'subtitlo', 'es_activo', 'creado_el', 'modificado_el')
    list_filter = ('es_activo', 'creado_el')
    search_fields = ('titlo', 'subtitlo')
    date_hierarchy = 'creado_el'

    fieldsets = (
        (None, {
            'fields': ('titlo', 'subtitlo', 'es_activo')
        }),
        ('Contenido del Carrusel', {
            'fields': ('imagen', 'imagen_principal', 'saber_mas_link'),
        }),
        ('Información de Tiempos', {
            'fields': ('creado_el', 'modificado_el'),
        }),
    )

    readonly_fields = ('creado_el', 'modificado_el')

admin.site.register(CarouselItem, CarouselItemAdmin)