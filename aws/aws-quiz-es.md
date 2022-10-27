## Servicios web de Amazon (AWS)

#### P1. Tiene una aplicación que utiliza una base de datos MySQL de 100 GB que está migrando a AWS. ¿Qué debe tener en cuenta al decidir si desea alojar la base de datos en RDS para MySQL o Aurora?

- \[ ] costo
- \[ ] facilidad de mantenimiento vs. granularidad del control
- \[x] todas estas respuestas
- \[ ] el motor de almacenamiento actual utilizado por la aplicación, como InnoDB o MyISAM

#### P2. ¿Qué base de datos es un tipo de base de datos NoSQL que puede almacenar y recuperar rápidamente pares clave-valor?

- \[ ] Aurora
- \[ ] Neptuno
- \[ ] RDS para MySQL
- \[x] DynamoDB

#### P3. La base de datos es una instancia de RDS que ejecuta SQL Server con replicación Multi-AZ y tiene varias utilidades de consola de .NET más antiguas que realizan operaciones de base de datos cada 15 segundos. Cuando el clúster tiene que cambiar el servidor de base de datos principal a la zona de disponibilidad secundaria, las utilidades de .NET comienzan a informar de errores de conexión a la base de datos, aunque otras aplicaciones pueden tener acceso a la base de datos. ¿Cómo se corrige este problema?

- \[ ] Utilice la consola rdsi para forzar un reinicio de la instancia de base de datos de modo que el servidor principal vuelva a ser el servidor maestro.
- \[ ] El servidor que ejecuta las utilidades .NET está almacenando en caché la búsqueda DNS en la dirección del clúster de base de datos. Vacíe la caché DNS del servidor y fuerce las utilidades de C# para abrir nuevas conexiones a la base de datos.
- \[ ] A.NET aplicación conservará la dirección IP de una cadena de conexión hasta que se reinicie el equipo host.
- \[x] Las utilidades net deben cambiar el extremo de SQL Server en las cadenas de conexión para leer desde el servidor de base de datos secundario mediante un try/catch.

#### P4. ¿Qué servicios de AWS pueden ayudarle a automatizar su canalización de desarrollo para la integración continua y la implementación continua?

- \[ ] CodePipeline
- \[ ] CodeDeploy
- \[x] todas estas respuestas
- \[ ] CodeBuild

#### P5. ¿Qué servicio de AWS cumple con los estándares descritos en el Nivel 1 del Estándar de seguridad de datos de la industria de tarjetas de pago (PCI DSS) para el manejo y la transmisión de datos de tarjetas de crédito?

- \[ ] Puerta de enlace API
- \[x] todas estas respuestas
- \[ ] Servicio de cola simple (SQS)
- \[ ] Kinesis Data Streams

#### P6. Tiene una gran cantidad de archivos en su arreglo de discos de almacenamiento de información conectado a la red que deben archivarse y mantenerse durante un período de 10 años debido a las regulaciones de la industria. Se accederá a estos datos con poca frecuencia, pero deben conservarse ¿Cuál es el mejor servicio de AWS para almacenar estos datos?

- \[ ] EFS
- \[ ] Bola de nieve
- \[ ] OEBS
- \[x] Glaciar S3

#### P7. Para su cuenta raíz de AWS, ha generado una contraseña aleatoria de la longitud máxima permitida e incluido caracteres especiales. ¿Qué pasos adicionales debe seguir para proteger su cuenta raíz de AWS?

- \[ ] Cree un rol de AM para el administrador de la cuenta con los privilegios más altos. No almacene la contraseña raíz, pero cuando sea necesaria la cuenta raíz, restablezca la contraseña en la cuenta raíz mediante confirmación por correo electrónico y repita este procedimiento.
- \[ ] Almacene su contraseña generada aleatoriamente en su base de datos de secretos de organización utilizando un servicio como 1Password o LastPass, y solo otorgue acceso a este secreto al equipo de DevOps.
- \[ ] Cree cuentas de IAM para sus administradores y adjunte la política AdministratorAccess a sus cuentas. Deshabilite la cuenta raíz en la configuración del usuario.
- \[x] Cree un rol de IAM para el administrador de la cuenta con los privilegios más altos y no utilice la cuenta raíz en las operaciones diarias. Habilitar la autenticación de dos factores en la cuenta raíz

#### P8. ¿Qué opción de Elastic Load Balancing admite Lambda como destino?

- \[ ] Equilibrador de carga de red
- \[ ] Lambda no puede ser llamado directamente por las solicitudes web entrantes. Debe utilizar API Gateway.
- \[ ] Equilibrador de carga clásico
- \[x] Balanceador de carga de aplicaciones

#### P9. ¿Cómo se diseña una solución para que una base de datos de SQL Server se replique en todas las regiones de AWS en una arquitectura activa-activa?

- \[ ] Utilice RDS para SQL Server y cree la misma instancia en dos regiones diferentes. Utilice el Servicio de migración de bases de datos para mantener cada base de datos sincronizada.
- \[ ] Utilice un emparejamiento vpn o VPC para establecer una conexión entre las VPC de cada región. Instale SQL Server Enterprise Edition en instancias EC2 de cada región y configure un grupo de disponibilidad Always On.
- \[x] Use RDS para SQL Server 2016 o 2017 Enterprise Edition. Habilite la compatibilidad con Multi-AZ y seleccione la opción Duplicación/Siempre activada. Seleccione otra región para la opción de duplicación.
- \[ ] No puede configurar una arquitectura activo-activa para SQL Server que abarque regiones geográficas.

[Referencia](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html?opt_id=oeu1612780272452r0.9199525073583283)

#### P10. ¿Cuánto cuesta lanzar una instancia EC2 desde AWS Marketplace?

- \[ ] Todas las imágenes de AWS Marketplace incurren en tarifas por hora adicionales además de los cargos del tamaño de instancia que seleccione.
- \[ ] Solo puede lanzar imágenes creadas por otros usuarios en su cuenta de AWS, por lo que solo paga por el tamaño de instancia que seleccione y los costos de almacenamiento de S3 para la imagen base.
- \[x] Cada imagen tiene su propio precio que podría ser gratuito o incluir cargos por los costos de licencia de software. También pagará por la instancia en la que se ejecuta la imagen
- \[ ] Todas las imágenes de AWS Marketplace contienen solo software de código abierto sin cargos adicionales y son creadas por otros usuarios de AWS. Solo pagará por el tamaño de instancia que seleccione.

#### P11. Cuando se utiliza un clúster de ECS con instancias EC2, ¿qué tareas de mantenimiento debe realizar en ec2?

- \[ ] Las instancias creadas por ECS no tienen parches que deban aplicarse; sin embargo, debe asegurarse de que los contenedores contengan actualizaciones de seguridad importantes.
- \[x] Actualice el clúster con instancias creadas a partir de la AMI de ECS más reciente.
- \[ ] Los clústeres de ECS no utilizan instancias EC2.
- \[ ] No debe manipular directamente las instancias EC2 creadas por ECS. AWS actualizará automáticamente estas instancias.

#### P12. ¿Qué servidor de almacenamiento en caché en memoria no es compatible con ElastiCache?

- \[ ] Redis 5
- \[ ] Memcached
- \[x] Elasticsearch
- \[ ] Redis 3

#### P13. ¿Qué servicio de AWS se puede utilizar para ayudar a generar la documentación requerida por varios estándares de conformidad, como el Estándar de seguridad de datos de la industria de tarjetas de pago (PCI DSS) Nivel 1 para el manejo de datos de tarjetas de crédito?

