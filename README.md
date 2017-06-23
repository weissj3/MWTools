# MWTools
A set of tools designed to be used with the MilkyWay@home client.
Sweep Program:
  -Create parameter sweeps (one and two dimensional)
  -Utilizes GPU and CPUs to improve run time (Faster to use only GPU in small searches)
SGRBHB:
  -A few python scripts used to plot BHBs from the Sagittarius and Bifurcated streams in the North Galactic Cap SDSS data.
  -Data for these scripts should be receiving from SDSS using the queries:
    SELECT objID, psfMag_u, psfMag_g, psfMag_r, psfMagErr_u, psfMagErr_g, psfMagErr_r, extinction_u, extinction_g, extinction_r, ra, dec, l, b, Star.specObjID, LOGGADOP, LOGGADOPUNC, LOGGSPEC, LOGGSPECUNC, LOGGWBG, LOGGWBGUNC, FEHSPEC, FEHSPECUNC, ELODIERVFINAL, ELODIERVFINALERR, SNR from dbo.Star, dbo.sppParams
WHERE dbo.Star.specObjID = dbo.sppParams.SPECOBJID
  AND (((psfMag_u - extinction_u) - (psfMag_g - extinction_g)) BETWEEN 0.8 AND 1.5)
  AND (((psfMag_g - extinction_g) - (psfMag_r - extinction_r)) BETWEEN -0.3 AND 0)
  AND b > 30.0;
  -Any data obtained from other queries will require modifications to the script to select different columns in the resultant star .csv files.
  -Things that could be done to improve this script include getting the column number from the top row of the file.
  -Can also look into ways to run map only once per column and then save the results for future use.
Metallicity Plots:
  -Working on a new project which requires mapping the metallicty of the Milky Way disk using our tracer stars.
  -Query used to get data will be provided after the work is done.
  -Need to add the ability to plot in galactic B and distance, where distance is calculated using absolute magnitude derived from metallicty and isochrones.
