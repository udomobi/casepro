import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageBoardComment",
            fields=[
                ("id", models.AutoField(verbose_name="ID", serialize=False, auto_created=True, primary_key=True)),
                ("object_pk", models.TextField(verbose_name="object ID")),
                ("user_name", models.CharField(max_length=50, verbose_name="user's name", blank=True)),
                ("user_email", models.EmailField(max_length=254, verbose_name="user's email address", blank=True)),
                ("user_url", models.URLField(verbose_name="user's URL", blank=True)),
                ("comment", models.TextField(max_length=3000, verbose_name="comment")),
                ("submit_date", models.DateTimeField(default=None, verbose_name="date/time submitted", db_index=True)),
                (
                    "ip_address",
                    models.GenericIPAddressField(unpack_ipv4=True, null=True, verbose_name="IP address", blank=True),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True,
                        help_text="Uncheck this box to make the comment effectively disappear from the site.",
                        verbose_name="is public",
                    ),
                ),
                (
                    "is_removed",
                    models.BooleanField(
                        default=False,
                        help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.',
                        verbose_name="is removed",
                    ),
                ),
                ("pinned_on", models.DateTimeField(null=True, blank=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        related_name="content_type_set_for_messageboardcomment",
                        verbose_name="content type",
                        to="contenttypes.ContentType",
                        on_delete=models.PROTECT,
                    ),
                ),
                ("site", models.ForeignKey(to="sites.Site", on_delete=models.PROTECT)),
                (
                    "user",
                    models.ForeignKey(
                        related_name="messageboardcomment_comments",
                        on_delete=django.db.models.deletion.SET_NULL,
                        verbose_name="user",
                        blank=True,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("submit_date",),
                "abstract": False,
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "permissions": [("can_moderate", "Can moderate comments")],
            },
        )
    ]
