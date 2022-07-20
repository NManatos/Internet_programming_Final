#from rest_framework import serializers
#from .models import Event,User


# class EventSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     description = serializers.CharField( max_length=100)
#     location = serializers.CharField(max_length=64)
#     seats = serializers.IntegerField()
#     price = serializers.FloatField()
#     category = serializers.CharField(max_length=64)
#     coverImg = serializers.ImageField()
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Event.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Event` instance, given the validated data.
#         """
#         instance.description = validated_data.get('description', instance.description)
#         instance.location = validated_data.get('location', instance.location)
#         instance.seats = validated_data.get('seats', instance.seats)
#         instance.price = validated_data.get('price', instance.price)
#         instance.category = validated_data.get('category', instance.category)
#         instance.coverImg = validated_data.get('coverImg ', instance.coverImg)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']