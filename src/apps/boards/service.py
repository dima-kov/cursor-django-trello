from apps.boards.models import Task


class ProtectedTaskDelete(Exception):
    pass


def delete_task(task):
    if task.protected:
        raise ProtectedTaskDelete()
    else:
        task.status = Task.STATUS_ARCHIVED
