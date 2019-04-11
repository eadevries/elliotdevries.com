from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    body = models.TextField()
    urgency = models.SmallIntegerField(default=0)
    handled = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def body_preview(self):
        return (self.body[:50] + "[...]") if len(self.body) > 50 else self.body

    def __str__(self):
        return self.subject[:50]


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    order = models.IntegerField(default=100)
    blurb = models.TextField(blank=True)
    external_link = models.URLField(blank=True)
    external_link_text = models.CharField(max_length=100, blank=True)
    icon_choices = (
        ('PAPER_AIRPLANE', 'Paper Airplane'),
        ('SQUARE_ROOT', 'Square Root'),
        ('TETRIS_BLOCK', 'Tetris Block'),
    )
    icon = models.CharField(max_length=50, choices=icon_choices)
    full_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def icon_classes(self):
        icon_dict = {
            'PAPER_AIRPLANE': 'far fa-paper-plane',
            'SQUARE_ROOT': 'fas fa-square-root-alt',
            'TETRIS_BLOCK': 'fas fa-th-large'
        }
        return icon_dict.get(self.icon, "not found")
