from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Bug

class BugModelTest(TestCase):
    def setUp(self):
        current_date = timezone.now()
        self.bug = Bug.objects.create(
                title="Test Bug",
                description="This is a test bug.",
                priority="High",
                status="Open",
                report_date=current_date
            )

    def test_bug_title(self):
        self.assertEqual(self.bug.title, "Test Bug")

    def test_bug_description(self):
        self.assertEqual(self.bug.description, "This is a test bug.")

    def test_bug_priority(self):
        self.assertEqual(self.bug.priority, "High")

    def test_bug_status(self):
        self.assertEqual(self.bug.status, "Open")



class BugViewTests(TestCase):
    def setUp(self):
        current_date = timezone.now()
        self.bug = Bug.objects.create(
                title="Test Bug",
                description="This is a test bug",
                bug_type="error",
                report_date=current_date,
                status="TO DO"
        )

    def test_view_bug(self):
        response = self.client.get(reverse('bug:view_bug', args=(self.bug.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")
        self.assertContains(response, "This is a test bug")

    def test_view_bug_not_found(self):
        non_existent_bug_id = self.bug.id + 1
        response = self.client.get(reverse('bug:view_bug', args=(non_existent_bug_id,)))
        self.assertEqual(response.status_code, 404)

    def test_register_bug(self):
        response = self.client.get(reverse('bug:register_bug'))
        self.assertEqual(response.status_code, 200)

