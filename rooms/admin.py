from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "total_amenities",
        "country",
        "rating",
        "created_at",
    )

    list_filter = (
        "price",
        "country",
        "address",
        "amenities",
    )

    search_fields = (
        "name",
        "price",
        "owner__username",
    )

    search_help_text = " 방 이름, 가격 혹은 호스트 이름으로 검색하세요. "

    def total_amenities(self, room):
        return room.amenities.count()
        """models.py 혹은 여기에 취사선택 가능"""


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


# Register your models here.
