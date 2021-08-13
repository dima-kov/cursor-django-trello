from django.contrib.auth.decorators import login_required
from django.db.models import Count, Prefetch
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from apps.boards.models import Board, Comment, Task


class CreateCommentView(generic.CreateView):
    model = Comment
    fields = ["message"]

    template_name = 'boards/create_comment_form.html'
    success_url = reverse_lazy('home:home-page')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.task = self.request.user.tasks.last()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteComment(generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('home:home-page')
    template_name = 'boards/delete_comments.html'

    def get_queryset(self):
        return super(DeleteComment, self).get_queryset().filter(created_by=self.request.user)


class BoardDetailView(generic.DetailView):
    model = Board
    context_object_name = 'board'
    template_name = 'boards/board-page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BoardDetailView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        prefetch_tasks = Prefetch(
            'cols__tasks',
            queryset=Task.objects.select_related('col') \
                .prefetch_related('comments')
                .annotate(comments_count=Count('comments')) \
                .exclude(status=Task.STATUS_ARCHIVED)
        )
        return super(BoardDetailView, self).get_queryset() \
            .select_related('owner') \
            .prefetch_related('users', 'cols', prefetch_tasks) \
            .filter(users=self.request.user)
