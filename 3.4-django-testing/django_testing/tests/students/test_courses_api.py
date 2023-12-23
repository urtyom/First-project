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

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs, make_m2m=True)

    return factory


@pytest.mark.django_db
def test_api_get_first_course(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.get('/courses/')

    data = response.json()
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_api_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/courses/')

    data = response.json()
    assert type(data) == type(courses) == list


@pytest.mark.django_db
def test_api_get_filter_id_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/courses/')

    data = response.json()
    random_course = data[0]
    course_id = random_course['id']

    response = client.get('/courses/?id='+str(course_id))

    filtered_courses = response.data

    assert len(filtered_courses) == 1
    assert filtered_courses[0]['id'] == course_id


@pytest.mark.django_db
def test_api_get_filter_name_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/courses/')

    data = response.json()
    random_course = data[0]
    course_name = random_course['name']

    response = client.get('/courses/?name='+str(course_name))

    filtered_courses = response.data

    assert len(filtered_courses) == 1
    assert filtered_courses[0]['name'] == course_name


from django.urls import reverse


@pytest.mark.django_db
def test_api_update_courses(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[0].id

    update_data = {
        'name': "Новое название курса",
    }

    url = f'/courses/{course_id}/'
    response = client.patch(url, data=update_data)

    assert response.status_code == 200

    updated_course = response.data

    assert updated_course['name'] == update_data['name']


@pytest.mark.django_db
def test_api_delete_course(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[0].id

    url = f'/courses/{course_id}/'
    response = client.delete(url)

    assert response.status_code == 204

    with pytest.raises(Course.DoesNotExist):
        Course.objects.get(id=course_id)
