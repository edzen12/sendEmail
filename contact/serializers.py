from rest_framework import serializers

from contact.models import Person
from contact.tasks import send_info


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        person = super().create(validated_data)
        person.save()
        send_info(
            person.name,
            person.lastName,
            person.patronymic,
            person.phone,
            person.email,
            person.dateOfBirth,
            person.passNumber,
            person.address,
            person.analysisDate,
            person.completeDate,
        )
        return person