- \[x] Artefacto
- \[ ] DocumentDB
- \[ ] Imprima el resumen de conformidad de AWS y guárdelo con la documentación necesaria para una auditoría.
- \[ ] Gestor de secretos

#### P14. Cuando se utiliza AWS para investigación y desarrollo antes de una migración planificada, ¿cómo se evitan aumentos inesperados o picos en la facturación?

- \[ ] Utilice el panel de facturación para crear un presupuesto de costos. Ingrese la cantidad máxima que desea que se le cobre cada mes. Cualquier cargo que se produzca por encima de esta cantidad hará que AWS suspenda automáticamente esos recursos.
- \[ ] Con la cuenta raíz de AWS, active el acceso de IAM a la información de facturación de la cuenta. Asegúrese de que los usuarios de IAM tengan la política Billing FullAccessGroup. Luego, desde el panel de facturación, verifique los cargos acumulados una vez al día.
- \[ ] Si está utilizando la capa gratuita de AWS, tendrá que confirmar el uso de cualquier servicio que supere los límites de la capa gratuita de AWS.
- \[x] Con la cuenta raíz de AWS, habilite alertas de facturación en las preferencias del usuario. A continuación, utilice CloudWatch para crear una alarma de facturación y establecer un umbral en un importe específico en dólares para sus cargos mensuales estimados.

#### P15. Está creando una tabla de DynamoDB para almacenar todas las películas que se han estrenado desde 1938. Su aplicación permitirá a los usuarios buscar por título de película y ver los detalles de esa película. Dado el ejemplo siguiente que muestra los datos de película que va a importar, ¿cuál es el mejor conjunto de claves para aplicar a esta tabla?

```json
{
  "title": "The Avengers",
  "year": 2012,
  "cast": ["Mark Ruffalo", "Robert Downey, Jr."],
  "genres": ["Action"]
}
```

- \[ ] La clave principal debe ser una clave de partición del campo de título.
- \[ ] La clave principal debe ser el campo de título y la clave de partición debe ser el campo de géneros.
- \[ ] La clave principal debe ser una clave compuesta por una clave de partición en el campo de título y una clave de ordenación en el campo de año.
- \[x] La clave principal debe crearse como un valor completamente único, como una lista numérica secuencial de ID de película. La clave de partición debe ser el campo de título para una búsqueda rápida.

#### P16. ¿Qué almacén de datos proporciona una forma sencilla y rápida de almacenar atributos básicos de usuario en un formato basado en objetos?

- \[ ] ORDS para Oracle
- \[ ] Corrimiento al rojo
- \[ ] Neptuno
- \[x] DynamoDB

#### P17. Necesita una base de datos sin esquema. ¿Qué servicio de base de datos de Amazon proporciona esa solución?

- \[ ] ORDS
- \[ ] Aurora
- \[ ] Corrimiento al rojo
- \[x] DynamoDB

#### P18. ¿Qué canal de comunicación no admite SNS de forma nativa?

- \[ ] Mensaje de texto de OSMS
- \[ ] notificación push
- \[ ] correo electrónico
- \[x] llamada telefónica automatizada

#### P19. Al diseñar una aplicación web sin servidor con Lambda, ¿qué concepto clave debe tener en cuenta en su diseño?

- \[ ] Las aplicaciones web sin servidor se ejecutan dentro del navegador web del usuario, por lo que deberá almacenar cualquier dato que el usuario cambie directamente en una base de datos.
- \[ ] Lambda solo permite escribir funciones en JavaScript.
- \[ ] Lambda no utiliza servidores, por lo que solo puede devolver la misma solicitud a todos los usuarios.
- \[x] Lambda no tiene estado, por lo que no recordará quién es un usuario entre las solicitudes.

#### P20. Un principio de DevOps es ver la infraestructura como código. ¿Qué servicio de AWS le permite crear scripts de su infraestructura de AWS?

- \[ ] CloudTrail
- \[x] CloudFormation
- \[ ] AWS Config
- \[ ] Catálogo de servicios de AWS

#### P21. Ha creado una instancia EC2 de Windows con una dirección IP pública e instalado SQL Server. Al intentar conectarse a SQL Server desde el Administrador corporativo de SQL Server en el equipo local, la instancia EC2 de Windows no puede establecer una conexión con el servidor. ¿Qué es lo primero que debes comprobar?

- \[ ] Compruebe las tablas de enrutamiento de la VPC.
- \[x] Compruebe que los grupos de seguridad asignados permiten el tráfico del puerto TCP 1433 desde su dirección IP actual.
- \[ ] Compruebe las directivas de Firewall de Windows.
- \[ ] Compruebe que se está conectando a la instancia mediante un usuario que no es sa.

#### P22. Está hospedando una aplicación configurada para transmitir medios a sus clientes en los puertos TCP 3380-3384, 3386-3388 y 3390. La ficha Entrantes siguiente muestra tres directivas de grupo de seguridad entrantes asociadas a esta instancia. ¿Qué política debe utilizar?

![image](images/001.png?raw=png)

- \[x] La regla que expone los puertos TCP 3380-3390 también expondría públicamente el puerto 3389 (RDP) a todo Internet. Escriba reglas separadas para exponer solo los puertos necesarios.
- \[ ] La primera regla de grupo de seguridad permite todo el tráfico en esta instancia. Exponer toda la instancia a todo Internet deja el servidor abierto a varios ataques de los otros servicios que se ejecutan en diferentes números de puerto.
- \[ ] Verifique que los propietarios de las cuentas de AWS realmente controlan todo el bloque CIDR C para 12.228.11.0-255 y que estas son IP seguras para el acceso RDP en esta instancia.
- \[ ] No hay recomendaciones que hacer.

#### P23. Tiene cuatro servidores front-end web detrás de un equilibrador de carga, que usan NFS para acceder a otra instancia EC2 que cambia el tamaño y almacena imágenes para la aplicación front-end. ¿Qué directivas de grupo de seguridad se deben asignar a estos servidores?

- \[ ] Asigne IP elásticas a todas las instancias y cree un grupo que permita que todo el tráfico pase entre cada una de las cinco
  Elásticas direcciones IP y permiten todo el tráfico HTTPS entrante.
- \[x] Los servidores front-end web deben permitir HTTPS. Asigne otro grupo a todas las instancias que permita que todo el tráfico pase entre instancias mediante ese grupo.
- \[ ] Cree un grupo de seguridad que permita el tráfico NFS, HTTP y HTTPS entrante desde todas las direcciones IP. Aplique este grupo a todos los servidores.
- \[ ] Cree un grupo de seguridad que permita el tráfico HTTP y HTTPS entrante desde todas las direcciones IP y aplíquelo a los servidores web. Cree un segundo grupo de seguridad para el almacén de archivos NFS que permita el tráfico NFS saliente al intervalo IP privado de los servidores front-end web.

#### P24. Tiene un servidor web Linux EC2 que de repente se agota el tiempo de espera en todas las solicitudes HTTP y sus intentos de conexión SSH se agotan. Observa que está fallando la comprobación del estado del sistema en la consola de EC2. ¿Qué medidas debe tomar?

- \[x] Restaure la instancia desde la última imagen de la AMI. Las comprobaciones de estado del sistema indican que el sistema de archivos de la instancia está dañado.
- \[ ] Detenga e inicie la instancia. Esto moverá la instancia a otro host.
- \[ ] Póngase en contacto con el soporte técnico de AWS. El error de una comprobación del estado del sistema indica un error en el hardware subyacente y debe ser abordado por un representante de AWS.
- \[ ] Reinicie la instancia. Esto detendrá e iniciará la instancia y la moverá a otro host.

