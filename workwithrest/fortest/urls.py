from . import api_view

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'friend', api_view.FriendViewset),
router.register(r'belonging', api_view.BelongingViewset),
router.register(r'borrow', api_view.BorrowedViewset),