# PFS_kansoku : Subaru/Gen2 commands to operate PFS

See PFS-GEN-IPM003003 for details.

## /launcher

Launchers (GUI) for some useful commands

PFS.yml
: launchers used for the Runs 01 and 02

## /task 

Device Dependent command and python modules imported in the abstract commands.

PFSdd.py
: Device Dependent command

misc.py
: misc tools for Abstract commands. symbolic link from $OBSHOME/COMMON/pfsmisc.py on Gen2 server.

## /para

Parameters for Device Dependent command.

MCSEXPOSE.para
: take MCS exposure

PFSCMD.para
: Send OneCmnd to an Actor

RELOAD.para
: Reload an Actor

SLEEP.para
: Sleep

## /sk

Abstract commands.

### /SPEC_ENG : for engineering.

PFS_MCS_MULTI_EXP.sk
: Move telescope and take a series of MCS exposure.

PFS_MCS_MULTI_EXP_IIC.sk
: Move telescope and take a series of MCS exposure **through IIC**.

PFS_MCS_MULTI_EXP2.sk
: Interlace telescope movement and MCS exposure.

PFS_MCS_PFI_ROTCENTER.sk
: Rotate and calculate PFI rotation center on MCS detector.

PFS_POPT2_MOVE.sk
: Hexapod operation. Calculates ADC position for default setting.

PFS_POPT2_MOVE2.sk
: Hexapod operation. Calculates ADC position for all ADC settings.

PFS_MCS_CHECK.sk
: MCS health check

PFS_FIBRE_LIGHT.sk
: Turn on/off LEDs

PFS_SPS_EXPOSURE.sk
: SpS exposure (bias, dark, arc, trace)

PFS_SPS_EXPOSURE.sk
: Abort SpS exposure

PFS_DOMELAMP_EXP.sk
: Sps exposure using dome flat lamp and dome room lamp.
