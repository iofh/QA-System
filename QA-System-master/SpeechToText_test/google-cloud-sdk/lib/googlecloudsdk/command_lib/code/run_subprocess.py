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
"""Customized versions of runners in subprocess.

Some of this is just for python 2 support and can be simplified.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os.path
import subprocess
from googlecloudsdk.core import config
from googlecloudsdk.core.updater import update_manager
from googlecloudsdk.core.util import files as file_utils
import six


def _FindOrInstallComponent(component_name):
  """Finds the path to a component or install it.

  Args:
    component_name: Name of the component.

  Returns:
    Path to the component. Returns None if the component can't be found.
  """
  if (config.Paths().sdk_root and
      update_manager.UpdateManager.EnsureInstalledAndRestart([component_name])):
    return os.path.join(config.Paths().sdk_root, 'bin', component_name)

  return None


def GetGcloudPreferredExecutable(exe):
  """Finds the path to an executable, preferring the gcloud packaged version.

  Args:
    exe: Name of the executable.

  Returns:
    Path to the executable.
  Raises:
    EnvironmentError: The executable can't be found.
  """
  path = _FindOrInstallComponent(exe) or file_utils.FindExecutableOnPath(exe)
  if not path:
    raise EnvironmentError('Unable to locate %s.' % exe)
  return path


def Run(cmd, show_output=True):
  """Run command and optionally send the output to /dev/null or nul."""
  if show_output:
    subprocess.check_call(cmd)
  else:
    with file_utils.FileWriter(os.devnull) as devnull:
      subprocess.check_call(cmd, stdout=devnull, stderr=devnull)


def GetOutputLines(cmd, show_stderr=True, strip_output=False):
  """Run command and get its stdout as a list of lines.

  Args:
    cmd: List of executable and arg strings.
    show_stderr: False to suppress stderr from the command.
    strip_output: Strip head/tail whitespace before splitting into lines.

  Returns:
    List of lines (without newlines).
  """
  p = subprocess.Popen(
      cmd,
      stdout=subprocess.PIPE,
      stderr=None if show_stderr else subprocess.PIPE)
  stdout, _ = p.communicate()
  text = six.ensure_text(stdout)
  if strip_output:
    text = text.strip()
  lines = text.splitlines()
  return lines


def GetOutputJson(cmd, show_stderr=True):
  """Run command and get its JSON stdout as a parsed dict.

  Args:
    cmd: List of executable and arg strings.
    show_stderr: False to suppress stderr from the command.

  Returns:
    Parsed JSON.
  """
  p = subprocess.Popen(
      cmd,
      stdout=subprocess.PIPE,
      stderr=None if show_stderr else subprocess.PIPE)
  stdout, _ = p.communicate()
  return json.loads(six.ensure_text(stdout).strip())
