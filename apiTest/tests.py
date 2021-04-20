from django.test import TestCase
from apiTest.models import Project
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTest(TestCase):
    def setUp(self):
        print("开始测试")
        #user = User.objects.get(id=1)
        Project.objects.create(name="project_001", version="1.0", createUser_id=1)

    def testGetProjetctByName(self):
        project = Project.objects.get(name="project_001")
        self.assertEqual(project.version, "1.0")
        self.assertEqual(project.type, "Web")
        self.assertEqual(project.status, True)
        self.assertEqual(project.createUser_id, 1)

    def tearDown(self):
        project = Project.objects.get(name="project_001")
        project.delete()
