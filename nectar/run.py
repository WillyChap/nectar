from nectar.functions.cleaning import clean_feederwatch
from nectar.functions.mismatch_analysis import run_mismatch_analysis
from nectar.functions.plotting import run_plots


def main():

    """
    Runs full nectar workflow

    1. Cleans raw FeederWatch hummingbird observation data
    2. Computes phenological mismatch between:
        - hummingbird arrival timing
        - flowering timing (using growing degree days)
    3. Generates output plots:
        - phenology timing over time
        - mismatch trends over time

    Workflow outputs are saved automatically to the configured OUTPUT_DIR.

    Returns
    -------
    pd.DataFrame
        Final mismatch results containing:
        - arrival_doy
        - flowering_doy
        - mismatch_days
    """
    print("\n===================================")
    print(f"HUMMINGBIRD ARRIVAL VS. FLOWER BLOOM")
    print("===================================\n")

    
    # CLEAN DATA
  
    print(f"Cleaning FeederWatch data...")
    fw_df = clean_feederwatch()
    print("   ✓ Cleaning complete\n")

    
    # TEMPORAL MISMATCH ANALYSIS
   
    print(f"Running mismatch analysis...")
    results = run_mismatch_analysis(fw_df=fw_df)
    print("   ✓ Analysis complete\n")

    # PLOTTING RESULTS
   
    print(f"Generating plots...")
    run_plots(results)
    print("   ✓ Plotting complete\n")

    # -----------------------------
    # COMPLETE
    # -----------------------------
    print("===================================")
    print(f"ANALYSIS COMPLETE")
    print(f"Data and plots saved to /outputs")
    print("===================================\n")

    return results


if __name__ == "__main__":
    main()