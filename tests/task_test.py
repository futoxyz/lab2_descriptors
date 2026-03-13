import pytest
from time import sleep
from src.task import Task


def test_tasks() -> None:
    '''
    Тесты дескрипторов.
    '''
    with pytest.raises(ValueError): # Id and description test
        task = Task("", "description")
    with pytest.raises(TypeError):
        task = Task(0, "description")
    with pytest.raises(ValueError):
        task = Task("some_id", "")
    with pytest.raises(TypeError):
        task = Task("some_id", 1)

    with pytest.raises(ValueError): # Priority test
        task = Task("some_id", "description", -1)
    with pytest.raises(TypeError):
        task = Task("some_id", "description", "priority_1")

    normal_task = Task("id_1", "description", 1)
    assert normal_task.status == "pending"
    with pytest.raises(ValueError):
        normal_task.status = "can't be a status"
    with pytest.raises(ValueError):
        normal_task.status = 1010101
    normal_task.status = "in_progress"
    assert normal_task.status == "in_progress"

    with pytest.raises(ValueError):
        normal_task.priority = -1
    with pytest.raises(TypeError):
        normal_task.priority = "string"


def test_age_measurement() -> None:
    task = Task("id", "description")
    time_exist: float = 0.75
    sleep(time_exist)
    assert abs(task.age_seconds - time_exist) < 0.5 # Погрешность