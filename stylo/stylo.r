# make sure to install the Stylo package for R in order to run this code

library(stylo)

# the config below creates a nodes and edges csv for network analysis in gephi 
# additionally it creates a bootstrap consensus tree (100-1000 MFW, 10 iterations with 100 MFW increment)
stylo(
  gui = FALSE,                # run without GUI
  network = TRUE,             # enable edges/nodes csv output
  network.tables = "both",    # config for both edges and nodes csv output
  corpus.dir = "corpus",      # directory for corpus

  # Feature settings
  mfw.min = 100,              # start at 100 MFW
  mfw.max = 1000,             # go up to 1000 MFW
  mfw.incr = 1,               # increase by 100 each time
  culling.min = 0,
  culling.max = 0, 


  # Distance & analysis
  analysis.type = "BCT",       # Multidem
  distance.measure = "dist.delta", 
  write.png.file = TRUE,       # saves the consensus tree as jpg
  consensus.strength=0.5,
  group.delimiter = "_"       # color coding based on prefix, delimiter = _
)

