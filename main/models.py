from django.db import models
from django.contrib.auth.models import User


class Feature(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='feature_icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class VariantImage(models.Model):
    image = models.ImageField(upload_to='variant_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"

class Interest(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    proficiency_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    proficiency_level = models.CharField(
        max_length=15,
        choices=proficiency_choices,
        default='Beginner',
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField()
    stock_quantity = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owners = models.ManyToManyField(User, through='Ownership', related_name='owned_products')

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart - {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"CartItem - {self.product.name} ({self.quantity})"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    shipping_address = models.TextField()
    is_completed = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order - #{self.id} ({self.user.username})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem - {self.product.name} ({self.quantity})"

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"

class ProjectProposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, related_name='approved_proposals', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Proposal - {self.project_name} by {self.user.username}"

class ContactSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(User, related_name='resolved_submissions', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Submission - {self.subject} by {self.user.username}"

class OpenSourceProject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    github_url = models.URLField()
    contributors = models.ManyToManyField(User, related_name='contributed_projects')

    def __str__(self):
        return self.name

class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # You can customize the rating scale (e.g., 1 to 5)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating ({self.rating}) by {self.user.username}"

class CommentRating(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Like' if self.is_like else 'Dislike'} by {self.user.username}"

class Device(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields to store device information as needed

    def __str__(self):
        return self.name

class SerialNumber(models.Model):
    serial_key = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    seat_count = models.PositiveIntegerField(default=1)
    devices = models.ManyToManyField(Device, related_name='serial_numbers', blank=True)

    owners = models.ManyToManyField(User, through='Ownership', related_name='owned_serial_numbers')

    def __str__(self):
        return f"Serial Number - {self.serial_key}"

class UserStorage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owned_products = models.ManyToManyField(Product, through='Ownership', related_name='user_storages')
    serial_numbers_vault = models.ManyToManyField(SerialNumber, related_name='user_storages')

    def __str__(self):
        return f"User Storage - {self.user.username}"


class Ownership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(SerialNumber, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    user_storage = models.ForeignKey(UserStorage, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ownership of {self.product.name} by {self.user.username}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    social_media_links = models.JSONField(blank=True, null=True)  # Store social media links as JSON
    skills = models.ManyToManyField('Skill', related_name='user_profiles', blank=True)
    interests = models.ManyToManyField('Interest', related_name='user_profiles', blank=True)
    
    def __str__(self):
        return self.user.username


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    images = models.ManyToManyField('VariantImage', related_name='variants', blank=True)
    features = models.ManyToManyField('Feature', related_name='variants', blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating scale (e.g., 1 to 5)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    pros = models.TextField(blank=True, null=True)
    cons = models.TextField(blank=True, null=True)
    helpful_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.product.name} - {self.user.username}"


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=1)  # Add priority for wishlist items
    custom_fields = models.JSONField(blank=True, null=True)  # Store custom data as JSON
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


from django.db import models
from django.contrib.auth.models import User

class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, unique=True)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending")
    # Add other fields as needed for payment information
    
    def __str__(self):
        return f"Transaction by {self.user.username} - {self.transaction_id}"


class PaymentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    paypal_email = models.EmailField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    payment_history = models.ManyToManyField('PaymentTransaction', related_name='payment_informations', blank=True)
    preferred_payment_method = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=20, blank=True, null=True)  # Type of notification
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE, blank=True, null=True)
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.notification_date}"


