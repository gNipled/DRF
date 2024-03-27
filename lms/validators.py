from rest_framework import serializers

YOUTUBE_LINKS = ('youtube.com', 'youtu.be',)


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is None:
            return
        for link in YOUTUBE_LINKS:
            if link in tmp_val:
                return
        raise serializers.ValidationError('Wrong link, please use youtube for videos')
