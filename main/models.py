from django.db import models
from django.contrib.auth.models import User

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

class Ownership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

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
    owned_products = models.ManyToManyField(Product, through='Ownership', related_name='owners', blank=True)
    serial_numbers_vault = models.ManyToManyField(SerialNumber, related_name='owners', blank=True)

    def __str__(self):
        return f"User Storage - {self.user.username}"
