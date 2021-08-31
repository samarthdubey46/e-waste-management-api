from rest_framework import serializers

from .models import Complaint


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class ComplaintSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(allow_null=True, read_only=True)
    status = ChoiceField(choices=Complaint.TICKET_STATUS, default=Complaint.TICKET_STATUS[0][0])
    priority = ChoiceField(choices=Complaint.PRIORITY_CHOICES, default=Complaint.PRIORITY_CHOICES[0][0])
    image_1 = serializers.ImageField(allow_null=True, required=True,  allow_empty_file=True,max_length=None)
    image_2 = serializers.ImageField(allow_null=True, required=False, allow_empty_file=True,max_length=None)
    image_3 = serializers.ImageField(allow_null=True, required=False, allow_empty_file=True,max_length=None)
    image_4 = serializers.ImageField(allow_null=True, required=False, allow_empty_file=True,max_length=None)

    class Meta:
        model = Complaint
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        print({**validated_data, 'user': user})
        return Complaint.objects.create(**{**validated_data, 'user': user})


class ComplaintListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='get_image')
    status = ChoiceField(choices=Complaint.TICKET_STATUS, default=Complaint.TICKET_STATUS[0][0])
    priority = ChoiceField(choices=Complaint.PRIORITY_CHOICES, default=Complaint.PRIORITY_CHOICES[0][0])

    class Meta:
        model = Complaint
        fields = ['id', 'title', 'status', 'priority', 'created_at', 'image']