#### P25. Tiene varios servidores locales y le gustaría almacenar sus copias de seguridad externas en AWS. ¿Qué servicio de copia de seguridad totalmente administrado puede utilizar para enviar sus copias de seguridad a AWS?

- \[ ] Windows Server 2016 admite S3 como destino cuando se usan réplicas de almacenamiento.
- \[x] Utilice Storage Gateway.
- \[ ] Sincronice archivos directamente con S3 con la AWS CLI.
- \[ ] Utilice la consola rdsi para forzar un reinicio de la instancia de base de datos de modo que el servidor principal vuelva a ser el servidor maestro.

#### P26. ¿Cuál es la práctica recomendada para crear una base de datos PostgreSQL de alta disponibilidad en RDS que pueda soportar la pérdida de una sola región de AWS?

- \[ ] PostgreSQL no se puede replicar en todas las regiones. Restaure las copias de seguridad de la base de datos desde un bucket de S3 y vuelva a apuntar las conexiones de la base de datos a la nueva instancia.
- \[ ] Cree réplicas de lectura en otras regiones de AWS. Puede designar una nueva base de datos maestra a partir de cualquiera de las réplicas de lectura hasta que se resuelva el error regional.
- \[ ] Compruebe que la instancia está configurada para la compatibilidad con Multi-AZ. Los cambios en la base de datos se sincronizarán automáticamente con otra región en caso de error y RDS seleccionará automáticamente un nuevo maestro hasta que se resuelva el error regional.
- \[x] Cree réplicas de lectura en otras regiones de AWS. Asegúrese de que las operaciones de lectura en la base de datos se producen en una réplica de lectura disponible y envíe las operaciones de escritura a otra región si necesita promover una réplica de lectura a una base de datos independiente si el maestro está inactivo.

#### P27. Ha creado una nueva instancia EC2 de Linux e instalado PostgreSQL, pero no puede establecer una conexión con el servidor desde el equipo local. ¿Qué pasos toma para resolver este problema?

- \[ ] Cree una regla de grupo de seguridad que permita todo el tráfico de 0.0.0.0/0. Esto verificará si otra regla está denegando o no el tráfico.
- \[x] Compruebe que los grupos de seguridad asignados permiten el tráfico desde su dirección IP al puerto 5432. Compruebe que PostgreSQL está configurado para escuchar el tráfico externo y está enlazado a la interfaz pública.
- \[ ] Asegúrese de que está utilizando una IP elástica y que está incluida dentro de la `postgresql.conf` archivo de configuración.
- \[ ] Detenga e inicie la instancia. Las nuevas reglas de grupo de seguridad solo entrarán en vigor después de un reinicio.

#### P28. ¿Qué hace el cuerpo de la declaración de esta política de bucket de S3?

```json
{
  "Sid": "bucketpolicy1",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::userreports/*",
  "Condition": {
    "IpAddress": { "aws:SourceIp": "68.249.108.0/24" },
    "NotIpAddress": { "aws:SourceIp": "68.249.108.128/32" }
  }
}
```

- \[ ] bucketpolicy1 permite a cualquier usuario realizar cualquier acción en los objetos del bucket userreports, pero limita los objetos a permisos de solo lectura para cualquier persona que provenga de 68.249.108.0 a 68.249.108.255, excepto 68.249.108.128.
- \[ ] bucketpolicy1 permite a cualquier usuario procedente del intervalo IP de 68.249.108.0 acceder a objetos del bucket userreports y deniega el acceso a 68.249.108.128.
- \[ ] bucketpolicy1 permite a cualquier usuario realizar cualquier acción en los objetos del bucket userreports , excepto cualquier persona que provenga de la IP de 68.249.108.128.
- \[x] bucketpolicy1 permite a cualquier usuario que provenga del intervalo IP de 68.249.108.0 a 68.249.108.255 acceder a objetos del bucket userreports, excepto cualquier persona que provenga de la IP de 68.249.108.128.

#### P29. Se ha agregado un nuevo desarrollador al equipo y se le ha pedido que proporcione acceso a la cuenta de AWS de la organización. ¿Cuál es la mejor práctica para conceder acceso?

- \[ ] Proporcione al nuevo desarrollador el inicio de sesión de IAM que se asigna al equipo de desarrollo. Este usuario de IAM ya debería incluir todas las políticas que un desarrollador necesitaría.
- \[ ] Cree un usuario de IAM para el nuevo desarrollador. Asigne políticas manualmente a la nueva cuenta de usuario de IAM.
- \[ ] No otorgue al nuevo desarrollador acceso a la consola de AWS. Con el usuario de IAM asignado al grupo de desarrollo, genere un nuevo conjunto de claves de acceso y etiquételas con el nombre del desarrollador.
- \[x] Cree un usuario de IAM para el nuevo desarrollador. Asigne al nuevo desarrollador un grupo de desarrolladores que ya haya creado para los demás desarrolladores.

#### P30. Al lanzar una instancia EC2 con un tipo de instancia que admita el almacenamiento de instancias, ¿qué caso de uso es mejor para el almacenamiento de instancias?

- \[x] Utilice el almacenamiento de instancias para servir archivos temporales que requieren una latencia de E/S baja.
- \[ ] Utilice el almacenamiento de instancias para gestionar los archivos cargados por los usuarios. Dado que es más seguro que un volumen de EBS, puede aislar cualquier archivo malicioso para que no infecte el servidor.
- \[ ] El almacenamiento de instancias es más rápido que los volúmenes de EBS, así que instale la raíz del sistema operativo en este volumen para acelerar el rendimiento del servidor.
- \[ ] El almacenamiento de instancias es una opción obsoleta para el almacenamiento y no debe utilizarse.

#### P31. ¿Cuál es la práctica recomendada para escalar horizontalmente una aplicación web heredada ASP.NET que se basa en Active Directory y que actualmente se implementa en una única instancia EC2 de Windows?

- \[x] Utilice Sysprep para apagar la instancia durante una ventana de mantenimiento. Cree una imagen AMI y coloque ambos servidores detrás de Application Load Balancer con sesiones adhesivas.
- \[ ] Inicie un nuevo EC2 con la última versión de Windows Server e instale la aplicación de nuevo. Utilice Application Load Balancer y sesiones adhesivas para equilibrar entre ambos servidores.
- \[ ] Cree un clon del servidor utilizando una imagen AMI y el usuario Application Load Balancer para equilibrar el tráfico entre ambas instancias mediante sesiones adhesivas.
- \[ ] El escalado horizontal no es la mejor práctica en esta situación. Aumente el tamaño de la instancia EC2 existente y escale verticalmente la aplicación.

#### P32. ¿Qué hace esta pequeña sección de una plantilla de CloudFormation?

```yaml
FlowLog:
  Type: AWS::EC2::FlowLog
  Properties:
    DeliverLogsPermissionArn: !GetAtt IamRole.Arn
    LogGroupName: FlowLogsGroup
    ResourceId: !Ref LogVpcId
    ResourceType: VPC
    TrafficType: ALL
```

