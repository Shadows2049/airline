from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'planes', PlaneViewSet)
router.register(r'airlines', CompanyViewSet)
router.register(r'findflight', FindViewSet)
router.register(r'bookflight', BookViewSet)
router.register(r'paymentmethod', GpViewSet)
router.register(r'payforbooking', PFBViewSet)
router.register(r'finalize', FViewSet)
router.register(r'status', StatusViewSet)
router.register(r'cancel', CancelViewSet)
router.register(r'signin', SigninViewSet)
router.register(r'signup', SignupViewSet)
router.register(r'deposit', DepositViewSet)
router.register(r'pay', PayViewSet)
router.register(r'balance', BalanceViewSet)
router.register(r'statement', StatViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]