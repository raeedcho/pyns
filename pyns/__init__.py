"""The pyns package is a full port of the Neuroshare API to Python.

========
Overview
========
The classes and functions provided by this interface do not exactly 
replicate the functions provided by the Neuroshare API.  Instead of 
the function based Neuroshare API, the pyns package was created 
using an OOP style and a focus on having a form natural to 
the Python language.  

This project was put in place by Ripple, after noticing the growing
use of the Python language in the academic and scientific communities.

=======================
Required Python Modules
=======================
The pyns package makes use of a few Python modules outside the default
modules that would be present in any Python installation.  These 
modules are standard for any scientific or computational
use of the Python language and are likely to be present on your system.
If you do you not have any the below package they are easily installed
in a windows system using the Python distribution Python(x, y) which
may be found at: http://www.pythonxy.com.

These modules are:

* numpy - A collection of array manipulation objects and functions.
When data is returned from data in the pyns package, numpy arrays 
are used to package the data for easy use with matplotlib.

* matplotlib - A collection of plotting and analysis objects and functions.  
These are not used explicitly in the pyns package, 
but they are used in all the provided examples.

* psutil - A module containing process utilities for Windows, Linux, and OS X
This module is used to check the available system memory.  Cached data 
for spike waveforms has the potential to arbitrarily large, and a check is made
to ensure enough physical memory is present on a system.  However, files 
large enough to cause problems are unlikely.

==============================
Neuroshare API to pyns Package
==============================
For those familiar the standard Neuroshare API.  Here is a mapping 
of the traditional Neuroshare functions to their pyns equivalent.

The mapping of Neuroshare API to this API for entity classes are 
as follows:

* ns_RESULT ns_OpenFile(pszFilename, hFile)
    
    pyns equivalent: :class:`pyns.NSFile`
* ns_RESULT ns_GetFileInfo(hFile, pFileInfo, dwFileInfoSize)
    
    pyns equivalent: :meth:`pyns.NSFile.get_file_info` 
* ns_RESULT ns_GetEntityInfo(hFile, dwEntityID, pEntityInfo, dwEntityInfoSize) 
    
    pyns equivalent: :meth:`pyns.nsentity.Entity.get_entity_info`
* ns_RESULT ns_GetSegmentInfo(hFile, dwEntityID, dwSourceID, pSegmentInfo, dwSegmentInfoSize) 
                              
    pyns equivalent: :meth:`pyns.nsentity.SegmentEntity.get_seg_source_info`
* ns_RESULT ns_GetSegmentSourceInfo(hFile, dwEntityID, pdwAnalogInfo, dwAnalogInfoSize) 
    
    pyns equivalent: :meth:`pyns.nsentity.SegmentEntity.get_seg_source_info`
* ns_RESULT ns_GetEventInfo(hFile, dwEntityID, pEventInfo, dwEventInfoSize) 
    
    pyns equivalent: :meth:`pyns.nsentity.EventEntity.get_event_info`
* ns_RESULT ns_GetAnalogInfo(hFile, dwEntityID, pAnalogInfo, dwAnalogInfoSize) 
    
    pyns equivalent: :meth:`pyns.nsentity.AnalogEntity.get_analog_info`
* ns_RESULT ns_GetNeuralInfo(hFile, dwEntityID, pNeuralInfo, dwNeuralInfoSize)
    
    pyns equivalent: :meth:`pyns.nsentity.NeuralEntity.get_neural_info`
* ns_RESULT ns_GetEventData(hFile, dwEntityID, pAnalogInfo, dwAnalogInfoSize) 
    
    pyns equivalent: :meth:`pyns.nsentity.EventEntity.get_event_info`
* ns_RESULT ns_GetSegmentData(hFile, dwEntityID, dwIndex, pdTimeStamp, pData, dwDataBufferSize, pdwSampleCount, pdwUnitID)  
                              
    pyns equivalent: :meth:`pyns.nsentity.SegmentEntity.get_segment_data`
* ns_RESULT ns_GetAnalogData(hFile, dwEntityID, dwStartIndex, dwIndexCount, pdwContCount, pData) 
    
    pyns equivalent: :meth:`pyns.nsentity.AnalogEntity.get_analog_data`
* ns_RESULT ns_GetEventData(hFile, dwEntityID, dwIndex, pdTimeStamp, pData, dwDataBufferSize, pdwDataRetSize) 
                            
    
    pyns equivalent: :meth:`pyns.nsentity.EventEntity.get_event_data`
* ns_RESULT ns_GetTimeByIndex(hFile, dwEntityID, dwIndex, pdTime)
    
    pyns equivalent: :meth:`pyns.nsentity.Entity.get_time_by_index`
* ns_RESULT ns_GetIndexByTime(hFile, dwEntityID, dTime, nFile, pdwIndex)
    
    pyns equivlanent: :meth:`pyns.nsentity.Entity.get_index_by_time`

========
Examples
========
A few examples are provided to ease new users to pyns and Python to
this package.

------------------
Simple Entity Dump
------------------
This example will open a nev file, find the associated .nsx files and
print out the result of the :meth:`pyns.nsentity.Entity.get_entity_info` 
function for each entity that was found.


::

    \"\"\"This quick example opens a .nev file named 'test_data.nev'
    and prints the ns_EntityInfo struct for each entity.
    \"\"\"
    from pyns.nsfile import NSFile
    nsfile = NSFile('test_data.nev')
    for entity in nsfile.get_entities():
        print entity.get_info()
"""
# The NSFile is the standard entry point for this package and 
# it will be made easily accessible by importing it from pyns.
from nsfile import NSFile