- \[x] Escribe los registros de flujo de red de la VPC en el grupo de registros FlowLogsGroup de CloudWatch. Puede utilizar esto para inspeccionar las conexiones de red de su VPC.
- \[ ] Registra todo el tráfico de red dentro de una VPC excepto los ID de instancia definidos por LogVpcID y lo registra en el grupo de registros FlowLogsGroup de CloudWatch.
- \[ ] Registra todo el tráfico de red que va hacia y desde una sola instancia EC2 en el grupo de registros De CloudWatch FlowLogsGroup. Puede usar esto para inspeccionar el tráfico de red sospechoso que ingresa a una instancia EC2.
- \[ ] Registra todas las solicitudes de DNS realizadas por los recursos dentro de una VPC y las registra en CloudWatch FlowLogsGroup. Utilice esta opción para diagnosticar errores de búsqueda dns en su entorno.

#### P33. Está ejecutando contenedores docker en ECS. ¿Cuál es la métrica más importante para monitorear?

- \[ ] El recuento de contenedores en ejecución para cada servicio desde CloudWatch.
- \[ ] El estado de la instancia de cada instancia EC2 del clúster desde CloudWatch.
- \[ ] Supervise el panel de servicio de EC2. Esté atento a las interrupciones publicadas en el servicio ECS.
- \[x] El consumo de memoria de cada instancia EC2 en su clúster desde CloudWatch.

#### P34. Application Load Balancer puede enrutar el tráfico a varios grupos de destino diferentes en función de varias condiciones. ¿Cuál de estos casos de uso no es compatible con Application Load Balancer?

- \[ ] Una solicitud con un encabezado HTTP de X-Requested-With: staging se puede enrutar a un grupo de destino para un servicio ECS en su entorno de ensayo.
- \[ ] Las direcciones IP de origen que coincidan con 192.0.2.0/24 en un puerto de escucha de 1433 se pueden enrutar a un grupo de destino para un clúster de RDS para SQL Server.
- \[ ] Una ruta de /signup\* se puede enrutar a un grupo de destino para una función de Lambda que procesa nuevos registros de usuarios.
- \[x] Una cadena de consulta Http POST de ? action=createuser se puede enrutar a un grupo de destino para un servicio ECS.

#### P35. ¿Qué hace una VPC?

- \[x] crea una red basada en la nube para interconectar un conjunto de servidores y dispositivos virtuales
- \[ ] crea un túnel seguro entre dos redes
- \[ ] crea un plano de almacenamiento compartido para que los datos de la aplicación se compartan entre varias instancias.
- \[ ] crea una red privada que está completamente aislada de la Internet pública.

#### P36. ¿Puede perder la dirección IP pública asociada a su instancia EC2?

- \[ ] Sí, puede perderlo si reinicia la instancia.
- \[x] Sí, puede perderlo si detiene e inicia la instancia.
- \[ ] No, nunca perderá la dirección IP pública de su instancia.
- \[ ] Sí, puede perderlo cuando edite las propiedades de la instancia y libere la dirección IP.

#### P37. ¿Dónde está el mejor lugar para almacenar copias de seguridad de bases de datos en una instancia EC2 configurada como servidor de bases de datos?

- \[x] un bucket de S3, sincronizado con las copias de seguridad de la base de datos a través de un script que llama a la AWS CLI
- \[ ] Volumen de EBS adjunto a la instancia
- \[ ] instancia adjunta a la instancia
- \[ ] almacenamiento de instancias, con un script que replica las copias de seguridad de la base de datos en otra instancia en una zona de disponibilidad diferente.

#### P38. ¿Cuál de estas es una restricción válida en las propiedades de una VPC?

- \[ ] Solo puede tener 10 gateways de Internet por región en una nueva cuenta de AWS.
- \[ ] Solo puede tener 10 VPC por región en una nueva cuenta de AWS
- \[x] No se puede crear un bloque CIDR con una máscara de red mayor que /16
- \[ ] Solo puede tener 10 subredes dentro de una VPC

#### P39. Tiene una instancia EC2 de Linux que no responde a las solicitudes y no puede conectarse a ella a través de SSH. Con la consola de EC2, emitió un comando para detener la instancia, pero durante los últimos 10 minutos la instancia ha estado en el estado de "detención". ¿Cuál es el siguiente paso que debes dar?

- \[x] Realice otra acción de detención a través de la consola de EC2 y elija la opción para detener la instancia con fuerza.
- \[ ] Cree una imagen AMI de la instancia y elija la opción para tomar la imagen sin reiniciar la instancia.
- \[ ] Edite las propiedades de la instancia y aumente el tamaño de la instancia.
- \[ ] Póngase en contacto con el soporte técnico de AWS. Cualquier otra acción podría dañar el sistema de archivos.

#### P40. Tiene 14 servidores web locales, 4 servidores de bases de datos, 6 servidores que utilizan software SIG, 3 servidores de archivos y 4 servidores de desarrollo. ¿Qué consideraciones debe tener en cuenta al migrar estos servidores a AWS?

- \[ ] AWS no tiene una forma de separar la facturación de los costos informáticos, por lo que deberá diseñar una forma de dividir el presupuesto entre departamentos.
- \[x] Las nuevas cuentas de AWS están limitadas a 20 instancias EC2 bajo demanda. Envíe una solicitud para aumentar sus límites de velocidad antes de iniciar una migración.

#### P41. A medida que su aplicación web crece y sus necesidades de supervisión de aplicaciones se vuelven más complejas, ¿qué servicio adicional de supervisión de registros NO debe considerar?

- \[ ] Pila ELK: Elasticsearch, Loggly y Kibana
- \[x] PRTG
- \[ ] Nueva Reliquia
- \[ ] Datadog

#### P42. Tiene una instancia T2 EC2 que es crítica para su infraestructura. ¿Cómo supervisaría la métrica más importante para este caso?

- \[x] Active CloudWatch Auto Recovery y coloque monitores en las comprobaciones de estado del sistema y estado de la instancia para que la instancia le notifique cuando cualquiera de las dos esté en alarma.
- \[ ] Utilice CloudWatch para colocar monitores en los créditos de CPU restantes. Si se queda sin crédito de CPU, la instancia se detendrá.

#### P43. ¿Qué función se puede utilizar para responder a un aumento repentino del tráfico web?

- \[ ] Grupos de EC2 Auto Scaling
- \[ ] AWS Shield Advanced
- \[ ] Réplicas de lectura de RDS
- \[x] todas estas respuestas

#### P44. Si un conjunto de servidores se encuentra dentro de una subred privada de la VPC, ¿cómo puede conectar esos servidores a servidores locales?

- \[ ] Establezca una conexión con AWS Direct Connect.
- \[ ] Utilice AWS Client VPN.
- \[ ] Instale un servidor OpenVPN en una instancia que se encuentra dentro de la subred con una IP elástica.
- \[x] Todas estas opciones pueden establecer una conexión a una subred privada.

#### P45. Tiene un equilibrador de carga UDP creado por una instancia que ejecuta un proxy NGINX. La solución de administración del rendimiento de las aplicaciones (APM) puede detectar errores en la instancia del equilibrador de carga y transferir la ELASTIC IP a una instancia de espera pasiva. Con la AWS CLI, ¿qué script programa en su APM para mover la IP elástica?

- \[x] A

<!---->

    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] B

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 assign-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] C

<!---->

    aws ec2 stop-instances --instance-ids i-8b953
    wait 30
    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
    aws ec2 start-instances --instance-ids i-8b953

- \[ ] D

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

#### P46. ¿Qué servicio puede alojar sus contenedores Docker?

- \[ ] Vela de luz
- \[ ] Elastic Container Service (ECS)
- \[ ] Elastic Compute Cloud (EC2)
- \[x] Todos estos servicios pueden alojar un contenedor docker.

