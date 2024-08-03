class SecondaryDatabaseRouter:
    def db_for_read(self, model, **hints):
        """
        Directs read operations for models in the specified app to the secondary database.
        """
        if model._meta.app_label == 'broker':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        """
        Directs write operations for models in the specified app to the secondary database.
        """
        if model._meta.app_label == 'broker':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allows relations between models in the specified app.
        """
        if obj1._meta.app_label == 'broker' or obj2._meta.app_label == 'broker':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Restricts migrations to the specified app in the secondary database.
        """
        if app_label == 'broker':
            return db == 'secondary'
        return None