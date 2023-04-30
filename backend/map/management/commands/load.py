import ijson
from django.conf import settings
from django.core.management.base import BaseCommand

from map.models import MapElementModel, MapLayerModel

LAYERS = (
    "incident",
    "schools",
    "kindergartens",
)


class OrganizationFields:
    NAME = "Наименование"
    ADDRESS = "Адрес"
    WORK_HOURS = "Время работы"
    LATITUDE = "Широта"
    LONGITUDE = "Долгота"


class CallFields:
    TYPE = "Тип вызова"
    DESCRIPTION = "Описание"
    TIME = "Время вызова"
    LATITUDE = "Широта"
    LONGITUDE = "Долгота"
    ADDRESS = "Адрес"
    HURT_COUNT = "Количество пострадавших"
    DEATH_COUNT = "Количество погибших"


class Command(BaseCommand):
    help = "Load data"

    def handle(self, *args, **options):
        self.load_layers()
        self.load_calls()

    def load_layers(self):
        for layer in LAYERS:
            try:
                MapLayerModel.objects.create(name=layer)
            except Exception as e:
                print(f"layer {layer} already exist")

    def load_calls(self):
        MapElementModel.objects.all().delete()
        filename = f"{settings.BASE_DIR}/map/management/commands/calls.json"
        layer = MapLayerModel.objects.get(name=LAYERS[0])
        try:
            with open(filename, "rb") as file:

                for record in ijson.items(file, "item"):

                    try:
                        MapElementModel.objects.create(
                            layer=layer,
                            latitude=record.get(CallFields.LATITUDE),
                            longitude=record.get(CallFields.LONGITUDE),
                            address=record.get(CallFields.ADDRESS),
                            name=record.get(CallFields.ADDRESS),
                            metadata=dict(
                                call_type=record.get(CallFields.TYPE),
                                time=record.get(CallFields.TIME),
                                death_count=record.get(CallFields.DEATH_COUNT),
                                hurt_count=record.get(CallFields.HURT_COUNT),
                            ),
                        )
                    except Exception as e:
                        print(e)
                        print("cant read item!!!")
        except Exception as e:
            print("cant parse file")
