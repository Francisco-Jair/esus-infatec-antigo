from django.urls import path

from indicadores_esus.core import views

app_name = "core"


urlpatterns = [
    path("", views.home_dashboard, name="home"),
    path("tabela_view/", views.TabelaView.as_view(), name="tabela_dados"),
    path("user_data/", views.UserView.as_view(), name="user_dados"),
    path("links_uteis/", views.LinksUteisVew.as_view(), name="links_uteis"),
    path(
        "filtro_gestantes/", views.FiltroGestantesVew.as_view(), name="filtro_gestantes"
    ),
    path("acs_maps/", views.ACSRotaView.as_view(), name="acs-rota"),
    path("filtro/", views.FiltroAllVew.as_view(), name="filtro_all"),
    path("busca_cidadao/", views.search_citizen, name="search_citizen"),
    path("busca_cidadao_htmx/", views.search_citizen, name="citizen_list_htmx"),
    ### GESTANTES ###
    path("lista_gestantes/", views.pregnant_women_list, name="pregnant_list"),
    path("lista_gestantes_htmx/", views.pregnant_women_list, name="pregnant_list_htmx"),
    path("detalhes_gestante/<int:pk>/", views.pregnant_detail, name="pregnant_detail"),
    path(
        "imprime_gestantes/",
        views.print_pregnant_woman_list,
        name="print_pregnant_list",
    ),
    path(
        "imprime_detalhes_gestante/<int:pk>/",
        views.print_pregnant_detail,
        name="print_pregnant_detail",
    ),
    ### MULHERES ###
    path("lista_mulheres/", views.women_list, name="women_list"),
    path("lista_mulheres_htmx/", views.women_list, name="women_list_htmx"),
    path("detalhes_mulher/<int:pk>/", views.woman_detail, name="woman_detail"),
    path("imprime_mulheres/", views.print_women_list, name="print_women_list"),
    path(
        "imprime_detalhes_mulher/<int:pk>/",
        views.print_woman_detail,
        name="print_woman_detail",
    ),
    ### CRIANÇAS ###
    path("lista_criancas/", views.children_list, name="children_list"),
    path("lista_criancas_htmx/", views.children_list, name="children_list_htmx"),
    path("detalhes_crianca/<int:pk>/", views.child_detail, name="child_detail"),
    path("imprime_criancas/", views.print_children_list, name="print_children_list"),
    path(
        "imprime_detalhes_crianca/<int:pk>/",
        views.print_child_detail,
        name="print_child_detail",
    ),
    ### HIPERTENSOS ###
    path("lista_hipertensos/", views.hypertensives_list, name="hypertensives_list"),
    path(
        "lista_hipertensos_htmx/",
        views.hypertensives_list,
        name="hypertensives_list_htmx",
    ),
    path(
        "detalhes_hipertenso/<int:pk>/",
        views.hypertensive_detail,
        name="hypertensive_detail",
    ),
    path(
        "imprime_hipertensos/",
        views.print_hypertensives_list,
        name="print_hypertensive_list",
    ),
    path(
        "imprime_detalhes_hipertenso/<int:pk>/",
        views.print_hypertensive_detail,
        name="print_hypertensive_detail",
    ),
    ### DIABÉTICOS ###
    path("lista_diabeticos/", views.diabetics_list, name="diabetics_list"),
    path("lista_diabeticos_htmx/", views.diabetics_list, name="diabetics_list_htmx"),
    path("detalhes_diabetico/<int:pk>/", views.diabetic_detail, name="diabetic_detail"),
    path("imprime_diabeticos/", views.print_diabetics_list, name="print_diabetic_list"),
    path(
        "imprime_detalhes_diabetico/<int:pk>/",
        views.print_diabetic_detail,
        name="print_diabetic_detail",
    ),
]
