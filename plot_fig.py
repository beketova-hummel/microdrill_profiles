import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator)
import os
import types

    ################################
    ################################
    ####  DEFINING FIGS ##########
    ################################
    ################################

def prepare_plots(results):

    plt.close('all')

    figures_height = 4

    #first plot
    fig1, ax1 = plt.subplots(1)
    fig1.suptitle(os.path.basename(results.profile_name) + "  drill and feed profiles")
    fig1.set_figheight(figures_height)
    fig1.set_figwidth(13)   
    
    #second plot
    fig2, ax2 = plt.subplots(1)
    fig2.suptitle(os.path.basename(results.profile_name) + "  drill profile with moving averages, thresholds and slope")
    fig2.set_figheight(figures_height)
    fig2.set_figwidth(13)

    #third plot
    fig3, ax3 = plt.subplots(1)
    fig3.suptitle(os.path.basename(results.profile_name) + "  corrected drill profile")
    fig3.set_figheight(figures_height)
    fig3.set_figwidth(13)


    ################################
    ################################
    ####  FIG 1 ##########
    ################################
    ################################

    ax1.plot(results.depths_original, results.drill_amps_original, label = 'drill amp (%)')
    ax1.plot(results.depths_original, results.feed_amps, label = 'feed amp (%)') 
    ax1.legend()
    ax1.set_ylim(0, 50)
    ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.grid(which = 'minor', alpha = 0.2)
    ax1.grid(which = 'major', alpha = 0.5)
    

    ################################
    ################################
    ####  FIG 2 ##########
    ################################
    ################################

    ax2.plot(results.depths_original, results.drill_amps_original, label = 'drill amp (%)')
    ax2.plot(results.depths_original, results.feed_amps, alpha = 0.5, label = 'feed amp (%)') 
    ax2.plot(results.depths_normalized + results.enter_depth, results.smooth_amps, color='red', alpha = 0.5, label = 'moving ave')
    ax2.annotate('T1', xy=(results.enter_depth, results.enter_amps), xytext=(results.enter_depth, results.enter_amps + 10), ha = 'right', va = 'top', xycoords='data') #textcoords="offset points"
    ax2.annotate('T2', xy=(results.exit_depth, results.exit_amps), xytext=(results.exit_depth, results.exit_amps + 10), xycoords='data', va='top', ha='left')
    ax2.plot([results.enter_depth], [results.enter_amps], 'o', c='green', label = 'threshold 1')
    ax2.plot([results.exit_depth], [results.exit_amps], 'o', c='green', label = 'threshold 2')   
    ax2.plot(np.array([results.enter_depth, results.exit_depth]), np.array([results.enter_amps, results.exit_amps]), '--', c = 'green')
    ax2.legend()
    ax2.set_ylim(0, 50)
    ax2.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax2.grid(which = 'minor', alpha = 0.2)
    ax2.grid(which = 'major', alpha = 0.5)

    ################################
    ################################
    ####  FIG 3 ##########
    ################################
    ################################

    ax3.plot(results.depths_normalized, results.amps_new, label = 'drill amp corrected (%)')
    ax3.legend()
    ax3.set_ylim(0, 50)
    ax3.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax3.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax3.grid(which = 'minor', alpha = 0.2)
    ax3.grid(which = 'major', alpha = 0.5)


    ################################
    ################################
    ####  FIGS LABELS ##########
    ################################
    ################################

    ax1.set_xlim([0,300+results.enter_depth])
    ax1.set_xlabel("Drilling depth (mm)", size = 8)
    ax1.set_ylabel("Amplitude (%)", size = 8)

    ax2.set_xlim([0-results.enter_depth,300])
    ax2.set_xlabel("Drilling depth (mm)", size = 8)
    ax2.set_ylabel("Amplitude (%)", size = 8)

    ax3.set_xlim([0-results.enter_depth,300])
    ax3.set_xlabel("Drilling depth (mm)", size = 8)
    ax3.set_ylabel("Amplitude (%)", size = 8)  

    ################################
    ################################
    ####  SAVING FIGS ##########
    ################################
    ################################

    fig1.savefig((results.profile_name) + "_raw_profiles" + ".png") 
    fig2.savefig((results.profile_name) + "_profiles_w_thresholds" + ".png")
    fig3.savefig((results.profile_name) + "_corrected_profiles" + ".png")  
    plt.show()
    #raise RuntimeError('cancel')
    
    figs = types.SimpleNamespace(
        fig1 = fig1,
        fig2 = fig2, 
        fig3 = fig3 )

    return figs
