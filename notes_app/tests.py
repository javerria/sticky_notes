from django.test import TestCase
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
        StickyNote.objects.create(title='Test Post Title', content='This is a test post.')

    def test_view_all_notes(self):
        response = self.client.get(reverse('view_all_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')

    def test_view_note(self):
        test_note = StickyNote.objects.get(id=1)
        response = self.client.get(reverse('view_note', args=[str(test_note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')
        self.assertContains(response, 'This is a test post.')

    def test_edit_note(self):
        test_note = StickyNote.objects.get(id=1)
        response = self.client.get(reverse('view_note', args=[str(test_note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post Title')
        self.assertContains(response, 'This is a test post.')

        updated_note = {
            'title' : 'Updated Title',
            'content' : 'This is an updated note',
            'author' : 'There is an author now'
        }

        response = self.client.post(reverse('edit_note', args=[str(test_note.id)]), updated_note)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('view_note', args=[str(test_note.id)]))
        self.assertEqual(response.status_code, 200)

        test_note.refresh_from_db()        
        self.assertContains(response, 'Updated Title')
        self.assertContains(response, 'This is an updated note')
        self.assertContains(response, 'There is an author now')