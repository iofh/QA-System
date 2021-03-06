# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
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

"""Commands for creating or manipulating dedicated interconnect attachments."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


class InterconnectAttachments(base.Group):
  """Create or manipulate dedicated interconnect attachments."""
  pass

InterconnectAttachments.detailed_help = {
    'DESCRIPTION': """
        Create or manipulate Dedicated Interconnect attachments.

        For more information about about interconnect attachments for Dedicated
        Interconnect, see the documentation for
        [Dedicated interconnect attachments](https://cloud.google.com/interconnect/docs/how-to/dedicated/creating-vlan-attachments).

        See also: [Interconnect attachments API](https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments).
    """,
}

