from django.test import TestCase
from .models import Bug

class BugModelTest(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
                description="Test bug",
                bug_type="Error",
                report_date="2023-10-14",
                status="To do"
                )

    def test_bug_creation(self):
        """
            Test that a Bug instance is created correctly.
        """
        self.assertEqual(self.bug.description, "Test bug")
        self.assertEqual(self.bug.bug_type, "Error")
        self.assertEqual(self.bug.report_date, "2023-10-14")
        self.assertEqual(self.bug.status, "To do")

    def test_bug_string_representation(self):
        """
            Test the string representation of a Bug instance.
        """
        self.assertEqual(str(self.bug), "Test bug (Error)")

    def test_bug_status_change(self):
        """
            Test changing the status of a Bug.
        """
        self.bug.status = "In progress"
        self.bug.save()
        updated_bug = Bug.objects.get(id=self.bug.id)
        self.assertEqual(updated_bug.status, "In progress")

    def test_bug_bug_type_choices(self):
        """
        Test that bug_type choices are respected.
        """
        with self.assertRaises(ValueError):
            bug = Bug.objects.create(
                    description="Invalid Bug",
                    bug_type="InvalidType",
                    report_date="2023-10-15",
                    status="To do"
                    )

        valid_bug = Bug.objects.create(
                description="Valid Bug",
                bug_type="Feature",
                report_date="2023-10-15",
                status="To do"
                )
        self.assertEqual(valid_bug.bug_type, "Feature")
