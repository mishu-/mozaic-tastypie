from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from mozaictodo.models import TodoItem


class TodoItemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
        resource_name = 'todo'
        authorization= Authorization()