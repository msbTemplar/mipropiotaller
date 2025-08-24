from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from datetime import datetime, time
import locale
from django.core.mail import send_mail
from .models import CarouselItem, Service, Testimonial, Booking, ContactMessage, TeamMember, FacturaVenta  
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives # Permite enviar HTML y texto plano
from django.template.loader import render_to_string # Permite renderizar plantillas
#import datetime
from .forms import TestimonialForm
from django.db.models import Sum
from django.utils import timezone

# Create your views here.




def home(request):
    carousel_items = CarouselItem.objects.all().order_by('id')
    testimonios = Testimonial.objects.all().order_by('-id') # Ordena por ID descendente para mostrar los más nuevos primero
    
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'carousel_items': carousel_items,
        'testimonios': testimonios
    }
    return render(request, 'cars_repairs_app/home.html', context)


def about(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    return render(request, 'cars_repairs_app/about.html', context)


def services(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        servicio_id = request.POST.get('servicio')
        fecha_servicio_str = request.POST.get('fecha_servicio')
        solicitud_especial = request.POST.get('solicitud_especial')

        if not all([nombre, email, servicio_id, fecha_servicio_str]):
            messages.error(request, "Error: Por favor, complete todos los campos requeridos.")
            return redirect('services')

        try:
            servicio_obj = Service.objects.get(id=servicio_id)
            fecha_servicio_obj = datetime.strptime(fecha_servicio_str, '%m/%d/%Y')
            fecha_con_hora = datetime.combine(fecha_servicio_obj, time.min)

            Booking.objects.create(
                nombre=nombre,
                email=email,
                phone=phone,
                servicio=servicio_obj,
                fecha_servicio=fecha_con_hora,
                solicitud_especial=solicitud_especial
            )

            try:
                # 1. Correo para el cliente (HTML)
                contexto_email_cliente = {
                    'nombre': nombre,
                    'servicio': servicio_obj,
                    'fecha_servicio': fecha_servicio_str,
                    'solicitud_especial': solicitud_especial,
                }
                subject_cliente = '✅ Confirmación de tu reserva en nuestro servicio'
                html_content_cliente = render_to_string('cars_repairs_app/emails/email_confirmacion.html', contexto_email_cliente)
                text_content_cliente = f'Hola {nombre}, gracias por tu reserva. Hemos recibido tu solicitud para el servicio de "{servicio_obj.titulo_pestaña}" en la fecha {fecha_servicio_str}.'

                msg_cliente = EmailMultiAlternatives(subject_cliente, text_content_cliente, settings.EMAIL_HOST_USER, [email])
                msg_cliente.attach_alternative(html_content_cliente, "text/html")
                msg_cliente.send()

                # 2. Correo para el administrador (HTML con tabla)
                contexto_email_admin = {
                    'nombre': nombre,
                    'email': email,
                    'phone': phone,
                    'servicio': servicio_obj,
                    'fecha_servicio': fecha_servicio_str,
                    'solicitud_especial': solicitud_especial,
                }
                subject_admin = '🔔 ¡Nueva reserva recibida!'
                html_content_admin = render_to_string('cars_repairs_app/emails/email_admin.html', contexto_email_admin)
                text_content_admin = f"""¡Hola Administrador! Se ha recibido una nueva reserva.
                                        Nombre: {nombre}
                                        Email: {email}
                                        Teléfono: {phone}
                                        Servicio: {servicio_obj.titulo_pestaña}
                                        Fecha: {fecha_servicio_str}
                                        Solicitud Especial: {solicitud_especial}"""

                msg_admin = EmailMultiAlternatives(subject_admin, text_content_admin, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL])
                msg_admin.attach_alternative(html_content_admin, "text/html")
                msg_admin.send()

            except Exception as e:
                messages.error(request, f"❌ La reserva se guardó, pero hubo un error al enviar el correo: {e}")

            messages.success(request, "✅ ¡Tu reserva ha sido enviada con éxito! Revisa tu correo electrónico para la confirmación.")
            return redirect('services')

        except Service.DoesNotExist:
            messages.error(request, "❌ Error: El servicio seleccionado no es válido.")
            return redirect('services')
        except ValueError:
            messages.error(request, "❌ Error: El formato de fecha es inválido. Por favor, use MM/DD/YYYY.")
            return redirect('services')
        except Exception as e:
            messages.error(request, f"❌ Ocurrió un error inesperado: {e}")
            return redirect('services')

    else:
        services = Service.objects.filter(es_activo=True).order_by('orden')
        testimonials = Testimonial.objects.all()

        fecha_actual = datetime.now().strftime('%A, %B %d, %Y')
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y')
        except locale.Error:
            fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
        
        fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
        
        context = {
            'fecha_actual': fecha_actual,
            'fecha_actual_es': fecha_actual_es,
            'fecha_hora_actual': fecha_hora_actual,
            'services': services,
            'testimonials': testimonials
        }
        return render(request, 'cars_repairs_app/service.html', context)



def services_sin_email(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        servicio_id = request.POST.get('servicio')
        fecha_servicio_str = request.POST.get('fecha_servicio')
        solicitud_especial = request.POST.get('solicitud_especial')
        
        # Validación de campos vacíos
        if not all([nombre, email, servicio_id, fecha_servicio_str]):
            messages.error(request, "Error: Por favor, complete todos los campos requeridos.")
            return redirect('services')  # Redirige a la misma página
            
        try:
            servicio_obj = Service.objects.get(id=servicio_id)
            fecha_servicio_obj = datetime.strptime(fecha_servicio_str, '%m/%d/%Y')
            fecha_con_hora = datetime.combine(fecha_servicio_obj, time.min)
            
            Booking.objects.create(
                nombre=nombre,
                email=email,
                servicio=servicio_obj,
                fecha_servicio=fecha_con_hora,
                solicitud_especial=solicitud_especial
            )
            
            messages.success(request, "✅ ¡Tu reserva ha sido enviada con éxito! Te contactaremos pronto.")
            return redirect('services')  # Redirige a la misma página después del éxito
            
        except Service.DoesNotExist:
            messages.error(request, "❌ Error: El servicio seleccionado no es válido.")
            return redirect('services')
        except ValueError:
            messages.error(request, "❌ Error: El formato de fecha es inválido. Por favor, use MM/DD/YYYY.")
            return redirect('services')
        except Exception as e:
            messages.error(request, f"❌ Ocurrió un error inesperado: {e}")
            return redirect('services')
    else:
        services = Service.objects.filter(es_activo=True).order_by('orden')
        testimonials = Testimonial.objects.all()

        fecha_actual = datetime.now().strftime('%A, %B %d, %Y')
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y')
        except locale.Error:
            fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
        
        fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
        
        context = {
            'fecha_actual': fecha_actual,
            'fecha_actual_es': fecha_actual_es,
            'fecha_hora_actual': fecha_hora_actual,
            'services': services,
            'testimonials': testimonials
        }
        return render(request, 'cars_repairs_app/service.html', context)

def services1(request):
    services = Service.objects.filter(es_activo=True).order_by('orden')
    testimonials = Testimonial.objects.all()  # Obtén todos los testimonios

    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y')
    except locale.Error:
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'services': services,
        'testimonials': testimonials  # Añade los testimonios al contexto
    }
    return render(request, 'cars_repairs_app/service.html', context)


def booking(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    return render(request, 'cars_repairs_app/booking.html', context)


def team(request):
    # Obtiene todos los miembros del equipo que estén activos
    # y los ordena por el campo 'full_name'
    team_members = TeamMember.objects.filter(is_active=True).order_by('full_name')

    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')
    
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y')
    except locale.Error:
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    
    context = {
        'team_members': team_members, # ¡Aquí se añade la lista de miembros del equipo!
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    
    return render(request, 'cars_repairs_app/team.html', context)


def testimonial(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial_instance = form.save(commit=False)
            # Aquí puedes asignar campos adicionales, por ejemplo, el usuario actual si estuviera autenticado
            # testimonial_instance.autor = request.user.username 
            testimonial_instance.save()
            return redirect('testimonial')  # Redirige a la misma página para evitar reenvío de formulario

    else:
        form = TestimonialForm()

    # Obtener todos los testimonios de la base de datos
    testimonios = Testimonial.objects.all().order_by('-id') # Ordena por ID descendente para mostrar los más nuevos primero
    
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual,
        'form': form,
        'testimonios': testimonios,
    }
    return render(request, 'cars_repairs_app/testimonial.html', context)


def page404(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    return render(request, 'cars_repairs_app/404.html', context)


def contact(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    return render(request, 'cars_repairs_app/contact.html', context)



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, subject, message]):
            messages.error(request, "❌ Por favor, complete todos los campos requeridos.")
            return redirect('contact_page')

        try:
            # Guarda el mensaje en la base de datos
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            
            try:
                # 1. Prepara el correo para el cliente
                contexto_cliente = {
                    'recipient_type': 'client',
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'subject': subject,
                    'message': message,
                }
                html_cliente = render_to_string('cars_repairs_app/emails/email_contacto.html', contexto_cliente)
                text_cliente = f'Hola {name}, hemos recibido tu mensaje. Asunto: {subject}'
                
                msg_cliente = EmailMultiAlternatives('Confirmación de tu mensaje', text_cliente, settings.EMAIL_HOST_USER, [email])
                msg_cliente.attach_alternative(html_cliente, "text/html")
                msg_cliente.send()

                # 2. Prepara el correo para el administrador
                contexto_admin = {
                    'recipient_type': 'admin',
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'subject': subject,
                    'message': message,
                }
                html_admin = render_to_string('cars_repairs_app/emails/email_contacto.html', contexto_admin)
                text_admin = f'Nuevo mensaje de contacto de {name}. Asunto: {subject}'
                
                msg_admin = EmailMultiAlternatives('Nuevo mensaje de contacto', text_admin, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL])
                msg_admin.attach_alternative(html_admin, "text/html")
                msg_admin.send()
                
            except Exception as e:
                messages.error(request, f"❌ El mensaje se guardó, pero hubo un error al enviar el correo: {e}")

            messages.success(request, "✅ ¡Tu mensaje ha sido enviado con éxito! Revisa tu correo electrónico para la confirmación.")
            return redirect('contact_page')
        
        except Exception as e:
            messages.error(request, f"❌ Ocurrió un error inesperado al enviar tu mensaje: {e}")
            return redirect('contact_page')
    
    return render(request, 'cars_repairs_app/contact.html')




def custom_logout_view(request):
    logout(request)
    return redirect('home') 
