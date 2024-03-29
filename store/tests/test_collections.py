from rest_framework.test import APIClient
from rest_framework import status
import pytest
from store.models import Collection, Product
from django.contrib.auth.models import User
from model_bakery import baker


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    
    def test_if_user_anonymous_returns_401(self):
        # AAA (Arrange, Act, Assert)

        #Arrange

        #Act sd
        client = APIClient()
     
        response = client.post('/store/collections/', {'title': 'a'})

        #Assert

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_not_admin_returns_403(self):
        # AAA (Arrange, Act, Assert)

        #Arrange

        #Act sd
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})

        #Assert

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_invalid_returns_400(self):
        # AAA (Arrange, Act, Assert)

        #Arrange

        #Act sd
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title': ''})

        #Assert

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_valid_returns_201(self, api_client, create_collection):
        # AAA (Arrange, Act, Assert)

        #Arrange

        #Act sd
        api_client.force_authenticate(user=User(is_staff=True))

        response = create_collection({'title': 'a'})
        #Assert

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)
        # baker.make(Product, collection=collection, _quantity=10)

        response = api_client.get(f'/store/collections/{collection.id}/')


        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0,
        }
