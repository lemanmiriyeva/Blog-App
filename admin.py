
from flask_admin.contrib.sqla import ModelView

class AuthorsAdmin(ModelView):
    can_view_details=True

class CategoriesAdmin(ModelView):
    can_view_details=True

class PostsAdmin(ModelView):
    can_view_details=True
    column_exclude_list=['img']

class StatusAdmin(ModelView):
    can_view_details=True