#### P47. En la consola de S3, debajo de la columna Acceso, ¿qué indica la insignia pública junto al nombre del bucket?

![image](images/002.png?raw=png)

- \[x] A todos los objetos de este bucket se les asigna acceso público y cualquier persona en Internet puede leerlos o escribirlos. Asegúrese de que no se compartan públicamente datos confidenciales dentro de este bucket.
- \[ ] Todos los objetos dentro de este bucket son grabables, lo que significa que la Internet pública tiene la capacidad de cargar cualquier archivo directamente en su bucket de S3. Su bucket de S3 podría usarse para servir malware.
- \[ ] A algunos objetos de este bucket se les asigna acceso público. Compruebe que los objetos compartidos públicamente dentro de este bucket no contengan datos confidenciales.
- \[ ] Los objetos dentro de este bucket se pueden hacer públicos, si la ACL de ese objeto está configurada para permitir el acceso de todos. Los buckets privados no permiten establecer permisos públicos en ningún objeto.

#### P48. ¿Qué privilegio es específico de la cuenta raíz de AWS y no se puede conceder a otro usuario de IAM en la cuenta?

- \[ ] Revocar el rol AdministratorAccess o concederlo a otro usuario de IAM.
- \[ ] Cree una nueva zona hospedada en Route 53.
- \[x] Elimine la cuenta de AWS.
- \[ ] Modificar los detalles de facturación.

#### Pregunta 49. Su aplicación está enviando 50,000 correos electrónicos a través de SES cada día. Dado que debe mantener una tasa de rebote baja para evitar ser puesto en libertad condicional, ¿qué sistema simple diseña para procesar automáticamente los rebotes duros?

- \[x] Configure SES para enviar todos los eventos de rebote a un tema de SNS. Cree una función de Lambda que procese cada evento de rebote duro y marque automáticamente esa cuenta como rebote en la aplicación para evitar más intentos de envío.
- \[ ] Configure SES para que ya no se envíe a direcciones de correo electrónico que estén en su lista de rebotes.
- \[ ] Configure SES para enviar los registros de todos los intentos de entrega a través de Kinesis Firehose. Procesa cada evento y busca tipos de rebote y elimina estos correos electrónicos de tu lista.
- \[ ] Envíe todos los correos electrónicos a través de SES con un encabezado de respuesta personalizado. Configure SES para escuchar los eventos en esta dirección de correo electrónico y marque cualquier dirección de correo electrónico que responda a esta cuenta como un mensaje rebotado y elimínela de su lista de correo electrónico.

#### Pregunta 50. Su aplicación web está recibiendo una cantidad sospechosa de solicitudes incorrectas de direcciones IP extranjeras. Su negocio está operando en solo unos pocos países y le gustaría bloquear cualquier otro tráfico. ¿Cuál es la mejor práctica para limitar el acceso a su aplicación web por país?

- \[x] Utilice Web Application Firewall y cree una condición de coincidencia geográfica para eliminar todas las solicitudes de países que no están en su lista de permitidos.
- \[ ] Utilice Application Load Balancer para crear una nueva regla de enrutamiento que examine la dirección IP de origen. Agregue un bloque de IP para los países que tienen acceso.
- \[ ] Aloje el front-end de su sitio web en CloudFront y configure una restricción geográfica en la distribución.
- \[ ] Utilice CloudTrail para supervisar las direcciones IP de las solicitudes incorrectas. Utilice Lambda para agregar estas direcciones IP a una regla del equilibrador de carga de aplicaciones que bloquea las direcciones IP.

#### Pregunta 51. ¿Cuál es la práctica recomendada para mantener las instancias EC2 de Windows y aplicar actualizaciones?

- \[ ] Active la actualización automática en Windows Update en cada EC2 que se lance, o cree su propia AMI con esta característica habilitada y lance todas sus instancias EC2 desde esta AMI.
- \[ ] Cree un programa de mantenimiento que un empleado debe completar cada semana confirmando que se realizó una inspección visual de cada instancia y qué parches se aplicaron.
- \[x] Utilice AWS Systems Manager Patch Manager para buscar instancias de parche que requieran actualizaciones durante una ventana de mantenimiento establecida.
- \[ ] Instale Windows Server Update Services en el controlador principal de Active Directory.

#### P52. Además de CloudFormation, puede utilizar otras herramientas de orquestación para automatizar la formación y el mantenimiento de servidores. ¿Qué herramienta es _no_ una opción eficiente para la orquestación de una gran infraestructura?

- \[ ] Chef
- \[ ] Ansible
- \[ ] Títere
- \[x] Vagabundo

#### Pregunta 53. ¿Qué sucede con una instancia rds de SQL Server si las bases de datos aumentan de tamaño y superan el espacio asignado?

- \[ ] RDS aumentará automáticamente el espacio asignado en un 10 % y enviará a la cuenta raíz de AWS un correo electrónico con los pasos de resolución. Asigne más espacio para evitar cargos por exceso de edad.
- \[x] La instancia de base de datos informará de un estado de STORAGE_FULL y se volverá inaccesible si la instancia no tiene suficiente almacenamiento restante para funcionar. Asigne más espacio a la instancia.
- \[ ] SQL Server cerrará todas las conexiones existentes a las bases de datos e intentará reducir sus archivos de registro para recuperar espacio de almacenamiento.
- \[ ] RDS aumentará automáticamente el espacio asignado en un 5% y continuará asignando nuevo espacio hasta el 50% del espacio original asignado. Cuando el espacio de almacenamiento ha aumentado un 50%, RDS detendrá automáticamente la instancia para preservar la integridad de los datos.

#### Pregunta 54. Tiene una flota de dispositivos IoT que envían telemetría a una aplicación del lado del servidor proporcionada por su proveedor de IoT para decodificar un formato de mensajería propietario. Los dispositivos se aprovisionan para enviar informes de telemetría al servidor a través de UDP en el puerto 6339. ¿Cuál es la mejor manera de escalar este servidor a medida que se agregan más dispositivos Iot a su flota?

- \[ ] Utilice un equilibrador de carga de red para distribuir el tráfico entre sus servidores. Utilice las comprobaciones de estado de UDP para determinar si el servidor está disponible para recibir tráfico.
- \[x] Utilice Route 53 con comprobaciones de estado HTTP. Cree una aplicación en el servidor para informar del estado de preparación del software de servidor proporcionado por el proveedor a Route 53 a través de HTTP.
- \[ ] Utilice Route 53 con comprobaciones de estado de UDP. A medida que se amplía la escala, Route 53 enrutará el tráfico a los nuevos servidores si pasan las comprobaciones de estado.
- \[ ] Utilice Application Load Balancer para distribuir el tráfico entre los servidores.

#### Pregunta 55. las reglas de salida de un grupo de seguridad solo permiten que el tráfico vaya a 0.0.0.0/0 en el puerto TCP 22 (SSH) y el puerto TCP 3306 (MySQL). Revise las reglas de entrada enumeradas en la imagen a continuación. ¿Cuál es el problema más importante a solucionar con esta configuración de grupo de seguridad, para una instancia EC2 de Ubuntu que actúa como servidor web?

