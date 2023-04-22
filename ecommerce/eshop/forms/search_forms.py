from django.forms import CharField, Form, TextInput


class SearchForm(Form):
    search_query = CharField(label='', max_length=100, widget=TextInput(
        attrs={'placeholder': 'Search...'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_query'].widget.attrs['class'] = 'form-control me-1 rounded-start'

    class Meta:
        fields = ["search_query"]
