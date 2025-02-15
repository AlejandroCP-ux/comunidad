# urls.py

from django.urls import include, path
from django.contrib.auth import views as auth_views
from comunidad import settings
from . import views
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('crear_comunidad/', views.crear_comunidad, name='crear_comunidad'),
    path('comunidad/<slug:slug>/', views.detalle_comunidad, name='detalle_comunidad'),
    path('comunidades/', views.lista_comunidades, name='lista_comunidades'),
    path('comunidad/<slug:slug>/crear_proyecto/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<slug:slug>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('comunidad/<slug:slug>/crear_desafio/', views.crear_desafio, name='crear_desafio'),
    path('desafio/<slug:slug>/', views.detalle_desafio, name='detalle_desafio'),
    path('buscar/', views.buscar, name='buscar'),
    path('chat/<int:receptor_id>/', views.chat, name='chat'),
    path('ranking/', views.ranking_usuarios, name='ranking'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    path('publicaciones/', views.obtener_publicaciones_no_vistas, name='publicaciones'),
    path('publicaciones/<int:publicacion_id>/vista/', views.registrar_publicacion_vista, name='registrar_publicacion_vista'),
    path('comunidad/<slug:slug>/crear-publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('ws/chat/<int:receptor_id>/', views.ChatWS.as_asgi(), name='chat_ws'),
    path('aceptar-terminos/', views.aceptar_terminos, name='aceptar_terminos'),
    path('aceptar-terminos-registro/', views.aceptar_terminos_registro, name='aceptar_terminos_registro'),
    path('seguir/<slug>/', views.seguir_usuario, name='seguir_usuario'),
    path('dejar_de_seguir/<pk>/', views.dejar_de_seguir_usuario, name='dejar_de_seguir_usuario'),
    path('buscar_usuarios/', views.buscar_usuarios, name='buscar_usuarios'),
    path('actions/<int:action_id>/', views.update_user_points, name='action'),
    path('crear_concurso/', views.crear_concurso, name='crear_concurso'),
    path('concurso_resultados/', views.concurso_resultados, name='concurso_resultados'),
    path('campaign/<slug:slug>/', views.detalle_campaign, name='detalle_campaign'),
    path('comunidad/<slug:slug>/campaigns/', views.lista_campaigns, name='lista_campaigns'),
    path('comunidad/<slug:slug>/proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('perfil/<str:username>/publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('comunidad/<slug:slug>/miembros/', views.lista_miembros, name='lista_miembros'),
    path('puntuar/<int:pk>/<int:estrellas>/', views.puntuar_respuesta, name='puntuar_respuesta'),
    path('desafio/<int:desafio_id>/like/', views.like_desafio, name='like_desafio'),
    path('desafio/<int:desafio_id>/like/<int:comentario_id>', views.like_comentariod, name='like_respuesta'),
    path('comentar/<pk>/', views.crear_comentario, name='crear_comentario'),
    path('lista_publicaciones/comentar/<pk>/', views.crear_comentario_pub, name='crear_comentario_pub'),
    path('comentar_proyecto/<pk>/', views.crear_comentario_pro, name='crear_comentario_pro'),
    path('publicacion/<int:pk>/like/', views.like, name='like_publicacion'),
    path('comentario/<int:pk>/like/', views.like_comentario, name='like_comentario'),
    path('campaign/<slug:slug>/donar', views.guardar_donacion, name='guardar_donacion'),
    path('chat-comunidad/<slug:slug>/', views.chat_comunidad, name='chat_comunidad'),
    path('desafio/<slug:slug>/donar/', views.guardar_donacion, name='guardar_donacion'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('comunidad/<slug:slug>/unirse/', views.unirse_comunidad, name='unirse_comunidad'),
    path('comunidad/<slug:slug>/solicitar/', views.solicitar_membresia, name='solicitar_membresia'),
    path('solicitar_crowdsourcer/', views.solicitar_crowuser, name='solicitar_crowuser'),
    path('comunidad/<slug:slug>/salir/', views.salir_comunidad, name='salir_comunidad'),
    path('donaciones/', views.ver_donaciones, name='ver_donaciones'),
    path('no_me_gusta/<tematica>/', views.no_me_gusta, name='no_me_gusta'),
    path('editar_proyecto/<slug:slug>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<slug:slug>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('my_logout/', views.my_logout, name='my_logout'),
    path('publicacion/comentario/<int:pk>/editar', views.editar_comentario_publicacion, name='editar_comentario_publicacion'),
    path('proyecto/comentario/<int:pk>/editar', views.editar_comentario_proyecto, name='editar_comentario_proyecto'),
    path('publicacion/<int:pk>/editar', views.editar_publicacion, name='editar_publicacion'),
    path('marketplace/', views.marketplace, name='marketplace'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
