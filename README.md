# Real time Face Detection (FD) demo application
This application is adopted/restructured from the DYVERSE open source project (https://github.com/qub-blesson/DYVERSE). For full details on DYVERSE, please refer to Wang et al. [DYVERSE - DYnamic VERtical Scaling in Multi-tenant Edge Environments](https://arxiv.org/pdf/1810.04608.pdf). From the DYVERSE project, we only modified the Face detection application.  For original structure of the Face detection application and other aspects of the DYVERSE project, please refer to the original repo (https://github.com/qub-blesson/DYVERSE). The details, of the restructured FD application, are as follows:

The key changes in the application from the original include:
1. The development of a client component to be used for the Raspberry pi.
2. The EdgeServer component is distributed into three smaller component.
3. Docker containerisation support added.

The description of each component can be found in their respective directories.

# How to Use
We intend to use the FD application in integration with MiCADO-Scale for our in progress work, i.e. the extension of MiCADO-Scale to handle orchestration and runtime management of IoT applications in the cloud-fog-edge ecosystem. The details will appear soon here.  

The FD application can also used independently, i.e. without MiCADO-Scale. The usage details of each component can be found in the respective readme files. 