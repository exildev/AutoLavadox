from django.conf.urls import url
import views


# url ws de tipo de servicios porvehiculo
urlpatterns = [
    url(r'^ws/tipo/servicio/$', views.TiposServicios.as_view(), name='ws_tipo_servicio'),
    url(r'^ws/tipo/servicio/por/asignar/$', views.TiposServiciosPorAplicar.as_view(), name='ws_tipo_servici_a_realizar'),
]

# url de registro, edicion de orden
urlpatterns += [
    url(r'^add/orden/$', views.AddOrdenForm.as_view(), name='addorden'),
    url(r'^edit/orden/(?P<pk>\d+)/$', views.AddOrdenForm.as_view(), name='editorden'),
    url(r'^close/orden/(?P<pk>\d+)/$', views.CloseOrden.as_view(), name='closeorden'),
]

# lista de servicion por orden
urlpatterns += [
    url(r'^ws/servicios/orden/$', views.WsServiciosOrden.as_view(), name='wsservorden'),
]

# lista de servicion por orden
urlpatterns += [
    url(r'^add/servicio/$', views.AddServicio.as_view(), name='addservicio'),
    url(r'^edit/servicio/(?P<pk>\d+)/$', views.AddServicio.as_view(), name='editservicio'),
    url(r'^ok/servicio/(?P<pk>\d+)/$', views.OkService.as_view(), name='okservice'),
    url(r'^cancel/servicio/(?P<pk>\d+)/$', views.CancelService.as_view(), name='okservice'),
]


# url de ordenes pendientes
urlpatterns += [
    url(r'^get/ordenes/pendientes/$', views.GetOrdenesPendientes.as_view(), name='get_orden_pendien'),
]



# url de ordenes pendientes
urlpatterns += [
    url(r'^imprimir/orden/(?P<pk>\d+)/$', views.ImprimirOrden.as_view(), name='get_orden_pendien'),
    url(r'^ws/imprimir/orden/$', views.ServiciosOrden.as_view(), name='ws_imp_orden'),
]