from rest_framework import serializers

from dcim.api.serializers import NestedInterfaceSerializer
from ipam.api.serializers import NestedVLANSerializer
from netbox.api.serializers import PrimaryModelSerializer
from wireless.models import *
from .nested_serializers import *

__all__ = (
    'WirelessLANSerializer',
    'WirelessLinkSerializer',
)


class WirelessLANSerializer(PrimaryModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wireless-api:wirelesslan-detail')
    vlan = NestedVLANSerializer(required=False, allow_null=True)

    class Meta:
        model = WirelessLAN
        fields = [
            'id', 'url', 'display', 'ssid', 'description', 'vlan',
        ]


class WirelessLinkSerializer(PrimaryModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wireless-api:wirelesslink-detail')
    interface_a = NestedInterfaceSerializer()
    interface_b = NestedInterfaceSerializer()

    class Meta:
        model = WirelessLAN
        fields = [
            'id', 'url', 'display', 'interface_a', 'interface_b', 'ssid', 'description',
        ]