![image](https://user-images.githubusercontent.com/8637045/112515574-c077e780-8d6c-11eb-96a6-11f27a0547cf.png?raw=png)

- \[ ] Las reglas de salida bloquean el puerto UDP 53, por lo que el servidor no podrá resolver ninguna búsqueda DNS.
- \[x] Las reglas de salida no permiten que el tráfico HTTP salga de la instancia, por lo que las solicitudes HTTP entrantes fallarán porque los clientes nunca obtendrán respuestas HTTP.
- \[ ] El puerto SSH entrante no debe estar abierto al público. Limite SSH a una sola dirección IP o rango de IP de dirección controlada, o utilice una VPN para acceder a la VPC de este servidor.
- \[ ] Se exponen todos los puertos TCP entrantes, lo que anula las reglas HTTP y SSH y expone todos los puertos TCP a la Internet pública.

#### Pregunta 56. Una instancia EC2 que ejecuta un sitio de WordPress sigue siendo pirateada, a pesar de que ha restaurado el servidor varias veces y ha parcheado WordPress. ¿Qué servicio de AWS puede ayudarle a detectar y prevenir nuevos ataques?

- \[ ] CloudWatch
- \[x] GuardDuty
- \[ ] Escudo
- \[ ] Asesor de seguridad

#### Pregunta 57. Un cliente no técnico desea migrar un sitio de WordPress a AWS desde un servidor privado administrado por una empresa de alojamiento de terceros. ¿A qué servicio de AWS debería recomendar migrar el sitio?

- \[ ] CloudFront
- \[ ] Una instancia EC2 lanzada desde la AMI oficial de WordPress
- \[ ] S3
- \[x] Vela ligera

#### Pregunta 58. Su empresa tiene servidores locales con una solución de copia de seguridad en el sitio existente que también replica las copias de seguridad en otro campus en el otro lado del país con su propia solución de copia de seguridad en el sitio. Se le ha pedido que cree un tercer nivel de redundancia almacenando también estas copias de seguridad en la nube. En el caso de una falla de copia de seguridad primaria y secundaria, su jefe quiere saber que las copias de seguridad en la nube pueden ser accesibles lo más rápido posible para reducir el tiempo de inactividad durante la recuperación. ¿Qué clase de almacenamiento de S3 recomienda por costo y rendimiento?

- \[ ] Estándar S3
- \[ ] S3 Intelligent-Tiering
- \[ ] Glaciar S3
- \[x] Acceso poco frecuente a una zona de S3

#### Pregunta 59. ¿Qué big data store le permitirá almacenar grandes flujos de datos de actividad del usuario procedentes de aplicaciones web y móviles?

- \[ ] Neptuno
- \[ ] Aurora
- \[ ] RDS para SQL Server
- \[x] Corrimiento al rojo

#### P60. ¿Qué opción es la mejor para Auto Scaling sus instancias EC2 para patrones de tráfico predecibles?

- \[x] escala basada en un cronograma
- \[ ] escalado manual
- \[ ] escala basada en la demanda
- \[ ] mantener los niveles actuales en todo momento

#### P61. Está migrando un clúster de RabbitMQ local a AWS. ¿Qué ruta de migración debe elegir para facilitar tanto el mantenimiento como la implementación?

- \[ ] Vuelva a escribir las partes de su aplicación que usan RabbitMQ para usar SQS.
- \[ ] Lance un clúster de RabbitMQ con instancias EC2 utilizando una AMI compatible.
- \[ ] Vuelva a escribir las partes de su aplicación que usan RabbitMQ para usar Kinesis.
- \[x] Vuelva a escribir las partes de la aplicación que utilizan RabbitMQ para utilizar Amazon MQ.

#### P62. Al crear una nueva instancia de RDS, ¿qué hace la opción Multi-AZ?

- \[ ] replica las copias de seguridad de su base de datos en S3 y las pone a disposición en todas las regiones para evitar cualquier pérdida de datos
- \[x] crea una segunda instancia de base de datos pasiva dentro de la misma región que se convertirá en la base de datos principal durante una conmutación por error
- \[ ] crea un clúster de bases de datos de alta disponibilidad que hospedará el clúster de bases de datos en al menos dos regiones
- \[ ] crea otra instancia de base de datos en otra región y mantiene activo un modo de espera activo para la conmutación por error durante los errores regionales

#### P63. ¿Cuál es la mejor clase de instancia EC2 para un servidor que continuamente tiene una carga pesada de CPU?

- \[x] C5
- \[ ] T2
- \[ ] R5
- \[ ] H1

#### Pregunta 64. El sistema de gestión del rendimiento de las aplicaciones (APM) puede leer el estado de los monitores de CloudWatch y realizar acciones programadas. Cuando la métrica de CloudWatch StatusCheckFailed entra en un estado de error (un valor de 1), desea que su APM repare automáticamente la instancia. ¿Qué script utilizas?

- \[x] A

<!---->

    aws ec2 stop-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

- \[ ] B

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123

- \[ ] C

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    wait 30
    aws ec2 start-instance --instance-ids i-0b263919b6498b123

- \[ ] D

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

#### Pregunta 65. ¿Qué hay de malo en la tercera regla de grupo de seguridad entrante, que permite que todo el tráfico de sg-269afc5e vaya a una instancia EC2 de Ubuntu configurada como servidor web?

![065](https://user-images.githubusercontent.com/33999631/179728393-8a2636ea-04e7-4597-b0cc-8150e2bc91de.png?raw=png)

- \[ ] Todo el tráfico en todos los puertos se está denegando en esta instancia, lo que sobrescribe la regla HTTP y la hace redundante.
- \[x] La instancia se lanzó con el grupo de seguridad predeterminado, pero no hay forma de que un administrador entre SSH en la instancia.
  Agregue otra regla que permita el acceso SSH desde un origen seguro, como una sola IP o un rango de direcciones IP administradas.
- \[ ] No hay nada de malo en esta regla de grupo de seguridad. Suponiendo que sg-269afc5e se aplica a otros recursos que son correctamente
  protegido, esta regla permite que pase todo el tráfico que también está asignado al grupo de seguridad sg-269afc5e.
- \[ ] Todo el tráfico en todos los puertos está permitido en esta instancia. Esto expone la instancia a todo el tráfico público de Internet y
  sobrescribe la regla HTTP entrante.

#### Pregunta 66. Tiene una VPC que tiene una subred pública y privada. Hay una puerta de enlace NAT en la subred pública que permite a las instancias de la subred privada acceder a Internet sin tener exposición pública fuera de la VPC. ¿Cuáles deben ser las tablas de enrutamiento para la subred privada?

![image](images/003.png?raw=png)

- \[x] A

<!---->

    Destination 1: 10.0.0.0/16, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] B

<!---->

    Destination 1: 10.0.0.0/24, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

- \[ ] C

<!---->

    Destination 1: 10.0.0.0/24, Target 1: subnet-1948ba2;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] D

<!---->

    Destination 1: 10.0.0.0/16, Target 1: vpc-12bd09ac2;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

#### Pregunta 67. Para cumplir con los requisitos de auditoría de algunos estándares de conformidad, ¿qué herramienta de AWS se puede habilitar para mantener un registro de auditoría del acceso y los cambios en su infraestructura de AWS?

- \[x] CloudTrail
- \[ ] CloudWatch
- \[ ] Herramienta de auditoría y conformidad de AWS
- \[ ] GuardDuty

#### Pregunta 68. Tiene una aplicación que genera informes de larga duración, los almacena en un bucket de S3 y, a continuación, envía un correo electrónico al usuario que solicitó el informe con un vínculo para descargarlo. ¿Cuál es la práctica recomendada para almacenar los datos del informe en S3?

- \[ ] Cree un bucket público de S3. Cuando la aplicación cree el objeto de informe en S3, genere dos long generados aleatoriamente
  nombres de carpeta y coloque el archivo dentro de la subcarpeta más profunda. Establezca la política de retención en el objeto en una hora y envíe este enlace por correo electrónico a
  el usuario. El enlace estará activo durante una hora.
