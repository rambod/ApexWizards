from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/index.html')

<<<<<<< HEAD

from rest_framework import viewsets
from .models import *
from serializer import *

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class VariantImageViewSet(viewsets.ModelViewSet):
    queryset = VariantImage.objects.all()
    serializer_class = VariantImageSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ProjectProposalViewSet(viewsets.ModelViewSet):
    queryset = ProjectProposal.objects.all()
    serializer_class = ProjectProposalSerializer

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

class OpenSourceProjectViewSet(viewsets.ModelViewSet):
    queryset = OpenSourceProject.objects.all()
    serializer_class = OpenSourceProjectSerializer

class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer

class CommentRatingViewSet(viewsets.ModelViewSet):
    queryset = CommentRating.objects.all()
    serializer_class = CommentRatingSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class SerialNumberViewSet(viewsets.ModelViewSet):
    queryset = SerialNumber.objects.all()
    serializer_class = SerialNumberSerializer

class UserStorageViewSet(viewsets.ModelViewSet):
    queryset = UserStorage.objects.all()
    serializer_class = UserStorageSerializer

class OwnershipViewSet(viewsets.ModelViewSet):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer

class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class WishlistItemViewSet(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class PaymentTransactionViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer

class PaymentInformationViewSet(viewsets.ModelViewSet):
    queryset = PaymentInformation.objects.all()
    serializer_class = PaymentInformationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
=======
def test_page(request):
    context = {
        'test' : [1,2,3,4,5,6],
    }
    return render(request, 'main/test.html',context=context)
>>>>>>> ad96b624c1f79ccccc430dbfe5c8675826081a95
