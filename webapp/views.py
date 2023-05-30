from django.shortcuts import render

#   Diccionarios para los animes

animes = [
    {'anime': 'Naruto', 'descripcion': '¡Bienvenido a la increíble aventura de "Naruto"! Creado por Masashi Kishimoto, este apasionante anime y manga te transportará a un mundo lleno de ninjas, poderes sobrenaturales y emocionantes batallas. Acompaña a Naruto Uzumaki, un joven ninja hiperactivo y bromista, en su búsqueda para convertirse en el Hokage, líder supremo de su aldea. Con un zorro de nueve colas sellado en su interior, Naruto se enfrentará a desafíos tanto internos como externos, uniendo fuerzas con sus amigos Sakura y Sasuke. Juntos, lucharán contra villanos temibles y organizaciones criminales, mientras exploran temas de amistad, superación y sacrificio. Sumérgete en un universo repleto de acción trepidante, técnicas ninja asombrosas y momentos emocionales inolvidables. ¡Únete a Naruto en su camino hacia la grandeza y déjate cautivar por esta increíble historia!'},
    {'anime': 'One Pice', 'descripcion': '"One Piece" es un emocionante anime y manga creado por Eiichiro Oda que te sumergirá en un vasto y fascinante mundo de aventuras piratas. La historia sigue a Monkey D. Luffy, un joven intrépido y extrovertido que busca el tesoro definitivo conocido como el "One Piece", que se encuentra en la legendaria Grand Line. Acompañado por su variado y valiente grupo de amigos, la tripulación de los Sombrero de Paja, Luffy navega por mares peligrosos, desafiando a poderosos enemigos, descubriendo islas exóticas y luchando por sus sueños y la libertad. Con una combinación única de acción trepidante, personajes carismáticos y un toque de comedia, "One Piece" te llevará a un viaje épico lleno de emociones, amistad, lealtad y valentía. Prepárate para zarpar hacia una aventura inolvidable que te mantendrá enganchado desde el primer momento y te dejará ansioso por descubrir los secretos que guarda el océano. ¡Únete a Luffy y su tripulación en esta increíble odisea por el mundo de "One Piece"!'}
]

# Create your views here.

def webapp(request):
    return render(request, 'webapp/index.html')