# vCloud Air CLI 0.1
#
# Copyright (c) 2014 VMware, Inc. All Rights Reserved.
#
# This product is licensed to you under the
# Apache License, Version 2.0 (the "License").
# You may not use this product except in compliance with the License.
#
# This product may include a number of subcomponents with
# separate copyright notices and license terms. Your use of the source
# code for the these subcomponents is subject to the terms and
# conditions of the subcomponent's license, as noted in the LICENSE file.
#


import click
from vca_cli import cli, utils


@cli.command()
@click.pass_context
def example(ctx):
    """vCloud Air CLI Examples"""
    headers = ['Id', 'Example', 'Flavor', 'Command']
    example_id = 0
    table = []
    example_id += 1
    table.append([example_id, 'login to service', 'vCA',
                  'vca login email@company.com --password ****'])
    example_id += 1
    table.append([example_id, 'login to an instance', 'vCA',
                  'vca login email@company.com --password ****'
                  ' --instance c40ba6b4-c158-49fb-b164-5c66f90344fa'])
    example_id += 1
    table.append([example_id, 'login to a virtual data center', 'vCA',
                  'vca login email@company.com --password ****'
                  ' --instance c40ba6b4-c158-49fb-b164-5c66f90344fa'
                  ' --vdc VDC1'])
    example_id += 1
    table.append([example_id, 'login to service', 'vCHS',
                  'vca login email@company.com --password ****'
                  ' --host vchs.vmware.com --version 5.6'])
    example_id += 1
    table.append([example_id, 'login to an instance', 'vCHS',
                  'vca login email@company.com --password ****'
                  ' --host vchs.vmware.com --version 5.6'
                  ' --instance 55-234 --org MyOrg'])
    example_id += 1
    table.append([example_id, 'login to a virtual data center', 'vCHS',
                  'vca login email@company.com --password ****'
                  ' --host vchs.vmware.com --version 5.6'
                  ' --instance 55-234 --org MyOrg --vdc MyVDC'])
    example_id += 1
    table.append([example_id, 'login to vCloud Director', 'Standalone',
                  'vca login email@company.com --password ****'
                  ' --host myvcloud.company.com --version 5.5 --org MyOrg'])
    example_id += 1
    table.append([example_id, 'login to vCloud Director and VDC',
                  'Standalone',
                  'vca login email@company.com --password ****'
                  ' --host myvcloud.company.com --version 5.5 --org MyOrg'
                  ' --vdc MyVDC'])
    example_id += 1
    table.append([example_id, 'list available instances', 'vCA, vCHS',
                  'vca instance'])
    example_id += 1
    table.append([example_id, 'show details of instance', 'vCA, vCHS',
                  'vca instance info --instance '
                  'c40ba6b4-c158-49fb-b164-5c66f90344fa'])
    example_id += 1
    table.append([example_id, 'select an instance', 'vCA',
                  'vca instance use --instance '
                  'c40ba6b4-c158-49fb-b164-5c66f90344fa'])
    example_id += 1
    table.append([example_id, 'select an instance and VDC', 'vCA',
                  'vca instance use --instance '
                  'c40ba6b4-c158-49fb-b164-5c66f90344fa '
                  '--vdc MyVDC'])
    example_id += 1
    table.append([example_id, 'select an instance', 'vCHS',
                  'vca instance use --instance '
                  'M684216431-4470 --org M684216431-4470'])
    example_id += 1
    table.append([example_id, 'list organizations', 'All',
                  'vca org'])
    example_id += 1
    table.append([example_id, 'show organization details', 'All',
                  'vca org info'])
    example_id += 1
    table.append([example_id, 'select an organization', 'vCHS',
                  'vca org use --instance 55-234 --org MyOrg'])
    example_id += 1
    table.append([example_id, 'list VDC templates', 'All',
                  'vca org list-templates'])
    example_id += 1
    table.append([example_id, 'list VDC', 'All',
                  'vca vdc'])
    example_id += 1
    table.append([example_id, 'select VDC', 'All',
                  'vca vdc use --vdc vdc1'])
    example_id += 1
    table.append([example_id, 'create VDC', 'All',
                  'vca vdc create --vdc vdc2 --template d2p3v29-new-tp'])
    example_id += 1
    table.append([example_id, 'delete VDC (will prompt to confirm)', 'All',
                  'vca vdc delete --vdc vdc2'])
    example_id += 1
    table.append([example_id, 'delete VDC without prompt', 'All',
                  'vca vdc delete --vdc vdc2 --yes'])
    example_id += 1
    table.append([example_id, 'list catalogs and items', 'All',
                  'vca catalog'])
    example_id += 1
    table.append([example_id, 'create catalog', 'All',
                  'vca catalog create --catalog mycatalog'])
    example_id += 1
    table.append([example_id, 'delete catalog', 'All',
                  'vca catalog delete --catalog mycatalog'])
    example_id += 1
    table.append([example_id, 'delete catalog item', 'All',
                  'vca catalog delete-item --catalog mycatalog'
                  ' --item my_vapp_template'])
    example_id += 1
    table.append([example_id, 'upload media file (ISO) to catalog',
                  'All',
                  'vca catalog upload --catalog mycatalog'
                  ' --item esxi.iso --description ESXi-iso'
                  ' --file ~/VMware-VMvisor.iso'])
    example_id += 1
    table.append([example_id, 'list vApps',
                  'All',
                  'vca vapp'])
    example_id += 1
    table.append([example_id, 'create vApp',
                  'All',
                  'vca vapp create --vapp myvapp --vm myvm'
                  ' --catalog'
                  ' \'Public Catalog\' --template \'Ubuntu'
                  ' Server 12.04 LTS (amd64 20150127)\''])
    example_id += 1
    table.append([example_id, 'create vApp',
                  'All',
                  'vca vapp create -a myvapp -V myvm -c'
                  ' mycatalog -t mytemplate'
                  ' -n default-routed-network -m pool'])
    example_id += 1
    table.append([example_id, 'create vApp with manually assigned IP',
                  'All',
                  'vca vapp create -a myvapp -V myvm -c'
                  ' mycatalog -t mytemplate'
                  ' -n default-routed-network -mode manual'
                  ' --ip 192.168.109.25'])
    example_id += 1
    table.append([example_id, 'create multiple vApps',
                  'All',
                  'vca vapp create -a myvapp -V myvm -c'
                  ' mycatalog -t mytemplate'
                  ' -n default-routed-network -m pool'
                  ' --count 10'])
    example_id += 1
    table.append([example_id, 'create vApp and configure VM size',
                  'All',
                  'vca vapp create -a myvapp -V myvm -c'
                  ' mycatalog -t mytemplate'
                  ' -n default-routed-network -m pool'
                  ' --cpu 4 --ram 4096'])
    example_id += 1
    table.append([example_id, 'delete vApp',
                  'All',
                  'vca vapp delete --vapp myvapp'])
    example_id += 1
    table.append([example_id, 'show vApp details in JSON',
                  'All',
                  'vca -j vapp info --vapp myvapp'])
    example_id += 1
    table.append([example_id, 'deploy vApp',
                  'All',
                  'vca vapp deploy --vapp ubu'])
    example_id += 1
    table.append([example_id, 'undeploy vApp',
                  'All',
                  'vca vapp undeploy --vapp ubu'])
    example_id += 1
    table.append([example_id, 'power on vApp',
                  'All',
                  'vca vapp power-on --vapp ubu'])
    example_id += 1
    table.append([example_id, 'power off vApp',
                  'All',
                  'vca vapp power-off --vapp ubu'])
    example_id += 1
    table.append([example_id, 'customize vApp VM',
                  'All',
                  'vca vapp customize --vapp ubu --vm ubu'
                  ' --file add_public_ssh_key.sh'])
    example_id += 1
    table.append([example_id, 'insert ISO to vApp VM',
                  'All',
                  'vca vapp insert --vapp coreos1 --vm coreos1'
                  ' --catalog default-catalog'
                  ' --media coreos1-config.iso'])
    example_id += 1
    table.append([example_id, 'eject ISO from vApp VM',
                  'All',
                  'vca vapp eject --vapp coreos1 --vm coreos1'
                  ' --catalog default-catalog'
                  ' --media coreos1-config.iso'])
    example_id += 1
    table.append([example_id, 'attach disk to vApp VM',
                  'All',
                  'vca vapp attach --vapp myvapp'
                  ' --vm myvm --disk mydisk'])
    example_id += 1
    table.append([example_id, 'detach disk from vApp VM',
                  'All',
                  'vca vapp detach --vapp myvapp'
                  ' --vm myvm --disk mydisk'])
    example_id += 1
    table.append([example_id, 'list independent disks',
                  'All',
                  'vca vapp disk'])
    example_id += 1
    table.append([example_id, 'create independent disk of 100GB',
                  'All',
                  'vca disk create --disk mydisk'
                  ' --size 100'])
    example_id += 1
    table.append([example_id, 'delete independent disk by name',
                  'All',
                  'vca disk delete --disk mydisk'])
    example_id += 1
    table.append([example_id, 'delete independent disk by id',
                  'All',
                  'vca disk delete'
                  ' --id bce76ca7-29d0-4041-82d4-e4481804d5c4'])
    example_id += 1
    table.append([example_id, 'list user roles', 'vCA',
                  'vca role'])
    example_id += 1
    table.append([example_id, 'list users', 'vCA',
                  'vca user'])
    example_id += 1
    table.append([example_id, 'change current user password', 'vCA',
                  'vca user change-password --password current-pass'
                  ' --new-password new-pass'])
    example_id += 1
    table.append([example_id, 'create user', 'vCA',
                  'vca user create --user usr@com.com --first Name'
                  " --last Name --roles 'Virtual Infrastructure Administrator,"
                  " Network Administrator'"])
    example_id += 1
    table.append([example_id, 'list edge gateways',
                  'All',
                  'vca gateway'])
    example_id += 1
    table.append([example_id, 'get details of edge gateway',
                  'All',
                  'vca gateway info'])
    example_id += 1
    table.append([example_id, 'set syslog server on gateway',
                  'All',
                  'vca gateway set-syslog'
                  ' --ip 192.168.109.2'])
    example_id += 1
    table.append([example_id, 'unset syslog server on gateway',
                  'All',
                  'vca gateway set-syslog'])
    example_id += 1
    table.append([example_id, 'allocate external IP address',
                  'vCA',
                  'vca gateway add-ip'])
    example_id += 1
    table.append([example_id, 'release external IP address',
                  'vCA',
                  'vca gateway del-ip --ip 107.189.93.162'])
    example_id += 1
    table.append([example_id, 'show status', 'All',
                  'vca status'])
    example_id += 1
    table.append([example_id, 'show status and password', 'All',
                  'vca status --show-password'])
    example_id += 1
    table.append([example_id, 'list profiles', 'All',
                  'vca profile'])
    example_id += 1
    table.append([example_id, 'switch to a profile', 'All',
                  'vca --profile p1 <command>'])
    example_id += 1
    table.append([example_id, 'send debug to $TMPDIR/pyvcloud.log', 'All',
                  'vca --debug vm'])
    example_id += 1
    table.append([example_id, 'show version', 'All',
                  'vca --version'])
    example_id += 1
    table.append([example_id, 'show general help', 'All',
                  'vca --help'])
    example_id += 1
    table.append([example_id, 'show command help', 'All',
                  'vca <command> --help'])
    utils.print_table('vca-cli usage examples:',
                      headers, table)