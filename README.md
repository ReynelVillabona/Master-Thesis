# Read-me

Automated workflow to request from your localhost computation to another server using their data but using the computation you have in your localhost.

### Virtual Machine

Operating system : Ubuntu 20_04-lts-gen2
Public IP: 20.251.115.193
Username: azureuser


## Streamlit

page 1 : The buttom will create a .txt file in the virtual machine

page 2 : It will sum up the column a and b of a sqlite table that is in the VM machine created.

## How to run 

Before starting, communicate with me so I can start running the Virtual Machine created in Azure.

Open a powershell windows shell, check the status of your SSH by using "Get-Service sshd" then if if stopped start it using "Start-Service sshd".
Remember you have to configure yourself OpenSSH server and client to do SSH request.

Open the streamlit code and run it using "streamlit run app.py", you have to install streamlit if you do not have it "pip streamlit"

Go to Page 2 in streamlit adn press the buttom it will take a few seconds and it will display the sum of the two numbers of the SQLite table created in the Ubuntu Virtual Machine 

Go to Windows PowerShell, run "ssh -i C:\path\to\private\key.pem azureuser@20.251.115.193" in order to acces to the virtual machine.

### Under construction

