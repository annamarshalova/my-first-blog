from django import forms

from .models import Post, Video

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image')

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(moderation=True)



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video_file',)


