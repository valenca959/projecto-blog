from django.core.management.base import BaseCommand, CommandError
from blog.models import Post
from django.utils.text import slugify


class Command(BaseCommand):
    """"
    This class is a command that creates a new post to the database

    $ python manage.py add_post -- title "title" --content "content"
    """
    help = "creates a new post to the database"

    def add_arguments(self, parser):
        parser.add_argument("--title", type=str, help="Title of the post", required=True)
        parser.add_argument("--content", type=str, help="Content of the post", required=True)

    def handle(self, *args, **options):
        try:
            post = Post.objects.create(
                title=options["title"],
                slug=slugify(options["title"]),
                content=options["content"],
            )
        except Exception as e:
            raise CommandError(f"An error occurred: {e}")
        else:
            self.stdout.write(self.style.SUCCESS(f"Post {post.title} created successfully"))
        