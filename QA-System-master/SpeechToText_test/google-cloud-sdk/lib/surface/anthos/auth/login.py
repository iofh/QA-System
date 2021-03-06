# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Authenticate clusters using the Anthos client.."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.anthos import anthoscli_backend
from googlecloudsdk.command_lib.anthos import flags
from googlecloudsdk.command_lib.anthos.common import kube_flags
from googlecloudsdk.core import log


class Login(base.BinaryBackedCommand):
  """Authenticate clusters using the Anthos client."""

  detailed_help = {
      'EXAMPLES': """
      To  add credentials to default kubeconfig file:

          $ {command} --cluster=testcluster --login-config=kubectl-anthos-config.yaml

      To add credentials to custom kubeconfig file:

          $ {command}  --cluster=testcluster --login-config=kubectl-anthos-config.yaml --kubeconfig=my.kubeconfig

      To generate the commands without executing them:

          $ {command} --cluster=testcluster --login-config=kubectl-anthos-config.yaml --dry-run
            """,
  }

  _LOGIN_CONFIG_MESSAGE = 'Configuring Anthos authentication '
  _LOGIN_CONFIG_SUCCESS_MESSAGE = _LOGIN_CONFIG_MESSAGE + 'success.'
  _LOGIN_CONFIG_FAILED_MESSAGE = _LOGIN_CONFIG_MESSAGE + 'failed\n {}'

  def _LoginResponseHandler(self, response):
    if response.stdout:
      log.status.Print(response.stdout)

    if response.stderr:
      log.status.Print(response.stderr)

    if response.failed:
      log.error(self._LOGIN_CONFIG_FAILED_MESSAGE.format(response.stderr))
      return None
    log.status.Print(self._LOGIN_CONFIG_SUCCESS_MESSAGE)
    return response.stdout

  @staticmethod
  def Args(parser):
    kube_flags.GetKubeConfigFlag(
        'Specifies the destination kubeconfig file '
        'where credentials will be stored.').AddToParser(parser)
    flags.GetUserFlag().AddToParser(parser)
    flags.GetClusterFlag().AddToParser(parser)
    flags.GetLoginConfigFlag().AddToParser(parser)
    flags.GetLoginConfigCertFlag().AddToParser(parser)
    flags.GetDryRunFlag('Print out the generated kubectl commands '
                        'but do not execute them.').AddToParser(parser)
    flags.GetSetPreferredAuthenticationFlag().AddToParser(parser)

  def Run(self, args):
    cluster = args.CLUSTER
    config_file = args.login_config
    force_update = args.set_preferred_auth
    anthoscli_backend.GetPreferredAuthForCluster(cluster,
                                                 config_file,
                                                 force_update)
    command_executor = anthoscli_backend.AnthosAuthWrapper()
    log.status.Print(self._LOGIN_CONFIG_MESSAGE)
    response = command_executor(
        command='login',
        cluster=cluster,
        kube_config=args.kubeconfig,
        user=args.user,
        login_config=config_file,
        login_config_cert=args.login_config_cert,
        dry_run=args.dry_run,
        show_exec_error=args.show_exec_error,
        env=anthoscli_backend.GetEnvArgsForCommand())
    return self._LoginResponseHandler(response)
