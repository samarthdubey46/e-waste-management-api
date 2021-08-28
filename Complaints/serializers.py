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

    class Meta:
        model = Complaint
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        print({**validated_data, 'user': user})
        return Complaint.objects.create(**{**validated_data, 'user': user})
