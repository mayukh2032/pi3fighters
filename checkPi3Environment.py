#!/usr/bin/env python3

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Checks that the development environment is configured for Cloud ML."""

from __future__ import print_function
import pkg_resources
import re
import subprocess
import sys

MIN_CLOUD_ML_SDK_VERSION = '0.1.8a0'
MIN_CLOUD_SDK_VERSION = '136.0.0'
MIN_TENSORFLOW_VERSION = '0.11.0rc0'

def get_version_from_pip(package_name):
  """Returns the version of an installed pip package."""
  try:
    package_info = subprocess.check_output(['pip', 'show', package_name])
  except subprocess.CalledProcessError:
    print('ERROR: Package %s has not been installed with pip.' % package_name,
          file=sys.stderr)
    exit(1)
  for line in package_info.split('\n'):
    m = re.match(r'Version: (.+)', line)
    if m:
      return m.group(1)
  print('ERROR: Unable to parse "pip show" output: %s' % package_info,
        file=sys.stderr)
  exit(1)

def get_cloud_sdk_version():
  """Returns the version of the Cloud SDK that is installed."""
  gcloud_info = subprocess.check_output(['gcloud', 'version'])
  for line in gcloud_info.split('\n'):
    m = re.match(r'Google Cloud SDK (.+)', line)
    if m:
      return m.group(1)
  print('ERROR: Unable to parse "gcloud version" output: %s' % gcloud_info,
        file=sys.stderr)
  exit(1)

def check_version_is_supported(name, version, min_version, help=''):
  """Checks whether a particular version of a package is new enough."""
  if (pkg_resources.parse_version(version) <
      pkg_resources.parse_version(min_version)):
    # Version is too old.
    print('ERROR: Unsupported %s version: %s (minimum %s).%s' %
              (name, version, min_version, (' %s' % help) if help else ''),
          file=sys.stderr)
    exit(1)

# Check that TensorFlow is installed.
import tensorflow as tf
check_version_is_supported('TensorFlow', tf.__version__, MIN_TENSORFLOW_VERSION)


# Everything completed successfully.
print('Success! Your environment is configured correctly.')
