from django.db import connection


class EsusRouter:
    """
    A router to control all database operations on models in the
    esus application.
    """
    route_app_labels = {'esus'}
    allowed_models = {'tbpais', 'tbuf', 'tblocalidade', 'tblogradouro'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to esus_readonly.
        """

        if model._meta.app_label in self.route_app_labels:
            # if connection.tenant is not None:
            #     try:
            #         secretaria = models.Secretaria.objects.get(
            #             tenant=connection.tenant)
            #         if secretaria.database_slug is not None and secretaria.database_slug != "default" and secretaria.database_slug != "":
            #             return secretaria.database_slug
            #     except Exception as e:
            #         pass

            return 'esus'

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write esus models go to esus_readonly.
        """
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the esus app is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the esus app only appear in the
        'esus_readonly' database.
        """

        if app_label in self.route_app_labels:
            return False
        
        return None