- \[ ] Cree un bucket público de S3. Utilice un hash de la dirección de correo electrónico del usuario y la fecha y hora en que se solicitó el informe para generar un
  nombre único del objeto. Envíe este vínculo por correo electrónico al usuario y haga que se ejecute una tarea programada dentro de la aplicación para quitar objetos que son más antiguos
  que siete días.
- \[x] Cree un bucket de S3 privado. El enlace en el correo electrónico debe llevar al usuario a su aplicación, donde puede verificar el usuario activo
  sesión u obligar al usuario a iniciar sesión. Después de comprobar que el usuario tiene derechos para acceder a este archivo, haga que la aplicación recupere el objeto
  desde S3 y devolverlo en la respuesta HTTP. Elimine el archivo del bucket de S3 una vez completada la solicitud.
- \[ ] Cree un bucket de S3 privado. El enlace en el correo electrónico debe llevar al usuario a su aplicación, donde puede verificar el usuario activo
  sesión u obligar al usuario a iniciar sesión. Establezca el objeto de informe en S3 en public. Mostrar al usuario un botón "Descargar" en el navegador que enlaza
  al objeto público.

#### Pregunta 69. Al enviar un gran volumen de correo electrónico a través de SES, ¿cuál es el conjunto de métricas más importante para monitorear?

- \[x] sus quejas y tasas de rebote
- \[ ] se abre y hace clic en
- \[ ] clics y entregas
- \[ ] volumen de envío en los últimos 15 minutos y durante un día para observar los picos de facturación

#### Pregunta 70. Va a alojar una aplicación que utiliza una base de datos MySQL. ¿Qué base de datos debe seleccionar si no desea administrar las tareas de escalado o administración de bases de datos?

- \[ ] Inicie una imagen AMI desde el mercado que contenga un servidor MySQL preconfigurado.
- \[x] Aurora
- \[ ] RDS para MySQL
- \[ ] Corrimiento al rojo

#### P71. Un formulario en una aplicación web está enviando datos de registro a "http://example.com/signup/new?source=web" y estos datos deben ser manejados por un servicio ECS detrás de Application Load Balancer (ALB). ¿Qué regla ALB enrutará esta solicitud?

![image](images/004.png?raw=png)

- \[ ] A

<!---->

    IF (all match)
        Path is /signup*
        Query string is signup:new
    Then
        Forward to ecs-cluse-service <there is a typo - yes!

- \[ ] B

<!---->

    IF (all match)
        Path is /sign/new/&
        Query request method is POST
    Then
        Forward to ecs-cluse-service

- \[ ] C ... Uno más con POST
- \[x] D ... Solo uno con Get

#### P72. ¿Qué servicio de AWS puede alojar el servidor de aplicaciones web para un sitio de WordPress?

- \[ ] S3
- \[x] Elastic BeanStalk
- \[ ] ElasticCache
- \[ ] CloudFront

#### Pregunta 73. ¿Qué hace la siguiente AWS CLI? `create-service` comando para ECS do?

    aws ecs create-service \
     --cluster production \
     --service-name rest-api \
     --task-definition rest-api:1 \
     --desired-count 2 \
     --launch-type "FARGATE" \
     --network-configuration \
     "awsvpcConfiguration={subnets=[subnet-0b29129ab],securityGroups=[sg-0b29129ab]}"

- \[ ] cambia los grupos de seguridad de la ejecución **rest-api** tarea
- \[ ] crea un clúster llamado **producción** y lanza dos contenedores a Fargate con el **rest-api** definición de tareas
- \[x] lanza dos contenedores en Fargate en el existente **producción** clúster mediante el **rest-api** definición de tareas
- \[ ] crea una definición de servicio para el **rest-api** tarea; Coloque dos contenedores en el clúster de producción cuando se inicie **ecs-cli** comando up

#### Pregunta 74. Desea que su API pública sea rápidamente accesible desde todas las regiones. ¿Cuál es la mejor manera de hacerlo?

- \[ ] Cree un único extremo de puerta de enlace de API en una región central.
- \[ ] Cree un punto de enlace de puerta de enlace de API privada para cada región.
- \[ ] Cree un punto de enlace de puerta de enlace de API regional para cada región.
- \[x] Cree puntos de enlace de puerta de enlace de API optimizados para el borde e impleméntelos en una red de CloudFront.

#### Pregunta 75. ¿Qué tipo de solución de datos debe utilizar para los datos procedentes de datos no relacionales y relacionales de dispositivos IoT, sitios web, aplicaciones móviles, etc.?

- \[ ] Amazon DynamoDB
- \[x] Formación de AWS Lake
- \[ ] Amazon Redshift
- \[ ] Aurora amazónica

#### Pregunta 76. Tiene un conjunto de análisis que produce informes sobre los patrones de uso de la aplicación web. Después de completar la migración a AWS y utilizar Application Load Balancer para equilibrar la carga en toda la aplicación web, el departamento de marketing observó que los informes basados en la ubicación del tráfico web solo muestran el tráfico que se origina en una única ubicación. ¿Cuál es el problema?

- \[ ] Utilice un equilibrador de carga clásico, no un equilibrador de carga de aplicaciones.
- \[x] Application Load Balancer no conserva la dirección IP de origen original. El software de análisis debe configurarse para mirar el encabezado de solicitud HTTP 'X-Forwarded-For' para la dirección IP de origen correcta.
- \[ ] Application Load Balencer debe configurarse para conservar la dirección IP de origen del tráfico que está reenviando. Cree una política que habilite la compatibilidad con ProxyProtocol y adjúntela al ALB mediante la AWS CLI.
- \[ ] Configure las instancias EC2 del servidor web para que solo tengan direcciones IP privadas. Las direcciones IP públicas de las instancias se registran en los registros del servidor web, solo al ALB de errores debe tener una interfaz pública y enrutará el tráfico a las instancias a través de la interfaz privada.

#### Pregunta 77. Qué es `not` un usuario predeterminado de una instancia común de Linux lanzada desde una AMI?

- \[ ] ubuntu
- \[x] usuario del sistema
- \[ ] ec2-usuario
- \[ ] admin

[Referencia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)

#### Pregunta 78. Ha replicado la infraestructura que sirve a la API de back-end para su aplicación web en todas las regiones para servir mejor a sus clientes en los EE. UU. y la UE. ¿Cuál es la mejor manera de dirigir su aplicación web al centro de datos más cercano?

- \[x] Utilice Route 53 con búsquedas de geolocalización para dirigir el tráfico entre las dos regiones.
- \[ ] Cree una regla de redirección WAF que redirija el tráfico en el centro de datos de la UE si la IP de origen proviene de ciertos países.
- \[ ] Compre una extensión de dominio de país y dirija a sus usuarios al sitio correcto, como example.com y example.co
- \[ ] Haga que su aplicación front-end pruebe la latencia entre cada centro de datos y use el centro de datos que responde más rápido.

