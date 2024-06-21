from django.contrib.auth.models import User, Group, Permission
from django.test import TestCase, Client
from django.urls import reverse
from .models import StickyNote

# Create your tests here.
class StickyNoteModelTest(TestCase):
    def setUp(self):
        StickyNote.objects.create(title='Test Post Title', content='This is a test post.', author='Test Author')

    def test_note_has_title(self):
        test_note = StickyNote.objects.get(id=1)
        self.assertEqual(test_note.title, 'Test Post Title')

    def test_note_has_content(self):
        test_note = StickyNote.objects.get(id=1)
        self.assertEqual(test_note.content, 'This is a test post.')

class StickyNoteViewsTest(TestCase):
    def setUp(self):
        # Create the required group
        self.group_name = 'test_group'
        self.group = Group.objects.create(name=self.group_name)

        # Create a user and set password
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Assign the user to the group
        self.user.groups.add(self.group)

        # Assign necessary permissions to the group
        add_permission = Permission.objects.get(codename='add_stickynote')
        change_permission = Permission.objects.get(codename='change_stickynote')
        delete_permission = Permission.objects.get(codename='delete_stickynote')
        self.group.permissions.add(add_permission, change_permission, delete_permission)

        # Log in the user
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        # Create a test note
        self.note = StickyNote.objects.create(title='Test Post Title', content='This is a test post.', author=self.user.username)

    def test_view_all_notes(self):
        response = self.client.get(reverse('view_all_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')

    def test_view_note(self):
        response = self.client.get(reverse('view_note', args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')
        self.assertContains(response, 'This is a test post.')

    def test_edit_note(self):
        response = self.client.get(reverse('edit_note', args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')
        self.assertContains(response, 'This is a test post.')

        updated_note = {
            'title': 'Updated Title',
            'content': 'This is an updated note',
            'author': 'There is an author now'
        }

        response = self.client.post(reverse('edit_note', args=[str(self.note.id)]), updated_note)
        self.assertEqual(response.status_code, 302)  # Redirection after successful edit

        response = self.client.get(reverse('view_note', args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Updated Title')
        self.assertContains(response, 'This is an updated note')
        self.assertContains(response, 'There is an author now')
