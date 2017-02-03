from cpdashboard.models import Initiative, Objective, Perspective
from rest_framework import serializers

class InitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiative
        fields = ('id','description','objective', 'code_suffix', 'performance_measure', 'target', 'debit_code',\
            'weight', 'scheduled_start_date', 'scheduled_end_date', 'actual_start_date', \
            'projected_end_date', 'actual_end_date', 'budgeted_cost', 'projected_end_cost',\
            'actual_cost', 'budgeted_manhours', 'projected_manhours', 'actual_manhours', 'created_on', \
            'image')
    def create(self, validated_data):
        """ Create and return a new 'Initiative instance, given the validated data'"""
        return Initiative.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Initiative' instance, given the validated data
        """
        instance.description = validated_data.get('description', instance.description )
        instance.actual_start_date = validated_data.get('actual_start_date', instance.actual_start_date)
        instance.projected_end_date = validated_data.get('projected_end_date', instance.projected_end_date)
        instance.projected_end_cost = validated_data.get('projected_end_cost', instance.projected_end_cost)
        instance.actual_cost = validated_data.get('actual_cost', instance.actual_cost )
        instance.budgeted_manhours = validated_data.get('budgeted_manhours', instance.budgeted_manhours)
        instance.save()
        return instance


class ObjectiveSerializer(serializers.ModelSerializer):
    initiatives = serializers.PrimaryKeyRelatedField(many=True, queryset=Initiative.objects.all())

    green  = serializers.SerializerMethodField()
    red = serializers.SerializerMethodField()
    amber = serializers.SerializerMethodField()
    initiatives_url = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()
    
    def get_green(self, obj):
        return obj.green
    def get_amber(self, obj):
        return obj.amber
    def get_red(self, obj):
        return obj.red
    def get_initiatives_url(self, obj):
        return obj.get_initiatives_url()
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Objective
        fields = ('id', 'description', 'code', 'objective_commentary', 'result','perspective', 'initiatives', 'red', 'green', 'amber', 'initiatives_url', 'absolute_url')


class PerspectiveSerializer(serializers.ModelSerializer):
    objectives = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Perspective
        fields = ('id', 'description', 'objectives')
