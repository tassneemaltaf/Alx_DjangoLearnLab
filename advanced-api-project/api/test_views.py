from django.test import APITestCase
from rest_framework import status

class ApiTests(APITestCase):
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
    self.assertEqual(response.data['title'], 'New Book')

  def test_detail_view(self):
    response = self.client.get("books/<int:pk>/")
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_view(self):
    #Test if user is logged in
    login_success = self.client.login(username="testuser", password="testpass")
    self.assertTrue(login_success, "Login failed")
    updated_data = {'title': 'Updated Title', 'publication_year': 2023, 'author': 'Tass'}

    response = self.client.put("books/update/<int:pk>", updated_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_delete_view(self):
    response = self.client.delete("books/delete/<int:pk>")
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)