from django.core.management import BaseCommand

from lms.models import Lesson, Course
from users.models import User, Payments


class Command(BaseCommand):

    def handle(self, *args, **options):

        course_list = [
            {'name': 'kiloCourse',
             'preview': None,
             'description': 'kiloCourse, have 1 lesson'},
            {'name': 'MegaCourse',
             'preview': None,
             'description': 'MegaCourse, have 2 lessons'},
            {'name': 'GigaCourse',
             'preview': None,
             'description': 'GigaCourse, have 3 lessons'},
            {'name': 'TeraCourse',
             'preview': None,
             'description': 'TeraCourse, have 4 lessons'}
        ]

        course_to_create = [Course(**category) for category in course_list]
        Course.objects.all().delete()
        Course.objects.bulk_create(course_to_create)

        lesson_list = [
            {
                'name': 'lesson 1',
                'description': 'It`s in kiloCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[0],
             },
            {
                'name': 'lesson 2',
                'description': 'It`s in MegaCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[1],
            },
            {
                'name': 'lesson 3',
                'description': 'It`s in MegaCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[1],
            },
            {
                'name': 'lesson 4',
                'description': 'It`s in GigaCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[2],
            },
            {
                'name': 'lesson 5',
                'description': 'It`s in GigaCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[2],
            },
            {
                'name': 'lesson 6',
                'description': 'It`s in GigaCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[2],
            },
            {
                'name': 'lesson 7',
                'description': 'It`s in TeraCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[3],
            },
            {
                'name': 'lesson 8',
                'description': 'It`s in TeraCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[3],
            },
            {
                'name': 'lesson 9',
                'description': 'It`s in TeraCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[3],
            },
            {
                'name': 'lesson 10',
                'description': 'It`s in TeraCourse',
                'preview': None,
                'video_link': 'link(it`s not)',
                'course': course_to_create[3],
            },
        ]

        lessons_to_create = [Lesson(**product) for product in lesson_list]
        Lesson.objects.all().delete()
        Lesson.objects.bulk_create(lessons_to_create)

        payments_list = [
            {
                'user': None,
                'course': course_to_create[0],
                'lesson': None,
                'payed_amount': 420,
                'payment_method': 'CS',
            },
            {
                'user': None,
                'course': None,
                'lesson': lessons_to_create[3],
                'payed_amount': 69,
                'payment_method': 'CS',
            },
            {
                'user': None,
                'course': course_to_create[0],
                'lesson': None,
                'payed_amount': 420,
                'payment_method': 'TR',
            },
            {
                'user': None,
                'course': course_to_create[1],
                'lesson': None,
                'payed_amount': 420,
                'payment_method': 'TR',
            },
            {
                'user': None,
                'course': course_to_create[3],
                'lesson': None,
                'payed_amount': 420,
                'payment_method': 'TR',
            },
            {
                'user': None,
                'course': None,
                'lesson': lessons_to_create[3],
                'payed_amount': 69,
                'payment_method': 'CS',
            },
            {
                'user': None,
                'course': None,
                'lesson': lessons_to_create[6],
                'payed_amount': 69,
                'payment_method': 'TR',
            },
            {
                'user': None,
                'course': None,
                'lesson': lessons_to_create[7],
                'payed_amount': 69,
                'payment_method': 'CS',
            }
        ]

        lessons_to_create = [Payments(**product) for product in payments_list]
        Payments.objects.all().delete()
        Payments.objects.bulk_create(lessons_to_create)