
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
