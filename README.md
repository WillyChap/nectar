# Nectar

A lightweight python package that analyzes weather station temperature data from Colorado Climate Center (https://climate.colostate.edu/data_access_new.html) and data from Project Feederwatch (https://feederwatch.org/) to compare estimated flowering day of year using growing degree days (GDD) and estimated hummingbird arrival day of year for four species of migratory hummingbirds in the Front Range of Colorado.

# DATA
The raw FeederWatch dataset (~1.6 GB) is not included in this repository due to GitHub file size limits.
Users must download it separately from (https://feederwatch.org/explore/raw-dataset-requests/) and place it in the data/ directory before running the scripts. The user can not download more than more subset of data from the website. If you wish to look at the entire dataset (1988-2024) please download raw data and concatenate before running script. 


> **Data source:**   
> Colorado Climate Center Station Data provided by Colorado State University
> 
> Project Feederwatch Data provided by Cornell Lab of Ornithology

# Problems and Motivation
Scientists are already witnessing the impacts of global temperature increase on wildlife populations. More specifically, on migratory wildlife populations, including species of hummingbirds. Migratory hummingbirds, including the broad-tailed hummingbird _(Selasphorus Platycercus)_, black-chinned hummingbird _(Archilochus alexandri)_, Rufous hummingbird _(Selasphorus rufus)_, and calliope hummingbird _(Stellula calliope)_ use the Rocky Mountain region between April through August, before returning to their wintering grounds. However, with increasing temperatures across this region, it is hypothesized that peak flowering is occurring earlier than historically recorded. In turn, hummingbirds arriving during typical migration periods miss peak flowering, and thus lack adequate food availability. For this project, I am focusing on a subset of the Mountain West Region and analyzing temporal mismatch occuring in the Front Range of Colorado: Boulder, Castle Rock, and Fort Collins. 

# Usage

Nectar is intended to be used for scientists and wildlife officials to determine temporal mismatch between hummingbird arrivalals and flowering bloom time. This package outputs dataframes with the sume of gorwing degree days over all years (1988-2024), average estimated hummingbird arrival day of year (DOY), an estimated flowering DOY for all of the existing data years provided, the number of days of temporal mismatch, and the mean temporal mismatch over all of the years analyzed. Additionally, the plotting functionality provides a graph plotting esimated hummingbird arrival over time, estimated flowering day over time, and the overall temporal mismatch (in days) over time. 

## Installation

```bash
pip install -e .
```

Or from source:

```bash
git clone [(https://github.com/chandnir2/atoc4815_nectar.git)]
cd nectar
pip install -e .
```

## Command Line - this does not work yet

```bash
run-nectar    # generates outputs/flowering_vs_arrival.png and data/mismatch.png & csv files
```

## Files

- `cleaning.py` — read and clean raw Feederwatch data 
- `mismatch_analysis.py` — main functions
- `plotting.py` — plots temporal mismatch, flowering day of year, and hummingbird arrival day of year
- `run.py` — Driver script

## License

MIT
