from rest_framework import serializers
from .models import Property, User, Review

# A mini serializer to show host details safely
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PropertySerializer(serializers.ModelSerializer):
    # 1. Nested Serialization:
    # Instead of just returning "host": 1, this returns the full object:
    # "host": {"id": 1, "username": "alice", ...}
    # read_only=True means we use this for display, but when creating a property,
    # we can still just send the ID.
    host_details = HostSerializer(source='host', read_only=True)
    
    # 2. Calculated Fields (Method Fields):
    # These fields don't exist in the database table, but are calculated on the fly.
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'id', 
            'name', 
            'description', 
            'location', 
            'price_per_night', 
            'host',          # Input: Use this ID when creating (POST)
            'host_details',  # Output: Use this object when reading (GET)
            'average_rating', 
            'review_count',
            'created_at'
        ]

    def get_average_rating(self, obj):
        # 'reviews' is the related_name we defined in the Review model
        reviews = obj.reviews.all()
        if reviews.exists():
            # Calculate average manually or using aggregation
            total = sum([r.rating for r in reviews])
            return round(total / len(reviews), 1)
        return 0

    def get_review_count(self, obj):
        return obj.reviews.count()