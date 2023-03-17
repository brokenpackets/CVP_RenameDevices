from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Device
import json
import ssl

# Ignore untrusted/self-signed certificates.
ssl._create_default_https_context = ssl._create_unverified_context

# Stage device image with gold standard.
# Uses the image bundle applied to the Undefined container, but can be manually configured for a specific image.

#### User Vars
serialMapping = {'serial':'hostname',
                 'ssj88888888':'sw8-test',
                 }
undefinedContainerName = 'Undefined' # modify this if user has renamed the Undefined container.
#### Script Logic

def main():
    if CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_STATE) == 'true': # If device in ztp state, continue.
        device_serial = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
        if device_serial in serialMapping.keys():
            device_ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP) # Get Device IP
            device_user = CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_USERNAME) # Get CVP temp username for ZTP.
            device_pass =CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_PASSWORD) # Get CVP temp password for ZTP.
            device = Device(device_ip,device_user,device_pass) # Create eAPI session to device via Device library.
            try:
                hostname = serialMapping[device_serial]
                print hostname
                device.runCmds(['enable','configure','hostname '+hostname])
            except:
                print 'failure on '+device_ip
    else:
        pass
    #end device set-up.

if __name__ == "__main__":
    main()
