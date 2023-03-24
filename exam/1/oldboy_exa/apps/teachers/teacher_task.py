# author:liu_ll
# from celery_task import app
# @app.task
def update_test_bank(id):
    from teachers.models import TestBank
    TestBank.objects.filter(pk=id).update(is_end=True)
    return 'success'
