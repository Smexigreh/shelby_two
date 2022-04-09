from django.shortcuts import render
from .models import Biology
from .models import Chemistry
from .models import English
from .models import History
from .models import Information
from .models import Literature
from .models import Math
from .models import OID
from .models import OBZ
from .models import Physics
from .models import Russian_language
from .models import Social_studies


def biology(request):
    abs_biology = Biology.objects.all()
    count = 0
    for biology in abs_biology:
        if biology:
            count += 1

    return render(request, 'all_abs/biology.html', {'abs_biology': abs_biology, 'count': count})

def chemistry(request):
    abs_chemistry = Chemistry.objects.all()
    count = 0
    for chemistry in abs_chemistry:
        if chemistry:
            count += 1

    return render(request, 'all_abs/chemistry.html', {'abs_chemistry': abs_chemistry, 'count': count})

def english(request):
    abs_english = English.objects.all()
    count = 0
    for english in abs_english:
        if english:
            count += 1

    return render(request, 'all_abs/english.html', {'abs_english': abs_english, 'count': count})

def history(request):
    abs_history = History.objects.all()
    count = 0
    for history in abs_history:
        if history:
            count += 1

    return render(request, 'all_abs/history.html', {'abs_history': abs_history, 'count': count})

def information(request):
    abs_information = Information.objects.all()
    count = 0
    for information in abs_information:
        if information:
            count += 1

    return render(request, 'all_abs/information.html', {'abs_information': abs_information, 'count': count})

def literature(request):
    abs_literature = Literature.objects.all()
    count = 0
    for literature in abs_literature:
        if literature:
            count += 1

    return render(request, 'all_abs/literature.html', {'abs_literature': abs_literature, 'count': count})

def math(request):
    abs_math = Math.objects.all()
    count = 0
    for math in abs_math:
        if math:
            count += 1

    return render(request, 'all_abs/math.html', {'abs_math': abs_math, 'count': count})

def obz(request):
    abs_obz = OBZ.objects.all()
    count = 0
    for obz in abs_obz:
        if obz:
            count += 1

    return render(request, 'all_abs/OBZ.html', {'abs_obz': abs_obz, 'count': count})

def oid(request):
    abs_oid = OID.objects.all()
    count = 0
    for oid in abs_oid:
        if oid:
            count += 1

    return render(request, 'all_abs/OID.html', {'abs_oid': abs_oid, 'count': count})

def physics(request):
    abs_physics = Physics.objects.all()
    count = 0
    for physics in abs_physics:
        if physics:
            count += 1

    return render(request, 'all_abs/physics.html', {'abs_physics': abs_physics, 'count': count})

def russian_language(request):
    abs_russian_language = Russian_language.objects.all()
    count = 0
    for russian_language in abs_russian_language:
        if russian_language:
            count += 1

    return render(request, 'all_abs/russian_language.html', {'abs_russian_language': abs_russian_language, 'count': count})

def social_studies(request):
    abs_social_studies = Social_studies.objects.all()
    count = 0
    for social_studies in abs_social_studies:
        if social_studies:
            count += 1

    return render(request, 'all_abs/social_studies.html', {'abs_social_studies': abs_social_studies, 'count': count})
