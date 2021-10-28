MicroDrill (.rgp) file processing / Version 1

Author: Olga Beketova-Hummel

This work has been made entirely possible by a generous grant from the City of Amsterdam 
(project title: Raamwerk palen Adam, project code: CS2B07, year: 2021).

Licensed with BSD-3 license (see license.txt).

The purpose of the software is to remove the noise and correct for shaft friction from the micro-drill measurements collected by resistograph
in .rpd format.

To run it, change the current path to the folder which contains a set of "MicroDrill (.rgp) file processing / Version 1" codes and .rpd file.
Execute by ".\main.py .\FILENAME.rgp" (in windows).

It is compiled with the collection of python 3 codes. It takes a single .rgp file produced from a single micro-drill measurement, and

 - extracts measured data from .rgp, saves it in .csv, 
 - processes raw data, which is a measurement of resistance per (set via instrument) distance, 
 - adds a moving average curve to the drill amps, 
 - removes 0-values (or anything below a set threshold) that are produced before and after micro-drill instrument enters and exits a pile, based on threshold values, 
 - connects the two thresholds with a slope, and 
 - plots corrected for slope drill amplitude profile.

At the end, there is a .csv file, and multiple plots.
 
Reference Works (shaft friction):

Sharapov, E. S., Xiping Wang, and Elena Smirnova. "Drill bit friction and its effect on resistance drilling measurements in logs." 
20th International Nondestructive Testing and Evaluation of Wood Symposium. 2017.


Nutto, Leif, and Tobias Biechele. "Drilling resistance measurement and the effect of shaft friction–using feed force information for 
improving decay identification on hard tropical wood." Proceedings of the 19th International Nondestructive Testing and Evaluation 
of Wood Symposium, Rio de Janeiro, Brazil. 2015.

Fundova, Irena, Tomas Funda, and Harry X. Wu. "Non-destructive wood density assessment of Scots pine (Pinus sylvestris L.) 
using Resistograph and Pilodyn." PLoS One 13.9 (2018): e0204518.