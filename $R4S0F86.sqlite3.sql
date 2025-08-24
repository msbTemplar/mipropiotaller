BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_carouselitem" (
	"id"	integer NOT NULL,
	"titlo"	varchar(200),
	"subtitlo"	varchar(200),
	"imagen"	varchar(100),
	"imagen_principal"	varchar(100),
	"saber_mas_link"	varchar(200),
	"es_activo"	bool NOT NULL,
	"creado_el"	datetime NOT NULL,
	"modificado_el"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_service" (
	"id"	integer NOT NULL,
	"icono_fa"	varchar(50),
	"titulo_contenido"	varchar(200),
	"imagen_contenido"	varchar(100),
	"descripcion_corta"	text,
	"puntos_lista"	text,
	"imagen_encabezado"	varchar(100),
	"titulo_booking"	varchar(200),
	"descripcion_booking"	text,
	"orden"	integer,
	"es_activo"	bool NOT NULL,
	"creado_el"	datetime NOT NULL,
	"modificado_el"	datetime NOT NULL,
	"titulo_pestaña"	varchar(100),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_testimonial" (
	"id"	integer NOT NULL,
	"autor"	varchar(100),
	"profesion"	varchar(100),
	"imagen"	varchar(100),
	"servicio_id"	bigint NOT NULL,
	"texto"	text,
	FOREIGN KEY("servicio_id") REFERENCES "cars_repairs_app_service"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_booking" (
	"id"	integer NOT NULL,
	"nombre"	varchar(100) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"fecha_servicio"	datetime NOT NULL,
	"solicitud_especial"	text,
	"creado_el"	datetime NOT NULL,
	"servicio_id"	bigint,
	"phone"	varchar(100),
	FOREIGN KEY("servicio_id") REFERENCES "cars_repairs_app_service"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_contactmessage" (
	"id"	integer NOT NULL,
	"name"	varchar(100) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"phone"	varchar(100),
	"subject"	varchar(255) NOT NULL,
	"message"	text NOT NULL,
	"es_activo"	bool NOT NULL,
	"creado_el"	datetime NOT NULL,
	"modificado_el"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_teammember" (
	"id"	integer NOT NULL,
	"full_name"	varchar(100),
	"email"	varchar(254),
	"phone"	varchar(100),
	"address"	text,
	"designation"	varchar(100) NOT NULL,
	"photo"	varchar(100),
	"facebook_url"	varchar(200),
	"twitter_url"	varchar(200),
	"instagram_url"	varchar(200),
	"is_active"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_articulo" (
	"id"	integer NOT NULL,
	"nombre"	varchar(200) NOT NULL,
	"referencia"	varchar(100) NOT NULL UNIQUE,
	"precio_costo"	decimal NOT NULL,
	"precio_venta"	decimal NOT NULL,
	"stock"	integer NOT NULL,
	"is_active"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_facturacompra" (
	"id"	integer NOT NULL,
	"proveedor"	varchar(200) NOT NULL,
	"numero_factura"	varchar(100) NOT NULL UNIQUE,
	"fecha"	date NOT NULL,
	"total_monto"	decimal NOT NULL,
	"imagen_factura"	varchar(5500),
	"fichero_factura"	varchar(5500),
	"is_active"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_facturaventa" (
	"id"	integer NOT NULL,
	"cliente"	varchar(200) NOT NULL,
	"fecha"	date NOT NULL,
	"total_monto"	decimal NOT NULL,
	"imagen_factura"	varchar(5500),
	"fichero_factura"	varchar(5500),
	"is_active"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_lineafacturaventa" (
	"id"	integer NOT NULL,
	"cantidad"	integer unsigned NOT NULL CHECK("cantidad" >= 0),
	"precio_unitario"	decimal NOT NULL,
	"imagen_factura"	varchar(5500),
	"fichero_factura"	varchar(5500),
	"is_active"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"articulo_id"	bigint NOT NULL,
	"factura_id"	bigint NOT NULL,
	FOREIGN KEY("articulo_id") REFERENCES "cars_repairs_app_articulo"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("factura_id") REFERENCES "cars_repairs_app_facturaventa"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_cliente" (
	"id"	integer NOT NULL,
	"nombre_completo"	varchar(200) NOT NULL,
	"email"	varchar(254),
	"telefono"	varchar(50),
	"direccion"	text,
	"imagen_cliente"	varchar(5500),
	"fichero_cliente"	varchar(5500),
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"is_active"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_ordendetrabajo" (
	"id"	integer NOT NULL,
	"vehiculo"	varchar(200) NOT NULL,
	"descripcion_problema"	text NOT NULL,
	"estado"	varchar(50) NOT NULL,
	"fecha_entrada"	date NOT NULL,
	"fecha_salida_estimada"	date,
	"imagen_ot"	varchar(5500),
	"fichero_ot"	varchar(5500),
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"is_active"	bool NOT NULL,
	"cliente_id"	bigint NOT NULL,
	"factura_id"	bigint UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("factura_id") REFERENCES "cars_repairs_app_facturaventa"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("cliente_id") REFERENCES "cars_repairs_app_cliente"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "cars_repairs_app_ordendetrabajo_servicios_realizados" (
	"id"	integer NOT NULL,
	"ordendetrabajo_id"	bigint NOT NULL,
	"service_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ordendetrabajo_id") REFERENCES "cars_repairs_app_ordendetrabajo"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("service_id") REFERENCES "cars_repairs_app_service"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2025-08-23 10:53:54.834504'),
 (2,'auth','0001_initial','2025-08-23 10:53:54.864500'),
 (3,'admin','0001_initial','2025-08-23 10:53:54.907504'),
 (4,'admin','0002_logentry_remove_auto_add','2025-08-23 10:53:54.931502'),
 (5,'admin','0003_logentry_add_action_flag_choices','2025-08-23 10:53:54.945504'),
 (6,'contenttypes','0002_remove_content_type_name','2025-08-23 10:53:54.980539'),
 (7,'auth','0002_alter_permission_name_max_length','2025-08-23 10:53:55.003512'),
 (8,'auth','0003_alter_user_email_max_length','2025-08-23 10:53:55.021508'),
 (9,'auth','0004_alter_user_username_opts','2025-08-23 10:53:55.034508'),
 (10,'auth','0005_alter_user_last_login_null','2025-08-23 10:53:55.059506'),
 (11,'auth','0006_require_contenttypes_0002','2025-08-23 10:53:55.064502'),
 (12,'auth','0007_alter_validators_add_error_messages','2025-08-23 10:53:55.085507'),
 (13,'auth','0008_alter_user_username_max_length','2025-08-23 10:53:55.204514'),
 (14,'auth','0009_alter_user_last_name_max_length','2025-08-23 10:53:55.224503'),
 (15,'auth','0010_alter_group_name_max_length','2025-08-23 10:53:55.241505'),
 (16,'auth','0011_update_proxy_permissions','2025-08-23 10:53:55.252504'),
 (17,'auth','0012_alter_user_first_name_max_length','2025-08-23 10:53:55.269510'),
 (18,'cars_repairs_app','0001_initial','2025-08-23 10:53:55.277505'),
 (19,'sessions','0001_initial','2025-08-23 10:53:55.288502'),
 (20,'cars_repairs_app','0002_service','2025-08-23 11:38:34.601932'),
 (21,'cars_repairs_app','0003_remove_service_testimonial_autor_and_more','2025-08-23 11:51:11.792320'),
 (22,'cars_repairs_app','0004_alter_service_descripcion_corta_and_more','2025-08-23 15:54:40.935113'),
 (23,'cars_repairs_app','0005_booking_phone','2025-08-23 17:00:25.472978'),
 (24,'cars_repairs_app','0006_contactmessage','2025-08-23 17:18:09.447921'),
 (25,'cars_repairs_app','0007_teammember','2025-08-23 17:43:06.233414'),
 (26,'cars_repairs_app','0008_articulo_facturacompra_facturaventa_and_more','2025-08-24 07:38:48.858828'),
 (27,'cars_repairs_app','0009_cliente_ordendetrabajo','2025-08-24 08:13:48.754613');
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (1,'1','titulo: Car Servicing - Qualified Car Repair Service Center - None - 2025-08-23 11:16:45.455820+00:00',1,'[{"added": {}}]',7,1,'2025-08-23 11:16:45.458821'),
 (2,'2','titulo: Car Servicing - Qualified Car Wash Service Center - None - 2025-08-23 11:17:30.310170+00:00',1,'[{"added": {}}]',7,1,'2025-08-23 11:17:30.312166'),
 (3,'1','titulo: Car Servicing - Qualified Car Repair Service Center - None - 2025-08-23 11:16:45.455820+00:00',2,'[{"changed": {"fields": ["Imagen", "Imagen principal"]}}]',7,1,'2025-08-23 11:24:25.008709'),
 (4,'2','titulo: Car Servicing - Qualified Car Wash Service Center - None - 2025-08-23 11:17:30.310170+00:00',2,'[{"changed": {"fields": ["Imagen", "Imagen principal"]}}]',7,1,'2025-08-23 11:24:38.775824'),
 (5,'1','Diagnostic Test',1,'[{"added": {}}]',8,1,'2025-08-23 12:14:18.391412'),
 (6,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Titulo booking", "Descripcion booking"]}}]',8,1,'2025-08-23 12:16:24.207907'),
 (7,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 12:18:42.970526'),
 (8,'2','Engine Servicing',1,'[{"added": {}}]',8,1,'2025-08-23 12:20:01.174503'),
 (9,'3','Tires Replacement',1,'[{"added": {}}]',8,1,'2025-08-23 12:21:15.621983'),
 (10,'4','Oil Changing',1,'[{"added": {}}]',8,1,'2025-08-23 12:22:15.861778'),
 (11,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 12:22:25.283692'),
 (12,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:01:54.753191'),
 (13,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:03:02.864771'),
 (14,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:15:30.816636'),
 (15,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:15:37.577738'),
 (16,'3','Tires Replacement',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:15:42.806523'),
 (17,'2','Engine Servicing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:15:47.662423'),
 (18,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 13:15:50.919316'),
 (19,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:18:05.095762'),
 (20,'2','Engine Servicing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:18:10.083667'),
 (21,'3','Tires Replacement',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:18:14.995162'),
 (22,'4','Oil Changing',2,'[]',8,1,'2025-08-23 13:18:19.576228'),
 (23,'3','Tires Replacement',2,'[]',8,1,'2025-08-23 13:18:22.877212'),
 (24,'2','Engine Servicing',2,'[]',8,1,'2025-08-23 13:18:25.766368'),
 (25,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:18:30.896290'),
 (26,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:38:56.671923'),
 (27,'4','Oil Changing',2,'[]',8,1,'2025-08-23 13:39:02.244741'),
 (28,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:41:49.927249'),
 (29,'2','Engine Servicing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:41:55.186301'),
 (30,'3','Tires Replacement',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:42:00.344173'),
 (31,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:42:05.734104'),
 (32,'4','Oil Changing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:47:01.493085'),
 (33,'3','Tires Replacement',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:47:08.516782'),
 (34,'2','Engine Servicing',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:47:15.506753'),
 (35,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Puntos lista"]}}]',8,1,'2025-08-23 13:47:22.460738'),
 (36,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 13:53:40.496177'),
 (37,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 13:55:20.151498'),
 (38,'4','Oil Changing',2,'[]',8,1,'2025-08-23 13:55:32.231791'),
 (39,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 13:55:38.594252'),
 (40,'2','Engine Servicing',2,'[{"changed": {"fields": ["Imagen contenido"]}}]',8,1,'2025-08-23 13:55:52.007792'),
 (41,'3','Tires Replacement',2,'[{"changed": {"fields": ["Imagen contenido"]}}]',8,1,'2025-08-23 13:56:00.318938'),
 (42,'4','Oil Changing',2,'[{"changed": {"fields": ["Imagen encabezado"]}}]',8,1,'2025-08-23 13:56:11.485975'),
 (43,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Orden"]}}]',8,1,'2025-08-23 13:57:09.246453'),
 (44,'2','Engine Servicing',2,'[{"changed": {"fields": ["Orden"]}}]',8,1,'2025-08-23 13:57:14.983390'),
 (45,'3','Tires Replacement',2,'[{"changed": {"fields": ["Orden"]}}]',8,1,'2025-08-23 13:57:19.718588'),
 (46,'4','Oil Changing',2,'[{"changed": {"fields": ["Orden"]}}]',8,1,'2025-08-23 13:57:24.781911'),
 (47,'4','Oil Changing',2,'[]',8,1,'2025-08-23 13:58:14.734059'),
 (48,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Imagen encabezado"]}}]',8,1,'2025-08-23 14:08:56.585812'),
 (49,'2','Engine Servicing',2,'[{"changed": {"fields": ["Imagen encabezado"]}}]',8,1,'2025-08-23 14:09:05.241835'),
 (50,'3','Tires Replacement',2,'[{"changed": {"fields": ["Imagen encabezado"]}}]',8,1,'2025-08-23 14:09:21.677676'),
 (51,'4','Oil Changing',2,'[{"changed": {"fields": ["Imagen contenido"]}}]',8,1,'2025-08-23 14:09:32.628627'),
 (52,'1','Diagnostic Test',2,'[]',8,1,'2025-08-23 14:10:45.227718'),
 (53,'1','Testimonio de Client Name para Diagnostic Test',1,'[{"added": {}}]',9,1,'2025-08-23 15:39:42.018119'),
 (54,'2','Testimonio de Client Name para Engine Servicing',1,'[{"added": {}}]',9,1,'2025-08-23 15:40:11.561136'),
 (55,'3','Testimonio de Client Name para Tires Replacement',1,'[{"added": {}}]',9,1,'2025-08-23 15:40:27.458640'),
 (56,'4','Testimonio de Client Name para Oil Changing',1,'[{"added": {}}]',9,1,'2025-08-23 15:40:39.865377'),
 (57,'1','Diagnostic Test',2,'[{"changed": {"fields": ["Imagen encabezado"]}}]',8,1,'2025-08-23 15:43:36.991821'),
 (58,'1','Full Name',1,'[{"added": {}}]',12,1,'2025-08-23 17:48:06.223413'),
 (59,'2','Full Name',1,'[{"added": {}}]',12,1,'2025-08-23 17:48:21.008075'),
 (60,'3','Full Name',1,'[{"added": {}}]',12,1,'2025-08-23 17:48:29.770776'),
 (61,'4','Full Name',1,'[{"added": {}}]',12,1,'2025-08-23 17:48:37.871571'),
 (62,'1','tornillo',1,'[{"added": {}}]',15,1,'2025-08-24 07:52:31.860828'),
 (63,'2','Martillo',1,'[{"added": {}}]',15,1,'2025-08-24 07:53:04.945808'),
 (64,'1','Factura para Cliente 1 del 2025-08-24',1,'[{"added": {}}, {"added": {"name": "linea factura venta", "object": "3 x tornillo"}}, {"added": {"name": "linea factura venta", "object": "4 x Martillo"}}]',16,1,'2025-08-24 07:54:29.433738'),
 (65,'1','Factura AG-es-234 de el de los tornillos',1,'[{"added": {}}]',13,1,'2025-08-24 08:03:07.731153'),
 (66,'2','Factura ES-ASD-456 de el de la sruedas',1,'[{"added": {}}]',13,1,'2025-08-24 08:03:39.890623'),
 (67,'1','Cliente 1',1,'[{"added": {}}]',17,1,'2025-08-24 08:22:58.419492'),
 (68,'2','Cliente 11',1,'[{"added": {}}]',17,1,'2025-08-24 08:23:20.869850'),
 (69,'1','Orden de Trabajo #1 - Cliente 1',1,'[{"added": {}}]',18,1,'2025-08-24 08:25:20.780709'),
 (70,'2','Orden de Trabajo #2 - Cliente 11',1,'[{"added": {}}]',18,1,'2025-08-24 08:25:43.240080');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'cars_repairs_app','carouselitem'),
 (8,'cars_repairs_app','service'),
 (9,'cars_repairs_app','testimonial'),
 (10,'cars_repairs_app','booking'),
 (11,'cars_repairs_app','contactmessage'),
 (12,'cars_repairs_app','teammember'),
 (13,'cars_repairs_app','facturacompra'),
 (14,'cars_repairs_app','lineafacturaventa'),
 (15,'cars_repairs_app','articulo'),
 (16,'cars_repairs_app','facturaventa'),
 (17,'cars_repairs_app','cliente'),
 (18,'cars_repairs_app','ordendetrabajo');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_carouselitem','Can add Carousel Item'),
 (26,7,'change_carouselitem','Can change Carousel Item'),
 (27,7,'delete_carouselitem','Can delete Carousel Item'),
 (28,7,'view_carouselitem','Can view Carousel Item'),
 (29,8,'add_service','Can add Service'),
 (30,8,'change_service','Can change Service'),
 (31,8,'delete_service','Can delete Service'),
 (32,8,'view_service','Can view Service'),
 (33,9,'add_testimonial','Can add Testimonio'),
 (34,9,'change_testimonial','Can change Testimonio'),
 (35,9,'delete_testimonial','Can delete Testimonio'),
 (36,9,'view_testimonial','Can view Testimonio'),
 (37,10,'add_booking','Can add Booking'),
 (38,10,'change_booking','Can change Booking'),
 (39,10,'delete_booking','Can delete Booking'),
 (40,10,'view_booking','Can view Booking'),
 (41,11,'add_contactmessage','Can add contact message'),
 (42,11,'change_contactmessage','Can change contact message'),
 (43,11,'delete_contactmessage','Can delete contact message'),
 (44,11,'view_contactmessage','Can view contact message'),
 (45,12,'add_teammember','Can add team member'),
 (46,12,'change_teammember','Can change team member'),
 (47,12,'delete_teammember','Can delete team member'),
 (48,12,'view_teammember','Can view team member'),
 (49,13,'add_facturacompra','Can add factura compra'),
 (50,13,'change_facturacompra','Can change factura compra'),
 (51,13,'delete_facturacompra','Can delete factura compra'),
 (52,13,'view_facturacompra','Can view factura compra'),
 (53,14,'add_lineafacturaventa','Can add linea factura venta'),
 (54,14,'change_lineafacturaventa','Can change linea factura venta'),
 (55,14,'delete_lineafacturaventa','Can delete linea factura venta'),
 (56,14,'view_lineafacturaventa','Can view linea factura venta'),
 (57,15,'add_articulo','Can add articulo'),
 (58,15,'change_articulo','Can change articulo'),
 (59,15,'delete_articulo','Can delete articulo'),
 (60,15,'view_articulo','Can view articulo'),
 (61,16,'add_facturaventa','Can add factura venta'),
 (62,16,'change_facturaventa','Can change factura venta'),
 (63,16,'delete_facturaventa','Can delete factura venta'),
 (64,16,'view_facturaventa','Can view factura venta'),
 (65,17,'add_cliente','Can add cliente'),
 (66,17,'change_cliente','Can change cliente'),
 (67,17,'delete_cliente','Can delete cliente'),
 (68,17,'view_cliente','Can view cliente'),
 (69,18,'add_ordendetrabajo','Can add orden de trabajo'),
 (70,18,'change_ordendetrabajo','Can change orden de trabajo'),
 (71,18,'delete_ordendetrabajo','Can delete orden de trabajo'),
 (72,18,'view_ordendetrabajo','Can view orden de trabajo');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES (1,'pbkdf2_sha256$1000000$eHuRatKOxM6xxUVcGTGEo2$VQp//Evk1DTRu02BEWLftL6xm/95SRp5fywlbC6LtDU=','2025-08-24 07:27:18.422266',1,'moha','','msb.duck@gmail.com',1,1,'2025-08-23 10:54:18.086124','');
INSERT INTO "cars_repairs_app_carouselitem" ("id","titlo","subtitlo","imagen","imagen_principal","saber_mas_link","es_activo","creado_el","modificado_el") VALUES (1,'Car Servicing','Qualified Car Repair Service Center','carousel_images/carousel-bg-1_75x7TBB.jpg','carousel_images/carousel-1_XlPgv22.png',NULL,1,'2025-08-23 11:16:45.455820','2025-08-23 11:24:24.994713'),
 (2,'Car Servicing','Qualified Car Wash Service Center','carousel_images/carousel-bg-2_xEIr6l5.jpg','carousel_images/carousel-2_pqT7rX5.png',NULL,1,'2025-08-23 11:17:30.310170','2025-08-23 11:24:38.773511');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('97xn6n3yfgjkr04jfuh8dt33j5u849w0','.eJxVjMsOwiAQRf-FtSEMVB4u3fcbmmEYpGogKe3K-O_apAvd3nPOfYkJt7VMW-dlmpO4CBCn3y0iPbjuIN2x3pqkVtdljnJX5EG7HFvi5_Vw_w4K9vKts6azYgUWBmMNkHcIRnNmAE_ZASlniYCCUSEojoNlSp45o9VkcxLvD8--OCg:1upm9r:m7uc_BPxGHLNoLtNEFeEa75eDelWaASqWKGhbQPRvxY','2025-09-06 11:11:39.765128'),
 ('379mt8tjuz9y74ltr4oewovjxy8c2sm5','.eJxVjMsOwiAQRf-FtSEMVB4u3fcbmmEYpGogKe3K-O_apAvd3nPOfYkJt7VMW-dlmpO4CBCn3y0iPbjuIN2x3pqkVtdljnJX5EG7HFvi5_Vw_w4K9vKts6azYgUWBmMNkHcIRnNmAE_ZASlniYCCUSEojoNlSp45o9VkcxLvD8--OCg:1uq58I:qPxTNaWeLFMlUqnoCVXrwjubhACal_9Roz_PS8gjrwQ','2025-09-07 07:27:18.429302');
INSERT INTO "cars_repairs_app_service" ("id","icono_fa","titulo_contenido","imagen_contenido","descripcion_corta","puntos_lista","imagen_encabezado","titulo_booking","descripcion_booking","orden","es_activo","creado_el","modificado_el","titulo_pestaña") VALUES (1,'fa-car-side','15 Years Of Experience In Auto Servicing','service_images/service-1.jpg','Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet','<p>Quality Servicing<br />
Expert Workers<br />
Modern Equipment</p>','service_images/headers/carousel-bg-1.jpg','Certified and Award Winning Car Repair Service Provider','Eirmod sed tempor lorem ut dolores. Aliquyam sit sadipscing kasd ipsum. Dolor ea et dolore et at sea ea at dolor, justo ipsum duo rebum sea invidunt voluptua. Eos vero eos vero ea et dolore eirmod et. Dolores diam duo invidunt lorem. Elitr ut dolores magna sit. Sea dolore sanctus sed et. Takimata takimata sanctus sed.',1,1,'2025-08-23 12:14:18.378412','2025-08-23 15:43:36.988820','Diagnostic Test'),
 (2,'fa-car','15 Years Of Experience In Auto Servicing','service_images/service-2.jpg','2 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet','<p>Quality Servicing<br />
Expert Workers<br />
Modern Equipment</p>','service_images/headers/service-2.jpg','Certified and Award Winning Car Repair Service Provider','Eirmod sed tempor lorem ut dolores. Aliquyam sit sadipscing kasd ipsum. Dolor ea et dolore et at sea ea at dolor, justo ipsum duo rebum sea invidunt voluptua. Eos vero eos vero ea et dolore eirmod et. Dolores diam duo invidunt lorem. Elitr ut dolores magna sit. Sea dolore sanctus sed et. Takimata takimata sanctus sed.',2,1,'2025-08-23 12:20:01.172088','2025-08-23 14:09:05.227791','Engine Servicing'),
 (3,'fa-cog','15 Years Of Experience In Auto Servicing','service_images/service-3.jpg','3 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet','<p>Quality Servicing<br />
Expert Workers<br />
Modern Equipment</p>','service_images/headers/service-3.jpg','Certified and Award Winning Car Repair Service Provider','Eirmod sed tempor lorem ut dolores. Aliquyam sit sadipscing kasd ipsum. Dolor ea et dolore et at sea ea at dolor, justo ipsum duo rebum sea invidunt voluptua. Eos vero eos vero ea et dolore eirmod et. Dolores diam duo invidunt lorem. Elitr ut dolores magna sit. Sea dolore sanctus sed et. Takimata takimata sanctus sed.',3,1,'2025-08-23 12:21:15.617983','2025-08-23 14:09:21.675678','Tires Replacement'),
 (4,'fa-oil-can','15 Years Of Experience In Auto Servicing','service_images/service-4.jpg','4 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet','<p>Quality Servicing<br />
Expert Workers<br />
Modern Equipment</p>','service_images/headers/service-4.jpg','Certified and Award Winning Car Repair Service Provider','Eirmod sed tempor lorem ut dolores. Aliquyam sit sadipscing kasd ipsum. Dolor ea et dolore et at sea ea at dolor, justo ipsum duo rebum sea invidunt voluptua. Eos vero eos vero ea et dolore eirmod et. Dolores diam duo invidunt lorem. Elitr ut dolores magna sit. Sea dolore sanctus sed et. Takimata takimata sanctus sed.',4,1,'2025-08-23 12:22:15.858777','2025-08-23 14:09:32.615288','Oil Changing');
INSERT INTO "cars_repairs_app_testimonial" ("id","autor","profesion","imagen","servicio_id","texto") VALUES (1,'Client Name','Profession','testimonial_images/testimonial-1.jpg',1,'1 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit diam amet diam et eos. Clita erat ipsum et lorem et sit.'),
 (2,'Client Name','Profession','testimonial_images/testimonial-2.jpg',2,'2 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit diam amet diam et eos. Clita erat ipsum et lorem et sit.'),
 (3,'Client Name','Profession','testimonial_images/testimonial-3.jpg',3,'3 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit diam amet diam et eos. Clita erat ipsum et lorem et sit.'),
 (4,'Client Name','Profession','testimonial_images/testimonial-4.jpg',4,'4 Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit diam amet diam et eos. Clita erat ipsum et lorem et sit.'),
 (5,'<asdasdas','asdasd','testimonial_images/team-2.jpg',2,'asdasdasd'),
 (6,'ADadaD','adADadaDad','testimonial_images/team-3.jpg',4,'ADadaadA');
INSERT INTO "cars_repairs_app_booking" ("id","nombre","email","fecha_servicio","solicitud_especial","creado_el","servicio_id","phone") VALUES (1,'AAAaf','msb.caixa@gmail.com','2025-08-21 00:00:00','AFafaf','2025-08-23 16:16:51.483865',2,NULL),
 (2,'AAAaf','msb.caixa@gmail.com','2025-08-21 00:00:00','AFafaf','2025-08-23 16:17:22.766346',2,NULL),
 (3,'VBCVBCVBCBCB','msb.coin@gmail.com','2025-08-24 00:00:00','CVBCVCVCVBCBCCVB','2025-08-23 16:43:36.091784',4,NULL),
 (4,'ADAadAAD','msb.motive@gmail.com','2025-09-02 00:00:00','adaDAdaDadADadAadADD','2025-08-23 16:46:13.115185',3,NULL),
 (5,'aaaaaaaa','msb.tesla@gmail.com','2025-08-27 00:00:00','dfhdhfdhfdhfdfhdfhfdhfdhfdhfdhfh','2025-08-23 16:51:27.350524',3,NULL),
 (6,'aAdADAd','msb.motive@gmail.com','2025-08-24 00:00:00','adADadADdDa','2025-08-23 17:00:52.039941',1,NULL),
 (7,'adaAdaDAdADDada','msb.coin@gmail.com','2025-09-06 00:00:00','aDadaDadADadADAdADad','2025-08-23 17:02:30.936548',4,'adADadADadADad'),
 (8,'vvvvvvvvv','msebti2@gmail.com','2025-08-24 00:00:00','vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv','2025-08-23 17:07:37.816367',1,'vvvvvvvvvv'),
 (9,'xxxxxxxxxx','msebti2@gmail.com','2025-09-03 00:00:00','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','2025-08-23 17:10:07.576990',2,'xxxxxxxxx');
INSERT INTO "cars_repairs_app_contactmessage" ("id","name","email","phone","subject","message","es_activo","creado_el","modificado_el") VALUES (1,'dsfdssdfsdf','msebti2@gmail.com','sdfsdfdsfsdf','sdfsfsd','sdfsdfsdfsdfssdf',1,'2025-08-23 17:18:23.650683','2025-08-23 17:18:23.650683'),
 (2,'zzzzzzzzzzzzzzzzzzzzzzzzz','msebti2@gmail.com','zzzzzzzzzzzzzzzzzzzzzzzz','zzzzzzzzzzzzzzzzzz','zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',1,'2025-08-23 17:23:42.652284','2025-08-23 17:23:42.652284');
INSERT INTO "cars_repairs_app_teammember" ("id","full_name","email","phone","address","designation","photo","facebook_url","twitter_url","instagram_url","is_active","created_at","updated_at") VALUES (1,'Full Name',NULL,NULL,'','Designation','team_members/team-1.jpg',NULL,NULL,NULL,1,'2025-08-23 17:48:06.208409','2025-08-23 17:48:06.208409'),
 (2,'Full Name',NULL,NULL,'','Designation','team_members/team-2.jpg',NULL,NULL,NULL,1,'2025-08-23 17:48:21.005079','2025-08-23 17:48:21.005079'),
 (3,'Full Name',NULL,NULL,'','Designation','team_members/team-3.jpg',NULL,NULL,NULL,1,'2025-08-23 17:48:29.767779','2025-08-23 17:48:29.767779'),
 (4,'Full Name',NULL,NULL,'','Designation','team_members/team-4.jpg',NULL,NULL,NULL,1,'2025-08-23 17:48:37.868573','2025-08-23 17:48:37.868573');
INSERT INTO "cars_repairs_app_articulo" ("id","nombre","referencia","precio_costo","precio_venta","stock","is_active","created_at","updated_at") VALUES (1,'tornillo','RF-TOR_tornillo',12,13,9,1,'2025-08-24 07:52:31.858826','2025-08-24 07:52:31.858826'),
 (2,'Martillo','RF-MART-Martillo',23,25,8,1,'2025-08-24 07:53:04.939141','2025-08-24 07:53:04.939141');
INSERT INTO "cars_repairs_app_facturacompra" ("id","proveedor","numero_factura","fecha","total_monto","imagen_factura","fichero_factura","is_active","created_at","updated_at") VALUES (1,'el de los tornillos','AG-es-234','2025-08-24',245,'imagen_facturas_compra/carousel-bg-1.jpg','fichero_facturas_compra/testimonial-1.jpg',1,'2025-08-24 08:03:07.712147','2025-08-24 08:03:07.712147'),
 (2,'el de la sruedas','ES-ASD-456','2025-08-24',567,'imagen_facturas_compra/service-1.jpg','fichero_facturas_compra/service-2.jpg',1,'2025-08-24 08:03:39.887624','2025-08-24 08:03:39.888625');
INSERT INTO "cars_repairs_app_facturaventa" ("id","cliente","fecha","total_monto","imagen_factura","fichero_factura","is_active","created_at","updated_at") VALUES (1,'Cliente 1','2025-08-24',123,'imagen_facturas_venta/carousel-1.png','fichero_facturas_venta/about.jpg',1,'2025-08-24 07:54:29.420740','2025-08-24 07:54:29.420740');
INSERT INTO "cars_repairs_app_lineafacturaventa" ("id","cantidad","precio_unitario","imagen_factura","fichero_factura","is_active","created_at","updated_at","articulo_id","factura_id") VALUES (1,3,123,'imagen_facturas_linea_venta/service-4.jpg','fichero_facturas_linea_venta/testimonial-3.jpg',1,'2025-08-24 07:54:29.428741','2025-08-24 07:54:29.428741',1,1),
 (2,4,23,'','',1,'2025-08-24 07:54:29.429747','2025-08-24 07:54:29.429747',2,1);
INSERT INTO "cars_repairs_app_cliente" ("id","nombre_completo","email","telefono","direccion","imagen_cliente","fichero_cliente","created_at","updated_at","is_active") VALUES (1,'Cliente 1','msb.tesla@gmail.com','Cliente 1','Cliente 1','imagen_clientes/service-4.jpg','fichero_clientes/testimonial-1.jpg','2025-08-24 08:22:58.405503','2025-08-24 08:22:58.405503',1),
 (2,'Cliente 11','msb.motive@gmail.com','Cliente 11','Cliente 11','imagen_clientes/service-2.jpg','fichero_clientes/service-3.jpg','2025-08-24 08:23:20.866851','2025-08-24 08:23:20.866851',1);
INSERT INTO "cars_repairs_app_ordendetrabajo" ("id","vehiculo","descripcion_problema","estado","fecha_entrada","fecha_salida_estimada","imagen_ot","fichero_ot","created_at","updated_at","is_active","cliente_id","factura_id") VALUES (1,'vehculo 1','vehculo 1','pendiente','2025-08-24',NULL,'','','2025-08-24 08:25:20.772710','2025-08-24 08:25:20.772710',1,1,1),
 (2,'vehculo 1','vehculo 1','pendiente','2025-08-24',NULL,'','','2025-08-24 08:25:43.236080','2025-08-24 08:25:43.236080',1,2,NULL);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_testimonial_servicio_id_89daf1e5" ON "cars_repairs_app_testimonial" (
	"servicio_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_booking_servicio_id_f3d7543d" ON "cars_repairs_app_booking" (
	"servicio_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_lineafacturaventa_articulo_id_7ccd53c2" ON "cars_repairs_app_lineafacturaventa" (
	"articulo_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_lineafacturaventa_factura_id_202119f9" ON "cars_repairs_app_lineafacturaventa" (
	"factura_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_ordendetrabajo_cliente_id_9016e4e8" ON "cars_repairs_app_ordendetrabajo" (
	"cliente_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "cars_repairs_app_ordendetrabajo_servicios_realizados_ordendetrabajo_id_service_id_7da7cc86_uniq" ON "cars_repairs_app_ordendetrabajo_servicios_realizados" (
	"ordendetrabajo_id",
	"service_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_ordendetrabajo_servicios_realizados_ordendetrabajo_id_bd204202" ON "cars_repairs_app_ordendetrabajo_servicios_realizados" (
	"ordendetrabajo_id"
);
CREATE INDEX IF NOT EXISTS "cars_repairs_app_ordendetrabajo_servicios_realizados_service_id_90bdd64d" ON "cars_repairs_app_ordendetrabajo_servicios_realizados" (
	"service_id"
);
COMMIT;
