from django import template
from Glance_Skills_App.models import Projects_Comment,Project
register = template.Library()

@register.filter(name='is_upper')
def upper(value,project_id):
  mypost = Project.objects.get(id=project_id)
  comments_count = Projects_Comment.objects.filter(project=mypost).count()
  return comments_count

