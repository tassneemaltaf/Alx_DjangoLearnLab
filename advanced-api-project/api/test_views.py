from django.test import TestCase
from rest_framework import status

class ApiTests(TestCase):
  def setUp(self):
    return super().setUp()
  
  def tearDown(self):
    return super().tearDown()
  
  def test_list_view(self):
    response = self.client.get("/books/")

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_create_view(self):
    data = {'title' : 'This', 'publication_year' : 2023, 'author' : 'Tass'}

    response = self.client.post("/books/create/", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_detail_view(self):
    response = self.client.get("books/<int:pk>/")
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_view(self):
    updated_data = {'title': 'Updated Title', 'publication_year': 2023, 'author': 'Tass'}

    response = self.client.put("books/update/<int:pk>", updated_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_delete_view(self):
    response = self.client.delete("books/delete/<int:pk>")
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)