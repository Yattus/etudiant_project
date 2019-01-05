from datetime import datetime
from Etudiant.models import Domaine


def get_infos(request):
    return {'date_actuelle': datetime.now(),
            'domaines': Domaine.objects.all()
            }
