import splitfolders 

inputfolder = (r"C:\Users\Clarissa\Downloads\curated_data")
outputfolder = (r"C:\Users\Clarissa\Downloads\DataSplitting\DataSplit")
splitfolders.ratio(inputfolder, outputfolder, seed=42, ratio=(.8, .2))

help(splitfolders .ratio)