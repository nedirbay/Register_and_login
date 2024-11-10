from django.contrib import admin
from . import models
import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def process_pdf_and_save(text):
    lines = text.split('\n')
    maddalar = []
    madda = ""

    for line in lines:
        if line.startswith('1-nji madda'):
            madda = ''
            maddalar.clear()
        if '-nji madda' in line and line.index('-nji madda') < 5 or '-njy madda' in line and line.index('-njy madda') < 5:
            madda += "\n"
            maddalar.append(madda)
            print(madda)
            madda = ""
            madda += line + "\n"
        else:
            madda += line + "\n"

    maddalar.append(madda)
    return maddalar
    
def save_db(filename,maddalar):
    for madda in maddalar:
        models.Maddalar.objects.create(kanun=filename,maddalar=madda)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','user','text','created_at')
    list_display_links = ('id','user','text','created_at')
    list_filter = ('id','user','text','created_at')
    search_fields = ('text',)

class KanunUploadAdmin(admin.ModelAdmin):
    list_display = ('id','name','file')
    list_display_links = ('id','name','file')
    search_fields=('name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        text = extract_text_from_pdf(obj.file.path)
        maddalar=process_pdf_and_save(text)
        save_db(obj.name,maddalar)
        

class MaddalarAdmin(admin.ModelAdmin):
    list_display = ('id','kanun','maddalar')
    list_display_links = ('id','kanun','maddalar')
    search_fields = ('kanun','maddalar')

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.KanunUpload,KanunUploadAdmin)
admin.site.register(models.Maddalar,MaddalarAdmin)
admin.site.register(models.Answers)