
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import main

from django.urls import path
from .views import main , test_page



router = DefaultRouter()
router.register(r'features', FeatureViewSet)
router.register(r'variant_images', VariantImageViewSet)
router.register(r'interests', InterestViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'followers', FollowerViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'project-proposals', ProjectProposalViewSet)
router.register(r'contact-submissions', ContactSubmissionViewSet)
router.register(r'open-source-projects', OpenSourceProjectViewSet)
router.register(r'product-ratings', ProductRatingViewSet)
router.register(r'comment-ratings', CommentRatingViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'serial-numbers', SerialNumberViewSet)
router.register(r'user-storages', UserStorageViewSet)
router.register(r'ownerships', OwnershipViewSet)
router.register(r'user-preferences', UserPreferencesViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'product-variants', ProductVariantViewSet)
router.register(r'product-reviews', ProductReviewViewSet)
router.register(r'shipping-addresses', ShippingAddressViewSet)
router.register(r'wishlist-items', WishlistItemViewSet)
router.register(r'payment-transactions', PaymentTransactionViewSet)
router.register(r'payment-informations', PaymentInformationViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('main', main, name="main"),    
    path('', main, name="main"),  
    path('test/', test_page),  
]