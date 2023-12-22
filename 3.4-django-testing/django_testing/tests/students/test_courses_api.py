import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs, make_m2m=True)

    return factory()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs, make_m2m=True)

    return factory()


@pytest.mark.django_db
def test_api_get_first_course(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.get('/courses/')

    data = response.json()
    assert data['name'] == courses.name

