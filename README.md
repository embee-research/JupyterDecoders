# JupyterDecoders
Various decoders related to Jupyter malware. 

The `JupyterAESDecoder.py` script is aimed at a persistent command often deployed by jupyter into shell extension handlers. 
This script assumes that you have
- the base64 encoded file that Jupyter often stores on disk
- The AES key stored in the persistent command

Usage
`python JupyterAESdecoder.py --key <AES_key> --file <path_to_file>`

The logic that is imitated can be seen here
![image](https://user-images.githubusercontent.com/82847168/178676048-c9c3b9f0-738a-4543-90a1-3f6ad161b7e2.png)

An equivalent Cyberchef recipe observed here
![image](https://user-images.githubusercontent.com/82847168/178676328-3cefa22e-6510-4568-9f1d-142f6a93fc1d.png)
