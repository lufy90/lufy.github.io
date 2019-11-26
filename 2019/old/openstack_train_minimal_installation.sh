
## Keyston installation
yum install openstack-keystone httpd mod_wsgi

## glance installation
yum install openstack-glance

## placement installation
yum install openstack-placement-api

## nova instalation
# on controller node
yum install openstack-nova-api openstack-nova-conductor \
  openstack-nova-novncproxy openstack-nova-scheduler
# on compute node 
yum install openstack-nova-compute

## neutron installation
# controller node
yum install openstack-neutron openstack-neutron-ml2 \
  openstack-neutron-linuxbridge ebtables
# compute node
yum install openstack-neutron-linuxbridge ebtables ipset