[Referencia](https://aws.amazon.com/premiumsupport/knowledge-center/geolocation-routing-policy/)

#### Pregunta 79. Recientemente ha lanzado su nuevo producto web y espera 1,000 nuevos usuarios cada mes. Sin embargo, acaba de recibir la noticia del CEO de que su producto se presentará en una próxima conferencia cubierta por varios medios de comunicación, y esto podría llevar a 20,000 nuevos usuarios durante la próxima semana. ¿Cómo planea un aumento repentino en el tráfico?

- \[ ] Replique su infraestructura en dos regiones. Endurecerá la aplicación a un fallo regional y duplicará su capacidad.
- \[ ] Tome una imagen AMI de un servidor front-end para guardar la configuración y, a continuación, agregue más servidores al cluster pror a la conferencia. Quite los servidores del clúster después del pico de la conferencia.
- \[ ] Prueba para determinar su rendimiento y cuántos usuarios puede admitir. Desarrolle un plan de escalado para su front-end, microservicios y base de datos basado en métricas de CloudWatch que se alineen con los cuellos de botella probados.
- \[x] Utilice grupos de Auto Scaling para crear más servidores front-end cuando las métricas de CloudWatch para el uso de CPU en una sola instancia superen el 80 % durante cinco minutos.

[Referencia](https://aws.amazon.com/ec2/autoscaling/)

#### Pregunta 80. ¿Cómo se conecta a través de SSH a una instancia EC2 de Linux con un volumen de EBS si perdió su par de claves?

- \[ ] Detenga la instancia y cree una imagen AMI. Inicie la imagen con un nuevo par de claves.
- \[ ] Póngase en contacto con el soporte técnico de AWS. Un especialista de soporte puede restaurar de forma remota el acceso a su instancia y enviarle un nuevo par de claves.
- \[ ] No puede conectarse a esta instancia EC2. El par de claves se muestra solo una vez. Si lo pierde, habrá perdido todo el acceso a esta instancia. Conecte el volumen de EBS a otra instancia para recuperar los archivos.
- \[x] Adjunte el volumen de EBS a una instancia temporal lanzada con un nuevo par de claves y sobrescriba ~/.ssh/authorized_keys utilizando el mismo archivo de la nueva instancia.

[Referencia](https://medium.com/the-10x-dev/how-to-recover-access-login-to-your-aws-instance-after-losing-your-pem-keypair-file-e0d31bae2da4)

#### Pregunta 81. Su centro de datos local (172.16.128.0/24) ya está conectado a su AWS VPC (10.0.0.0/16) mediante una gateway de cliente. Desea conectar otro centro de datos para una empresa que acaba de adquirir (172.16.130.0/24) a su VPC como se muestra en la imagen. ¿Cuál es la mejor manera de crear este enlace?

![image](images/Q80.png?raw=png)

- \[ ] Establezca una conexión entre sus dos centros de datos y conecte el segundo centro de datos al primero a través de un túnel privado. El tráfico fluirá desde el segundo centro de datos y luego a través de los primeros datos, y luego a AWS.
- \[ ] Cree una segunda puerta de enlace de cliente y configure su cliente VPN en su segundo centro de datos para conectarse a la puerta de enlace privada virtual.
- \[x] Cree una segunda puerta de enlace privada virtual (VPG) y conéctela a la VPC. Cree una puerta de enlace de cliente para la nueva puerta de enlace privada virtual y use su cliente VPN en su segundo centro de datos para establecer una conexión con el VPG.
- \[ ] No puede tener más de una puerta de enlace de cliente por VPC, por lo que la solución propuesta no funcionará. Cree una segunda VPC con una puerta de enlace privada virtual y una puerta de enlace de cliente. Conecte las dos VPC mediante el emparejamiento de VPC.

#### P82. Está migrando una base de datos de 200 GB de un servidor SQL Server local a RDS para SQL Server. La base de datos debe tener un tiempo de inactividad mínimo durante la migración. ¿Cuál es la práctica recomendada para migrar esta base de datos?

- \[ ] Cierre todas las conexiones existentes a la base de datos de SQL Server y use el Servicio de migración de bases de datos para transferir los datos a RDS.
- \[x] Utilice el Servicio de migración de bases de datos para replicar la base de datos en RDS y mantenerla sincronizada durante la migración. Reoriente las aplicaciones para que usen el nuevo extremo de RDS.
- \[ ] Separe la base de datos de SQL Server durante la migración. Realice una copia de seguridad de la base de datos y utilice SQ con transferencia acelerada para cargar las copias de seguridad en S3. Restaure las copias de seguridad en la instancia de RDS.
- \[ ] Utilice el Asistente para importación y exportación del Administrador corporativo de SQL Server para crear una tarea de exportación y exportar las tablas a la instancia de RDS.

[Referencia](https://aws.amazon.com/dms/)

#### Pregunta 83. Ha habilitado la autenticación multifactor (MFA) para su cuenta raíz de AWS y ha perdido su dispositivo MFA. ¿Qué necesita hacer para recuperar el acceso a su cuenta?

- \[ ] No puede recuperar el acceso a su cuenta raíz de AWS. Póngase en contacto con el soporte técnico de AWS.
- \[x] Se enviará un correo electrónico a la dirección de correo electrónico registrada para verificar la propiedad de la cuenta. A continuación, deberá proporcionar el número de teléfono en la cuenta.
- \[ ] Se enviará un correo electrónico a la dirección de correo electrónico registrada. Después de hacer clic en el enlace de su correo electrónico, proporcione uno de los códigos de recuperación de MFA que se crearon cuando MFA estaba habilitado.
- \[ ] Utilice la AWS CLI con el token de acceso a la cuenta raíz para deshabilitar MFA en la cuenta raíz. A continuación, utilice la CLI para establecer una nueva contraseña en la cuenta raíz.

[Referencia](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html)

#### Pregunta 84. ¿Cómo se asigna una IP elástica a varias instancias EC2?

- \[ ] En el panel de la VPC, haga clic en Elastic IPs. Seleccione la IP elástica y haga clic en Asociar dirección. Seleccione cada instancia EC2 a la que desee asignar esta dirección.
- \[ ] En el panel de EC2, haga clic en Instancia EC2. En Acciones, seleccione > Administrar direcciones IP. haga clic para agregar una nueva dirección IP y escriba la dirección de la IP elástica. Repita el proceso para cada instancia EC2 a la que desee asignar esta IP elástica.
- \[ ] Utilice la AWS CLI y pase varias opciones '--instance-id' al comando aws ec2 assosiate-address.
- \[x] No se puede asignar una IP elástica a varias instancias EC2. Solo se puede asociar a una sola instancia EC2.

[Referencia](https://stackoverflow.com/questions/54742522/assign-multiple-ec2-instances-to-one-elastic-ip)

#### Pregunta 85. Ha creado una VPC que tiene una subred pública y una subred privada. Se colocó un servidor web en la subred pública y un servidor de base de datos en la subred privada. El servidor web puede conectarse al servidor de base de datos; sin embargo, el servidor de base de datos en 10.0.1.2 no puede obtener actualizaciones de software. ¿Cuál es la causa de este problema?

- \[x] No hay una puerta de enlace NAT para la subred privada, por lo que el servidor de base de datos no tiene rutas que le den acceso público a Internet para descargar actualizaciones de software.
- \[ ] Al servidor de base de datos se le debe asignar una dirección pública del grupo o asignar una IP elástica similar a la instancia 10.0.0.2.
- \[ ] El router no está configurado correctamente en la VPC. Agregue una tabla de ruta a ruta para la VPC que enruta todo el tráfico de 0.0.0.0/0 al ID de la puerta de enlace de Internet.
- \[ ] No hay ninguna puerta de enlace de Internet de salida conectada a la subred privada de la VPC.

#### Pregunta 86. ¿Beneficio de usar S3 Glacier?

- \[ ] tiempo de acceso
- \[ ] almacenar por pequeña duración
- \[x] costo
- \[ ] interregional
