# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    # Relación Uno-a-Uno con User de Django
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,  # Si se borra User, se borra Avatar
        related_name='avatar'      # Para acceder desde User: user.avatar
    )
    
    # Campos personalizados
    nombre_en_juego = models.CharField(
        max_length=50,
        unique=True,               # No puede haber dos avatares con mismo nombre
        help_text="Tu nombre público en SociaQuest"
    )
    
    # Stats RPG sociales
    nivel = models.IntegerField(
        default=1,
        help_text="Nivel de experiencia social"
    )
    xp = models.IntegerField(
        default=0,
        help_text="Puntos de experiencia acumulados"
    )
    carisma = models.IntegerField(
        default=1,
        help_text="Habilidad para socializar"
    )
    empatia = models.IntegerField(
        default=1, 
        help_text="Habilidad para entender a otros"
    )
    
    # Apariencia
    estilo_avatar = models.CharField(
        max_length=20,
        choices=[          # Opciones predefinidas
            ('aventurero', 'Aventurero'),
            ('elegante', 'Elegante'), 
            ('geek', 'Geek'),
            ('deportista', 'Deportista')
        ],
        default='aventurero'
    )
    color_principal = models.CharField(
        max_length=7,  # Para código HEX: #FF5733
        default='#4A90E2'
    )
    
    # Ubicación actual
    sala_actual = models.ForeignKey(
        'world.Sala',           # 'app.Modelo' para referencias entre apps
        on_delete=models.SET_NULL,  # Si se borra la sala, queda NULL
        null=True,
        blank=True
    )
    
    # Fechas automáticas
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    # Metadata adicional
    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
        ordering = ['-nivel', 'nombre_en_juego']  # Ordenar por nivel descendente
    
    # Representación en string
    def __str__(self):
        return f"{self.nombre_en_juego} (Nv. {self.nivel})"
    
    # Métodos personalizados
    def agregar_xp(self, cantidad):
        """Añade experiencia y checkea subida de nivel"""
        self.xp += cantidad
        while self.xp >= self.nivel * 100:  # 100 XP por nivel
            self.subir_nivel()
        self.save()
    
    def subir_nivel(self):
        """Sube de nivel y mejora stats"""
        self.nivel += 1
        self.carisma += 1
        self.empatia += 1
        # Puedes añadir notificaciones aquí después