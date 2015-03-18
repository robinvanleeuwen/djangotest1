from django.forms import ModelForm
from django.shortcuts import redirect, render
from app.models import Recipient


class RecipientForm(ModelForm):

    class Meta:
        model = Recipient
        fields = ["name1", "name2", "street","zip", "country", "phone1"]



def save_recipient():
    import sys
    print sys.stdout, "Saving Recipient data"


def get_recipient(request, template_name="recipient.html"):

    form = RecipientForm(request.POST or None)
    if form.is_valid():

        save_recipient()
        return redirect("recipient.html")

    return render(request, template_name, {'form': form})