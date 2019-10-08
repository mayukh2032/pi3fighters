
# Sets up the development environment for Cloud ML on Cloud Shell.
# Quit early if any command fails.
set -ex 
# Some pip installed tools are added to ~/.local/bin, which should be # added to the PATH.
if [[ ":${PATH}:" != *":${HOME}/.local/bin:"* ]]; then echo "Updating PATH" PATH=${HOME}/.local/bin:${PATH} echo 'export PATH=${HOME}/.local/bin:${PATH}' >> ~/.bashrc fi


pip3 install --user -U pillow

pip3 install --user -U numpy


pip3 install --user -U pandas 

pip3 install --user -U scikit-learn


pip3 install --user -U pyyaml


pip3 install --user -U scipy

# Install TensorFlow. 


pip3 install --user -U https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.14.0-cp37-cp37m-linux_x86_64.whl

# Install cloud ML SDK

pip3 install --user -U cloud-ml-sdk

# Download Samples
curl -L -o cloudml-samples.zip https://github.com/GoogleCloudPlatform/cloudml-samples/archive/master.zip

# UNZIP Samples

unzip cloudml-samples.zip

# Move to Samples

mv cloudml-samples-master/ samples/

# Update Path Variable

export PATH=${HOME}/.local/bin:${PATH}

# check environment

# Check that the Cloud ML SDK is installed.

 curl https://raw.githubusercontent.com/mayukh2032/pi3fighters/master/checkPi3Environment.py | python3


